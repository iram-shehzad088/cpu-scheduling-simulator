"""
main.py - CPU Scheduling Algorithm Simulator
=============================================
Course    : Operating Systems
Project   : CPU Scheduling Simulator
Student   : Iram Shehzad
ID        : 2131614642

Algorithms supported:
  1. FCFS  - First Come First Serve
  2. SJF   - Shortest Job First (Non-Preemptive)
  3. PS    - Priority Scheduling (Non-Preemptive)
  4. RR    - Round Robin

Metrics computed for each process:
  CT  - Completion Time
  TAT - Turnaround Time  (CT - AT)
  WT  - Waiting Time     (TAT - BT)
  RT  - Response Time    (First CPU time - AT)
"""

import sys
import copy

from process import Process
from fcfs import fcfs
from sjf import sjf
from priority import priority_scheduling
from round_robin import round_robin
from utils import (
    print_gantt_chart,
    print_results_table,
    print_averages,
    get_processes_input,
    reset_processes,
    print_separator,
)

BANNER = """
  ╔══════════════════════════════════════════════════════════╗
  ║          CPU SCHEDULING ALGORITHM SIMULATOR              ║
  ║               Operating Systems — NSU                    ║
  ╚══════════════════════════════════════════════════════════╝
"""

MENU = """
  Select an option:
  ─────────────────────────────────────────
  [1]  First Come First Serve (FCFS)
  [2]  Shortest Job First     (SJF)
  [3]  Priority Scheduling    (PS)
  [4]  Round Robin            (RR)
  [5]  Run ALL algorithms (same input)
  [6]  Exit
  ─────────────────────────────────────────
"""

# ─── Sample dataset for quick demo (you can also enter manually) ─────────────
DEMO_PROCESSES = [
    Process("P1", arrival_time=0, burst_time=8, priority=2),
    Process("P2", arrival_time=1, burst_time=4, priority=1),
    Process("P3", arrival_time=2, burst_time=9, priority=3),
    Process("P4", arrival_time=3, burst_time=5, priority=2),
]


def use_demo_or_input(ask_priority=False):
    """Ask whether to use demo data or enter manually."""
    print()
    print("  Would you like to:")
    print("  [1] Use demo processes (P1-P4, good for testing)")
    print("  [2] Enter your own processes")
    choice = input("\n  Your choice: ").strip()

    if choice == "1":
        # Deep copy so original DEMO_PROCESSES aren't modified
        procs = copy.deepcopy(DEMO_PROCESSES)
        print("\n  Using demo processes:")
        for p in procs:
            print(f"    {p.pid}  AT={p.arrival_time}  BT={p.burst_time}  Priority={p.priority}")
        return procs
    else:
        return get_processes_input(ask_priority=ask_priority)


def run_fcfs():
    print_separator()
    print("  [ FIRST COME FIRST SERVE — FCFS ]")
    processes = use_demo_or_input()
    gantt = fcfs(processes)
    print_separator("-")
    print_gantt_chart(gantt, "FCFS Gantt Chart")
    print_results_table(processes)
    print_averages(processes)


def run_sjf():
    print_separator()
    print("  [ SHORTEST JOB FIRST — SJF (Non-Preemptive) ]")
    processes = use_demo_or_input()
    gantt = sjf(processes)
    print_separator("-")
    print_gantt_chart(gantt, "SJF Gantt Chart")
    print_results_table(processes)
    print_averages(processes)


def run_priority():
    print_separator()
    print("  [ PRIORITY SCHEDULING (Non-Preemptive) ]")
    print("  Note: Lower number = Higher priority")
    processes = use_demo_or_input(ask_priority=True)
    gantt = priority_scheduling(processes)
    print_separator("-")
    print_gantt_chart(gantt, "Priority Scheduling Gantt Chart")
    print_results_table(processes, show_priority=True)
    print_averages(processes)


def run_rr():
    print_separator()
    print("  [ ROUND ROBIN — RR ]")
    processes = use_demo_or_input()

    while True:
        try:
            quantum = int(input("\n  Enter Time Quantum: "))
            if quantum <= 0:
                raise ValueError
            break
        except ValueError:
            print("  Time quantum must be a positive integer.")

    gantt = round_robin(processes, quantum)
    print_separator("-")
    print_gantt_chart(gantt, f"Round Robin Gantt Chart (Quantum={quantum})")
    print_results_table(processes)
    print_averages(processes)


def run_all():
    """Run all 4 algorithms on the same set of processes and compare results."""
    print_separator()
    print("  [ COMPARISON MODE — All Algorithms ]")
    print("  Note: Priority needed for PS; all algorithms get same processes.")
    processes = use_demo_or_input(ask_priority=True)

    while True:
        try:
            quantum = int(input("\n  Enter Time Quantum for Round Robin: "))
            if quantum <= 0:
                raise ValueError
            break
        except ValueError:
            print("  Time quantum must be a positive integer.")

    algorithms = [
        ("FCFS", fcfs, False),
        ("SJF",  sjf,  False),
        ("Priority", priority_scheduling, True),
    ]

    summary = []

    for name, algo, show_prio in algorithms:
        procs = copy.deepcopy(processes)
        gantt = algo(procs)
        print_separator("─")
        print(f"  ▶ {name}")
        print_gantt_chart(gantt, f"{name} Gantt Chart")
        print_results_table(procs, show_priority=show_prio)
        avg_wt = sum(p.waiting_time for p in procs) / len(procs)
        avg_tat = sum(p.turnaround_time for p in procs) / len(procs)
        avg_rt  = sum(p.response_time for p in procs) / len(procs)
        print_averages(procs)
        summary.append((name, avg_wt, avg_tat, avg_rt))

    # Round Robin
    procs = copy.deepcopy(processes)
    gantt = round_robin(procs, quantum)
    print_separator("─")
    print(f"  ▶ Round Robin (Q={quantum})")
    print_gantt_chart(gantt, f"RR Gantt Chart (Q={quantum})")
    print_results_table(procs)
    avg_wt = sum(p.waiting_time for p in procs) / len(procs)
    avg_tat = sum(p.turnaround_time for p in procs) / len(procs)
    avg_rt  = sum(p.response_time for p in procs) / len(procs)
    print_averages(procs)
    summary.append((f"RR (Q={quantum})", avg_wt, avg_tat, avg_rt))

    # ── Comparison Summary Table ──────────────────────────────────────────────
    print_separator()
    print("  📊 COMPARISON SUMMARY")
    print()
    col = 18
    print("  " + "Algorithm".ljust(col) + "Avg WT".ljust(col) + "Avg TAT".ljust(col) + "Avg RT".ljust(col))
    print("  " + "-" * (col * 4))
    for name, awt, atat, art in summary:
        print("  " + name.ljust(col) + f"{awt:.2f}".ljust(col) + f"{atat:.2f}".ljust(col) + f"{art:.2f}".ljust(col))
    print()

    # Best algorithm by WT
    best = min(summary, key=lambda x: x[1])
    print(f"  ✅ Best Average Waiting Time: {best[0]} ({best[1]:.2f})")
    print()


def main():
    print(BANNER)

    while True:
        print(MENU)
        choice = input("  Enter your choice: ").strip()

        if choice == "1":
            run_fcfs()
        elif choice == "2":
            run_sjf()
        elif choice == "3":
            run_priority()
        elif choice == "4":
            run_rr()
        elif choice == "5":
            run_all()
        elif choice == "6":
            print("\n  Goodbye! 👋\n")
            sys.exit(0)
        else:
            print("\n  ❌ Invalid choice. Please enter 1–6.")

        input("\n  Press Enter to return to menu...")


if __name__ == "__main__":
    main()
