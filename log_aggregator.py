import redis

r = redis.Redis(host="localhost", port=6379, password="Redis@123", decode_responses=True)

print("Waiting for logs....")

while True:
    log = r.brpop("logs__queue")[1]

    with open("aggregated_logs.txt", "a") as f:
        f.write(log + "\n")

    print(f"Processed: {log}") 
