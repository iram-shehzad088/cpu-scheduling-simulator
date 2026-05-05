"""
sjf.py - Shortest Job First Scheduling (Non-Preemptive)

HOW IT WORKS:
- At each scheduling decision point, pick the process with the SHORTEST burst time
  from all processes that have already arrived
- Non-preemptive: once a process starts, it runs to completion
- Optimal average waiting time BUT can cause starvation for long processes
"""

def sjf(processes):
    """
    Run SJF (non-preemptive) scheduling.
    Returns: gantt_chart (list of tuples)
    """
    procs = [p for p in processes]  # Work on a copy of references
    n = len(procs)
    completed = 0
    current_time = 0
    gantt_chart = []
    done = set()

    while completed < n:
        # Find all processes that have arrived and are not yet done
        available = [p for p in procs if p.arrival_time <= current_time and p.pid not in done]

        if not available:
            # CPU is idle — jump to the next arrival
            next_arrival = min(p.arrival_time for p in procs if p.pid not in done)
            gantt_chart.append(("IDLE", current_time, next_arrival))
            current_time = next_arrival
            continue

        # Pick the shortest burst time among available processes
        # Tie-break: earlier arrival time
        selected = min(available, key=lambda p: (p.burst_time, p.arrival_time))

        start_time = current_time
        selected.response_time = start_time - selected.arrival_time

        current_time += selected.burst_time
        selected.completion_time = current_time
        selected.turnaround_time = selected.completion_time - selected.arrival_time
        selected.waiting_time = selected.turnaround_time - selected.burst_time

        gantt_chart.append((selected.pid, start_time, selected.completion_time))
        done.add(selected.pid)
        completed += 1

    return gantt_chart
