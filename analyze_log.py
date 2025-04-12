from collections import defaultdict
import re
import os

from sklearn.metrics import log_loss


def analyze_log_file(filename="access.log"):


    try:
        with open(filename, "r") as f:
            log_lines = f.readlines()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

    # set up variables to store the datetime, error count, unique IPs, and URL counts for the log file.
for line in log_loss:
    match = re.search(r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) - (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \"GET (.+) HTTP/1.1\" (\d+)", line)
    if match:
        timestamp, ip, url, status_code = match.groups()
   
error_count = 0

unique_ips = set()

url_counts = defaultdict(int)


unique_ips.add(ip)

url_counts[url] += 1

if int(status_code) >= 400:
        error_count += 1
   
print(f"Total Errors (4xx and 5xx): {error_count}")
   
print(f"Unique IP Addresses: {len(unique_ips)}")

print("URL Access Counts:")
for url, count in url_counts.items(): 
        print(f"    {url}: {count}")
   
   
   
