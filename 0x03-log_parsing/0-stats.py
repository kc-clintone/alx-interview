#!/usr/bin/python3
"""
Script to read stdin line by line and compute metrics.
"""


import sys
import signal


total_file_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_stats():
    """
    Prints the computed statistics.
    """
    print(f"Total file size: {total_file_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

def signal_handler(sig, frame):
    """
    Handles the keyboard interruption (CTRL + C) and prints the stats.
    """
    print_stats()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        line_count += 1
        try:
            parts = line.split()
            ip_address = parts[0]
            status_code = int(parts[-2])
            file_size = int(parts[-1])

            total_file_size += file_size

            if status_code in status_codes:
                status_codes[status_code] += 1

        except (IndexError, ValueError):
            continue

        if line_count % 10 == 0:
            print_stats()

except Exception as e:
    print(f"Error: {e}")

print_stats()

