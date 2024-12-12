# variable definition
processes = {}
time = 0
process_count = 0

# Input process detailS
while True:
    try:
        no_processes = int(input("What is the number of processes running: "))
        if no_processes <= 0:
            raise ValueError("The number of processes must be a positive integer.")
        break
    except ValueError as e:
        print(e)
while True:
    try:
        quantum_time = float(input("Please enter the quantum: "))
        if quantum_time <= 0:
            raise ValueError("Quantum time must be a positive number.")
        break
    except ValueError as e:
        print(e)
while process_count < no_processes:
    name = input(f"Enter the name of process {process_count + 1}: ")
    while True:
        try:
            burst_time = int(input(f"Enter the burst time for process {process_count + 1}: "))
            if burst_time < 0:
                raise ValueError("Burst time must be a non-negative integer.")
            break
        except ValueError as e:
            print(e)
    while True:
        try:
            arrival_time = int(input(f"Enter the arrival time for process {process_count + 1}: "))
            if arrival_time < 0:
                raise ValueError("Arrival time must be a non-negative integer.")
            break
        except ValueError as e:
            print(e)

    processes[name] = {
        'burst_time': burst_time,
        'arrival_time': arrival_time,
        'remaining_time': burst_time,
        'waiting_time': 0
    }

    process_count += 1


# Sorting the processes based on their arrival times
processes = dict(sorted(processes.items(), key=lambda item: item[1]['arrival_time']))

# Round Robin Scheduling
while True:
    run = False
    for process in list(processes.keys()):
        # Skip the process if it hasn't arrived yet
        if processes[process]["arrival_time"] > time:
            continue
        
        # Check if the process can finish within the quantum time
        if processes[process]["remaining_time"] < quantum_time and processes[process]["remaining_time"] > 0:
            time += processes[process]["remaining_time"]
            processes[process]['waiting_time'] += time - processes[process]['arrival_time'] - processes[process]['burst_time']
            processes[process]['remaining_time'] = 0
            print(f"{process} completed at time {time}")
        elif processes[process]["remaining_time"] > quantum_time:
            # Process runs for the quantum time
            processes[process]['remaining_time'] -= quantum_time
            time += quantum_time
            
    

        # If there is remaining time, mark that a process was executed
        if processes[process]['remaining_time'] > 0:
            run = True

    # Exit the loop if no process was executed
    if not run:
        break
    

# Output results
print("\nName\t\tArrival Time\tBurst Time\tWaiting Time")
for process in processes.keys():
    print(f"{process}\t\t{processes[process]['arrival_time']}\t\t{processes[process]['burst_time']}\t\t{processes[process]['waiting_time']}")