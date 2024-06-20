# Log Parsing

This script reads input from stdin line by line and computes metrics based on the specified format. It processes log entries containing an IP address, date, HTTP request, status code, and file size. If the format does not match, the line is skipped.

## Input Format

The expected input format is as follows:

```
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
```

## Metrics

After every 10 lines or a keyboard interruption (CTRL + C), the script prints the following statistics:

1. **Total file size:** The sum of all previous file sizes encountered.
2. **Number of lines by status code:** Counts of each status code (200, 301, 400, 401, 403, 404, 405, and 500).

### Example Output

```
Total file size: File size: 123456
200: 5
404: 2
500: 1
```
