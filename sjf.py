def sjf(process_list):
    """
    Simulates Shortest Job First (SJF) CPU scheduling for a list of processes.
    Each process is represented as a list [burst_time, arrival_time, process_id].
    
    Args:
        process_list (list): A list of processes where each process is a list
                             containing [burst_time, arrival_time, process_id].

    Outputs:
        Prints the Gantt chart and completion metrics for each process.
    """

    t = 0  # Current time of the CPU scheduler
    gantt = []  # List to store the Gantt chart (sequence of executed processes)
    completed = {}  # Dictionary to store completed process metrics (CT, TT, WT)

    # While there are processes remaining to be scheduled
    while process_list != []:
        available = []  # List of processes available for execution at the current time t

        # Check which processes have arrived (arrival time <= current time)
        for p in process_list:
            if p[1] <= t:  # If the process has arrived
                available.append(p)

        # If no processes are available at the current time
        if available == []:
            t += 1  # Increment time
            gantt.append("idle")  # CPU is idle
            continue  # Skip to the next iteration of the loop

        # Sort the available processes by burst time (ascending order)
        available.sort()

        # Select the process with the shortest burst time
        process = available[0]
        burst_time = process[0]  # Burst time of the selected process
        arrival_time = process[1]  # Arrival time of the selected process
        pid = process[2]  # Process ID of the selected process

        # Execute the selected process
        t += burst_time  # Advance time by the burst time of the process
        gantt.append(pid)  # Add the process ID to the Gantt chart

        # Calculate completion metrics for the process
        ct = t  # Completion Time (time at which the process finishes execution)
        tt = ct - arrival_time  # Turnaround Time (total time spent in the system)
        wt = tt - burst_time  # Waiting Time (time spent waiting in the ready queue)

        # Remove the process from the process list (as it has been executed)
        process_list.remove(process)

        # Store the calculated metrics for the completed process
        completed[pid] = [ct, tt, wt]

    # Print the Gantt chart showing the order of process execution
    print("Gantt Chart:", gantt)

    # Print completion metrics for each process in a readable format
    print("\nCompleted Processes:")
    print("PID\tCompletion Time\tTurnaround Time\tWaiting Time")
    for pid, metrics in completed.items():
        print(f"{pid}\t{metrics[0]}\t\t{metrics[1]}\t\t{metrics[2]}")


if __name__ == "__main__":
    """
    Allow the user to input the process list interactively.
    """
    process_list = []

    print("Enter process details. When done, type 'done'.")
    while True:
        user_input = input("Enter burst time, arrival time, and process ID (comma-separated): ")
        if user_input.lower() == 'done':
            break

        try:
            burst_time, arrival_time, process_id = user_input.split(",")
            burst_time = int(burst_time.strip())
            arrival_time = int(arrival_time.strip())
            process_id = process_id.strip()

            process_list.append([burst_time, arrival_time, process_id])
        except ValueError:
            print("Invalid input. Please enter the details in the format: burst_time, arrival_time, process_id")

    # Call the SJF scheduling function with the process list
    sjf(process_list)