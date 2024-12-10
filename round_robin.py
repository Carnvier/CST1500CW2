# Get user input for quantum time and number of processes
quantum = float(input("Enter quantum: "))  # Amount of time each process is allowed to run
no_processes = int(input("Enter number of processes: "))
count = 0
processes = {}  # Dictionary to keep each process info

# Enter process details
while no_processes > count:
    process = input("Enter process name: ")
    burst_time = int(input("Enter burst time: "))
    arrival_time = int(input("Enter arrival time: "))
    processes[process] = {
        'burst_time': burst_time,
        'arrival_time': arrival_time,
        'remaining_time': burst_time  # Track remaining burst time
    }
    count += 1

# Sort processes by arrival time
processes = dict(sorted(processes.items(), key=lambda item: item[1]['arrival_time']))

print("\nProcess Scheduling:")

# Round Robin Scheduling
time = 0  # Initialize current time
while processes:
    # Track if any process was executed in this round
    executed = False
    
    for process in list(processes.keys()):  # Use list to avoid modifying the dictionary during iteration
        remaining_time = processes[process]['remaining_time']
        arrival_time = processes[process]['arrival_time']
        
        # Check if the process has arrived
        if arrival_time <= time:
            executed = True  # Mark that at least one process was executed
            
            # Process execution
            if remaining_time > quantum:
                time += quantum  # Increment time by quantum
                processes[process]['remaining_time'] -= quantum  # Decrease remaining time
                print(f"{process} executed for {quantum} time units. Remaining time: {processes[process]['remaining_time']}")
            else:
                time += remaining_time  # Process completes
                print(f"{process} executed for {remaining_time} time units and completed.")
                del processes[process]  # Remove completed process
        else:
            # If the process hasn't arrived yet, skip to the next
            continue

    # If no process was executed in this round, increment time to the next available process
    if not executed:
        time += 1 