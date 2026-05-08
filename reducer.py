import sys

current_log = None
current_count = 0

for line in sys.stdin:
    log_type, count = line.strip().split('\t')
    count = int(count)

    if current_log == log_type:
        current_count += count
    else:
        if current_log:
            print(current_log, current_count)

        current_log = log_type
        current_count = count

# Print last log type
if current_log:
    print(current_log, current_count)