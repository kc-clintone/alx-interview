#!/usr/bin/python3
"""
Script to compute metrics from log file lines, tracking
total file size and HTTP status codes.
"""


import signal
import sys


total_file_size = 0
status_codes_count = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}

def print_stats():
    """
    Print the statistics collected so far.
    """
    print(f"File size: {total_file_size}")
    for code in sorted(status_codes_count):
        if status_codes_count[code] > 0:
            print(f"{code}: {status_codes_count[code]}")

def process_line(line):
    """
    Process a line of input to update the metrics.
    """
    global total_file_size
    try:
        parts = line.split()
        if len(parts) < 7:
            return

        status_code = int(parts[-2])
        file_size = int(parts[-1])

        total_file_size += file_size

        if status_code in status_codes_count:
            status_codes_count[status_code] += 1

    except (ValueError, IndexError):
        return

def signal_handler(sig, frame):
    """
    Handle the Ctrl+C signal to print the stats before exiting.
    """
    print_stats()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)


if __name__ == "__main__":
    line_count = 0

    for line in sys.stdin:
        process_line(line)
        line_count += 1

        if line_count == 10:
            print_stats()
            line_count = 0

    if line_count > 0:
        print_stats()
