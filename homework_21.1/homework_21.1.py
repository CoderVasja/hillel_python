from datetime import datetime


def parse_timestamp(line):

    timestamp_start = line.find("Timestamp ") + len("Timestamp ")
    timestamp_str = line[timestamp_start:timestamp_start + 8]
    return datetime.strptime(timestamp_str, "%H:%M:%S")


def analyze_heartbeat(log_file, key):

    filtered_log = []

    with open(log_file, 'r') as file:
        for line in file:
            if key in line:
                filtered_log.append(line.strip())


    with open('hb_test.log', 'w') as output_file:
        for i in range(len(filtered_log) - 1):
            current_time = parse_timestamp(filtered_log[i])
            next_time = parse_timestamp(filtered_log[i + 1])
            time_diff = (current_time - next_time).total_seconds()

            if 31 < time_diff < 33:
                output_file.write(f"WARNING: Heartbeat difference {time_diff} seconds at {current_time}\n")
            elif time_diff >= 33:
                output_file.write(f"ERROR: Heartbeat difference {time_diff} seconds at {current_time}\n")



analyze_heartbeat('hblog.txt', 'TSTFEED0300|7E3E|0400')