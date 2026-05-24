import redis
import sys

r = redis.Redis(host="localhost", port=6379, password="Redis@123", decode_responses=True)

if len(sys.argv) < 2:
    print("Usage: python log_producer.py '<message>'")
    sys.exit(1)

message = sys.argv[1]

r.lpush("logs__queue", message)

print(f"Log sent: {message}")
