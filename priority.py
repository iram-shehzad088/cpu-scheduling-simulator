"""
priority.py - Priority Scheduling (Non-Preemptive)

HOW IT WORKS:
- At each scheduling point, pick the process with the HIGHEST priority
  among all arrived processes
- Convention used: LOWER priority number = HIGHER priority (e.g., priority 1 runs before priority 3)
- Non-preemptive: once started, runs to completion
- Risk: Starvation — low-priority processes may never run if high-priority ones keep arriving
"""

def priority_scheduling(processes):
    """
    Run Priority Scheduling (non-preemptive).
    Returns: gantt_chart (list of tuples)
    """
    procs = [p for p in processes]
    n = len(procs)
    completed = 0
    current_time = 0
    gantt_chart = []
    done = set()

    while completed < n:
        # All arrived, not finished
        available = [p for p in procs if p.arrival_time <= current_time and p.pid not in done]

        if not available:
            next_arrival = min(p.arrival_time for p in procs if p.pid not in done)
            gantt_chart.append(("IDLE", current_time, next_arrival))
            current_time = next_arrival
            continue

        # Lower number = higher priority; tie-break by arrival time
        selected = min(available, key=lambda p: (p.priority, p.arrival_time))

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
