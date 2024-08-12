# Log Metrics Script

This project is a Python script designed to process log files in a specific format and generate metrics based on the log data. The script reads lines from standard input, extracts information such as HTTP status codes and file sizes, and periodically prints out statistics.

## Features

- **Reads lines from stdin:** The script processes each line of input as it is read.
- **Supports a specific log format:** The script expects log lines to match a format that includes an IP address, a timestamp, an HTTP request, a status code, and a file size.
- **Computes metrics:** The script tracks the total file size and counts the occurrences of specific HTTP status codes.
- **Periodic output:** Every 10 lines, or when interrupted by a keyboard signal (Ctrl + C), the script prints the accumulated statistics.

## Log Format

The script expects each line of input to follow this format:

```
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
```

### Example:

```
192.168.0.1 - [2024-08-12] "GET /projects/260 HTTP/1.1" 200 1024
```

If a line does not conform to this format, it is ignored.

## Statistics

The script tracks the following statistics:

- **Total file size:** The cumulative size of all files mentioned in the log entries.
- **Number of lines by status code:** The count of occurrences for each of the following HTTP status codes: 200, 301, 400, 401, 403, 404, 405, 500.

### Output Example:

After processing lines, the script will output something like:

```
File size: 10240
200: 8
404: 2
```

## How to Use

1. **Clone the Repository:**

    ```sh
    git clone https://github.com/kc-clintone/0x03-log_parsing.git
    cd 0x03-log_parsing
    ```

2. **Make the Script Executable (Optional):**

    If you want to run the script directly:

    ```sh
    chmod +x 0-stats.py
    ```

3. **Run the Script:**

    You can pipe a log file into the script:

    ```sh
    ./0-generator.py | ./0-stats.py
    ```

    Or run it directly and input lines manually:

    ```sh
    python3 0-stats.py
    ```

    For each line processed, the script updates its metrics, and after every 10 lines or upon receiving a Ctrl + C interruption, it prints the statistics.

## Implementation Details

- **Input Handling:** The script reads from `stdin`, making it flexible to be used with files or manual input.
- **Signal Handling:** The script catches `SIGINT` (Ctrl + C) to print the current statistics before exiting.
- **Error Handling:** The script gracefully handles lines that do not match the expected format by skipping them.
