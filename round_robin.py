"""
round_robin.py - Round Robin Scheduling

HOW IT WORKS:
- Each process gets a fixed time slice called a "time quantum"
- If a process doesn't finish in its quantum, it goes back to the end of the ready queue
- Preemptive: processes are interrupted after their quantum expires
- Best for time-sharing systems — every process gets fair CPU time
- Response time is good, but overhead increases with many context switches
"""

from collections import deque

def round_robin(processes, quantum):
    """
    Run Round Robin scheduling with a given time quantum.
    Returns: gantt_chart (list of tuples)
    """
    # Sort by arrival time for initial queue building
    procs = sorted(processes, key=lambda p: p.arrival_time)
    n = len(procs)

    current_time = 0
    gantt_chart = []
    queue = deque()
    response_set = set()    # Track which processes have gotten CPU for the first time
    arrived = set()         # Track which processes have been added to queue
    completed = 0
    i = 0  # Index pointer into sorted procs list

    # Add all processes arriving at time 0
    while i < n and procs[i].arrival_time <= current_time:
        queue.append(procs[i])
        arrived.add(procs[i].pid)
        i += 1

    while completed < n:
        if not queue:
            # CPU idle — jump to next arrival
            next_proc = procs[i]
            gantt_chart.append(("IDLE", current_time, next_proc.arrival_time))
            current_time = next_proc.arrival_time
            queue.append(next_proc)
            arrived.add(next_proc.pid)
            i += 1
            continue

        p = queue.popleft()

        # Record first response time
        if p.pid not in response_set:
            p.response_time = current_time - p.arrival_time
            response_set.add(p.pid)

        # Run for min(remaining_time, quantum)
        exec_time = min(p.remaining_time, quantum)
        start_time = current_time
        current_time += exec_time
        p.remaining_time -= exec_time

        gantt_chart.append((p.pid, start_time, current_time))

        # Enqueue any new arrivals that came in during this execution
        while i < n and procs[i].arrival_time <= current_time:
            queue.append(procs[i])
            arrived.add(procs[i].pid)
            i += 1

        if p.remaining_time == 0:
            # Process finished
            p.completion_time = current_time
            p.turnaround_time = p.completion_time - p.arrival_time
            p.waiting_time = p.turnaround_time - p.burst_time
            completed += 1
        else:
            # Not finished — goes back to the end of the queue
            queue.append(p)

    return gantt_chart
