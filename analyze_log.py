from collections import defaultdict
import re
import os

def analyze_log_file(filename):
    try:
        with open(filename, "r") as f:
            log_lines = f.readlines()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return

    error_count = 0
    unique_ips = set()
    url_counts = defaultdict(int)

    for line in log_lines:
        match = re.search(
            r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) - "
            r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - "
            r"\"GET (.+) HTTP/1.1\" (\d+)", line)
        
        if match:
            timestamp, ip, url, status_code = match.groups()
            unique_ips.add(ip)
            url_counts[url] += 1
            if int(status_code) >= 400:
                error_count += 1

    print(f"Total Errors (4xx and 5xx): {error_count}")
    print(f"Unique IP Addresses: {len(unique_ips)}")
    print("URL Access Counts:")
    for url, count in url_counts.items():
        print(f"    {url}: {count}")

analyze_log_file("access.log")