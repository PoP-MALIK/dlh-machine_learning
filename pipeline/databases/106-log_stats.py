#!/usr/bin/env python3
"""Improve 34-log_stats.py by adding the top 10 of the most present IPs"""
"""in the collection nginx of the database logs"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")
    collection = client.logs.nginx
    total_logs = collection.count_documents({})
    print("{} logs".format(total_logs))
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, count))
    status_check = collection.count_documents({
            "method": "GET",
            "path": "/status"
    })
    print("{} status check".format(status_check))

    ip_count = {}
    logs = collection.find()
    for log in logs:
        ip = log.get("ip")
        if ip in ip_count:
            ip_count[ip] += 1
        else:
            ip_count[ip] = 1
    sorted_ips = sorted(ip_count.items(),
        key=lambda x: x[1],
        reverse=True
    )
    print("IPs:")
    for ip, count in sorted_ips[:10]:
        print("\t{}: {}".format(ip, count))

