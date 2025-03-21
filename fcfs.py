# First Come First Server
"""
TT = total time
CT = current time
BT = burst time

Process (arrival_time, burst_time, pid)
"""

import pandas as pd

def fcfs():
    print("Welcome to the FCFS scheduling program!")

    # Input validation for the number of processes
    while True:
        try:
            n = int(input("Enter the number of processes: "))
            if n <= 0:
                raise ValueError("Number of processes must be positive.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}")

    # Collect process information
    processes = []
    for i in range(n):
        print(f"\nProcess {i + 1}:")
        process_id = input("Enter Process ID: ")
        arrival_time = int(input("Enter Arrival Time: "))
        burst_time = int(input("Enter Burst Time(integer): "))
        processes.append((arrival_time, burst_time, process_id))

    # Convert to DataFrame and ensure numeric columns are properly typed
    df = pd.DataFrame(processes, columns=["Arrival Time", "Burst Time", "Process ID"])
    df["Arrival Time"] = pd.to_numeric(df["Arrival Time"])
    df["Burst Time"] = pd.to_numeric(df["Burst Time"])

    # Sort processes by arrival time
    df = df.sort_values(by="Arrival Time").reset_index(drop=True)

    # Initialize columns for completion, turnaround, and waiting times
    df['Completion Time'] = 0
    df['Turnaround Time'] = 0
    df['Waiting Time'] = 0

   # Calculate FCFS scheduling metrics
    current_time = 0
    for i in range(n):
        arrival = df.loc[i, "Arrival Time"]
        burst = df.loc[i, "Burst Time"]

        # Ensure CPU waits if process hasn't arrived
        if current_time < arrival:
            current_time = arrival

        # Compute completion time
        completion = current_time + burst
        df.loc[i, "Completion Time"] = completion

        # Update current time
        current_time = completion

        # Compute turnaround time = completion time - arrival time
        turnaround = completion - arrival
        df.loc[i, "Turnaround Time"] = turnaround

        # Compute waiting time = turnaround time - burst time
        waiting = turnaround - burst
        df.loc[i, "Waiting Time"] = waiting

    # Display results
    print("\nFCFS Scheduling Results:")
    print(df.to_string(index=False))  # More readable output without index

    # Compute and display average metrics
    avg_turnaround = df['Turnaround Time'].mean()
    avg_waiting = df['Waiting Time'].mean()
    print(f"\nAverage Turnaround Time: {avg_turnaround:.2f}")
    print(f"Average Waiting Time: {avg_waiting:.2f}")

# Run the FCFS scheduler
fcfs()
        

    



    

