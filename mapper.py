import sys

for line in sys.stdin:
    words = line.strip().split()

    log_type = words[1]

    print(f"{log_type}\t1")