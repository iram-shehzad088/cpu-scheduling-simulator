"""
fcfs.py - First Come First Serve Scheduling

HOW IT WORKS:
- Processes are executed in order of arrival time
- Non-preemptive: once a process starts, it runs until completion
- Simplest algorithm but can cause "convoy effect" (short processes wait for long ones)
"""

def fcfs(processes):
    """
    Run FCFS scheduling on a list of Process objects.
    Returns: gantt_chart (list of tuples) - [(pid, start, end), ...]
    """
    # Sort by arrival time
    procs = sorted(processes, key=lambda p: p.arrival_time)

    current_time = 0
    gantt_chart = []

    for p in procs:
        # If CPU is idle, jump to when process arrives
        if current_time < p.arrival_time:
            gantt_chart.append(("IDLE", current_time, p.arrival_time))
            current_time = p.arrival_time

        start_time = current_time
        p.response_time = start_time - p.arrival_time   # First response

        current_time += p.burst_time                     # Run to completion
        p.completion_time = current_time

        # TAT = CT - AT,  WT = TAT - BT
        p.turnaround_time = p.completion_time - p.arrival_time
        p.waiting_time = p.turnaround_time - p.burst_time

        gantt_chart.append((p.pid, start_time, p.completion_time))

    return gantt_chart
