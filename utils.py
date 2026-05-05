"""
utils.py - Display utilities for the CPU Scheduling Simulator

Contains:
- print_gantt_chart()   : Draws a visual Gantt chart in the terminal
- print_results_table() : Displays a formatted table of process metrics
- print_averages()      : Shows average CT, TAT, WT, RT
- get_processes_input() : Collects process data from the user interactively
"""

def print_gantt_chart(gantt_chart, title="Gantt Chart"):
    """
    Draws a text-based Gantt chart like this:
    | P1 | P2 | IDLE | P3 |
    0    4    9      12    17
    """
    print(f"\n  {title}")
    print("  " + "-" * (len(gantt_chart) * 8))

    # Top row: process boxes
    bar = "  |"
    for entry in gantt_chart:
        pid = str(entry[0])
        bar += f" {pid:^4} |"
    print(bar)

    # Bottom row: time markers
    timeline = "  "
    prev_end = None
    for entry in gantt_chart:
        pid, start, end = entry
        if prev_end is None:
            timeline += str(start).ljust(6)
        timeline += str(end).ljust(6)
        prev_end = end
    print(timeline)
    print()


def print_results_table(processes, show_priority=False):
    """
    Prints a formatted table of scheduling metrics.
    """
    col_w = 10

    # Header
    headers = ["Process", "Arrival", "Burst"]
    if show_priority:
        headers.append("Priority")
    headers += ["Completion", "Turnaround", "Waiting", "Response"]

    header_line = "  " + "".join(h.ljust(col_w) for h in headers)
    print(header_line)
    print("  " + "-" * len(header_line))

    # Rows
    sorted_procs = sorted(processes, key=lambda p: p.pid)
    for p in sorted_procs:
        row = [
            str(p.pid),
            str(p.arrival_time),
            str(p.burst_time),
        ]
        if show_priority:
            row.append(str(p.priority))
        row += [
            str(p.completion_time),
            str(p.turnaround_time),
            str(p.waiting_time),
            str(p.response_time),
        ]
        print("  " + "".join(v.ljust(col_w) for v in row))
    print()


def print_averages(processes):
    """
    Prints average TAT, WT, and RT.
    """
    n = len(processes)
    avg_tat = sum(p.turnaround_time for p in processes) / n
    avg_wt  = sum(p.waiting_time for p in processes) / n
    avg_rt  = sum(p.response_time for p in processes) / n

    print(f"  Average Turnaround Time : {avg_tat:.2f}")
    print(f"  Average Waiting Time    : {avg_wt:.2f}")
    print(f"  Average Response Time   : {avg_rt:.2f}")
    print()


def get_processes_input(ask_priority=False):
    """
    Interactively collects process input from the user.
    Returns a list of Process objects.
    """
    from process import Process

    print()
    while True:
        try:
            n = int(input("  Enter number of processes: "))
            if n <= 0:
                raise ValueError
            break
        except ValueError:
            print("  Please enter a positive integer.")

    processes = []
    print()
    for i in range(n):
        print(f"  --- Process P{i+1} ---")
        while True:
            try:
                at = int(input(f"    Arrival Time : "))
                bt = int(input(f"    Burst Time   : "))
                if at < 0 or bt <= 0:
                    raise ValueError
                break
            except ValueError:
                print("    Invalid input. Arrival >= 0, Burst > 0.")

        priority = 0
        if ask_priority:
            while True:
                try:
                    priority = int(input(f"    Priority     : "))
                    break
                except ValueError:
                    print("    Please enter an integer for priority.")

        processes.append(Process(f"P{i+1}", at, bt, priority))

    return processes


def reset_processes(processes):
    """Reset all process metrics so algorithms don't accumulate stale data."""
    for p in processes:
        p.reset()


def print_separator(char="=", width=65):
    print("\n  " + char * width + "\n")
