# Distributed Logging System — Part 1: Redis Setup

A DevOps project configuring Redis as a centralized message queue, laying the foundation for a multi-part distributed logging system.

Built as part of the **DevOps + SRE Daily Challenge Series**.

---

## Overview

Part 1 covers installing and configuring Redis on AWS EC2, securing it with password authentication, exposing it for external connections, and validating queue operations both locally and remotely.

---

## Architecture

```
MacBook
   ↓
AWS Security Group
   ↓
EC2 Instance (Ubuntu)
   ↓
Redis Server
   ↓
logs_queue
```

---

## Environment

| Component | Details |
|---|---|
| Cloud Provider | AWS |
| Compute | EC2 (Ubuntu) |
| Message Queue | Redis |
| Client Tool | redis-cli |

---

## Setup

### 1. Install Redis

```bash
sudo apt update && sudo apt install redis-server -y
redis-server --version
```

### 2. Configure Redis

Edit `/etc/redis/redis.conf` and update the following:

```
# Enable password authentication
requirepass Redis@123

# Allow external connections
bind 0.0.0.0
```

Restart and verify:

```bash
sudo systemctl restart redis-server
sudo systemctl status redis-server
```

### 3. Authenticate and Test

```bash
redis-cli
AUTH Redis@123
PING         # Expected: PONG
```

### 4. Create the Log Queue

Redis Lists are used as a simple message queue:

```bash
LPUSH logs_queue "Application Started"
LPUSH logs_queue "User Login Successful"
LPUSH logs_queue "Database Connected"
```

Validate the queue:

```bash
LLEN logs_queue       # Check queue length
LRANGE logs_queue 0 -1  # View all entries
```

### 5. Test Remote Connectivity

From a local MacBook:

```bash
redis-cli -h <EC2_PUBLIC_IP> -p 6379
AUTH Redis@123
PING         # Expected: PONG
```

> Make sure port `6379` is open in your AWS Security Group inbound rules.

---

## Key Learnings

- Redis installation and service management on EC2
- Difference between binding to `127.0.0.1` vs `0.0.0.0`
- Password-based authentication using `requirepass`
- Using Redis Lists (`LPUSH`, `LLEN`, `LRANGE`) as a message queue
- AWS Security Group configuration for external access
- Foundation concepts behind distributed logging systems

---

## Screenshots

| Screenshot | Description |
|---|---|
| `redis-version.png` | Redis installation verified |
| `redis-running.png` | Redis service status |
| `redis-auth-ping.png` | Authentication and PING test |
| `queue-length.png` | Queue length after LPUSH |
| `queue-content.png` | Queue contents via LRANGE |

---

## What's Next

In **Part 2**, the Redis queue will be integrated with log producers and consumers to simulate a full centralized logging workflow.

---

## Author

**Manik Singhal**
DevOps + SRE Daily Challenge Series
