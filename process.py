"""
process.py - Defines the Process data structure
Each process holds its input data and computed scheduling results
"""

class Process:
    def __init__(self, pid, arrival_time, burst_time, priority=0):
        # --- INPUT FIELDS (you provide these) ---
        self.pid = pid                      # Process ID (e.g., P1, P2)
        self.arrival_time = arrival_time    # When the process arrives in the ready queue
        self.burst_time = burst_time        # How long the process needs the CPU
        self.priority = priority            # Lower number = higher priority

        # --- OUTPUT FIELDS (calculated by the algorithm) ---
        self.completion_time = 0    # When the process finishes execution
        self.turnaround_time = 0    # CT - AT  (total time from arrival to finish)
        self.waiting_time = 0       # TAT - BT (time spent waiting, NOT executing)
        self.response_time = 0      # First time CPU is given - AT

        # For algorithms that need to track remaining burst time (Round Robin)
        self.remaining_time = burst_time

    def reset(self):
        """Reset computed values so the same process object can be reused across algorithms"""
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0
        self.response_time = 0
        self.remaining_time = self.burst_time

    def __repr__(self):
        return f"Process({self.pid}, AT={self.arrival_time}, BT={self.burst_time}, P={self.priority})"
