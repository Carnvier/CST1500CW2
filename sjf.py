# Shortest Job First (SJF) Scheduling Algorithm

def sjf(process_list):
    t = 0  # Current time
    gantt = []  # Gantt chart representation
    completed = {}  # Dictionary to store completion times, turnaround times, and waiting times

    while process_list:
        available = []
        for p in process_list:
            if p[1] <= t:  # Check if the process has arrived
                available.append(p)

        # No processes available
        if not available:
            t += 1
            gantt.append("idle")
            continue
        else:
            # Sort available processes by burst time, then by arrival time
            available.sort(key=lambda x: (x[0], x[1]))  # Sort by burst time, then arrival time
            process = available[0]  # Select the process with the shortest burst time

            # Service the process
            burst_time = process[0]
            pid = process[2]
            arrival_time = process[1]
            t += burst_time  # Update current time
            gantt.append(pid)  # Update Gantt chart

            # Calculate completion time, turnaround time, and waiting time
            ct = t
            tt = ct - arrival_time  # Turnaround time
            wt = tt - burst_time  # Waiting time

            # Remove the completed process from the list
            process_list.remove(process)
            completed[pid] = [ct, tt, wt]  # Store completion information

    # Print the Gantt chart and completion information
    print("Gantt Chart:", gantt)
    print("Process Completion Information:")
    print("PID\tCT\tTT\tWT")
    for pid, times in completed.items():
        print(f"{pid}\t{times[0]}\t{times[1]}\t{times[2]}")

if __name__ == "__main__":
    # List of processes in the format [burst_time, arrival_time, process_id]
    process_list = [[6, 2, "p1"], [2, 5, "p2"], [8, 1, "p3"], [3, 0, "p4"], [4, 0, "p5"]]
    sjf(process_list)