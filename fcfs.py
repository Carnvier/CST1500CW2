# First Come First Serve
"""
TT = total time
CT = current time
BT = burst time

Process (arrival_time, burst_time, pid)
"""

import pandas as pd

def fcfs():
    print("Welcome to the FCFS scheduling program!")
    n = int(input("Enter the number of processes: "))

    processes = []
    for i in range(n):
        print(f"\nProcess {i + 1}:")
        process_id = input("Enter Process ID: ")
        arrival_time = int(input("Enter Arrival Time: "))
        burst_time = int(input("Enter Burst Time: "))
        processes.append((process_id, arrival_time, burst_time))

    # Sort processes by arrival time
    df = pd.DataFrame(processes)
    df = df.sort_values(by="Arrival Time").reset_index(drop=True)

    # Initialize columns for completion, turnaround, and waiting times
    df['Completion Time'] = 0
    df['Turnaround Time'] = 0
    df['Waiting Time'] = 0

    # Caalculate FCFS scheduling metrics
    current_time = 0
    for i in range(n):
        arrival = df.loc[i, 'Arrival Time']
        burst = df.loc[i, 'Burst Time']

        # Ensure CPU Waits if process hasn't arrived
        if current_time < arrival:
            current_time = arrival
        
        # Compute completion time
        completion = current_time + burst
        df.loc[i, 'Completion Time'] = completion

        # Update current time
        current_time = completion

        # Compute turnaround time = completion time - arrival time
        turnaround = completion - arrival
        df.loc[i, 'Turnaround Time'] = turnaround

        # Compute waiting time = turnaround time - burst time
        waiting = turnaround - burst
        df.loc[i, 'Waiting Time'] = waiting

    # Display results
    print("\nFCFS Scheduling Results:")
    print(df)

    # Compute and display average metrics
    avg_turnaround = df['Turnaround Time'].mean()
    avg_waiting = df['Waiting Time'].mean()
    print(f"\nAverage Turnaround Time: {avg_turnaround:.2f}")
    print(f"Average Waiting Time: {avg_waiting:.2f}")

# Run the FCFS scheduler
fcfs()
        

    



    

