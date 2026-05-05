# 🖥️ CPU Scheduling Algorithm Simulator

**Course:** Operating Systems | North South University  
**Student:** Iram Shehzad | ID: 2131614642

---

## 📌 What is this?

A terminal-based Python simulator that demonstrates and compares four classic CPU scheduling algorithms used by Operating Systems to manage process execution.

---

## ⚙️ Algorithms Implemented

| Algorithm | Type | Key Property |
|-----------|------|-------------|
| FCFS | Non-Preemptive | Executes in order of arrival |
| SJF  | Non-Preemptive | Shortest burst runs first — optimal avg. WT |
| Priority Scheduling | Non-Preemptive | Lower priority number = higher priority |
| Round Robin | Preemptive | Each process gets a fixed time quantum |

---

## 📊 Metrics Calculated

For each process, the simulator computes:

- **CT** — Completion Time
- **TAT** — Turnaround Time = CT − Arrival Time
- **WT** — Waiting Time = TAT − Burst Time
- **RT** — Response Time = First CPU assignment − Arrival Time

---

## 📁 Project Structure

```
cpu_scheduler/
│
├── main.py          ← Entry point; interactive menu
├── process.py       ← Process data class
├── fcfs.py          ← First Come First Serve
├── sjf.py           ← Shortest Job First
├── priority.py      ← Priority Scheduling
├── round_robin.py   ← Round Robin
└── utils.py         ← Gantt chart, table display, input helpers
```

---

## 🚀 How to Run

**Requirements:** Python 3.7+, no external libraries needed.

```bash
git clone https://github.com/YOUR_USERNAME/cpu-scheduler-simulator
cd cpu-scheduler-simulator/cpu_scheduler
python main.py
```

---

## 🎮 How to Use

1. Run `python main.py`
2. Choose an algorithm from the menu (1–4), or choose **[5] Run ALL** to compare all algorithms on the same input
3. Either use the **built-in demo processes** (P1–P4) or **enter your own**
4. View the Gantt Chart, results table, and averages
5. In comparison mode, see which algorithm wins on waiting time

---

## 📸 Sample Output

```
  ╔══════════════════════════════════════════════════════════╗
  ║          CPU SCHEDULING ALGORITHM SIMULATOR              ║
  ║               Operating Systems — NSU                    ║
  ╚══════════════════════════════════════════════════════════╝

  FCFS Gantt Chart
  --------------------------------
  |  P1  |  P2  |  P3  |  P4  |
  0     8     12    21    26

  Process   Arrival   Burst   Completion  Turnaround  Waiting  Response
  P1        0         8       8           8           0        0
  P2        1         4       12          11          7        7
  ...

  📊 COMPARISON SUMMARY
  Algorithm         Avg WT    Avg TAT    Avg RT
  FCFS              8.75      15.25      8.75
  SJF               7.75      14.25      7.75
  Priority          7.75      14.25      7.75
  RR (Q=3)          13.50     20.00      3.00

  ✅ Best Average Waiting Time: SJF (7.75)
```

---

## 🔑 Key Concepts (for your understanding)

**Why does SJF have the best average waiting time?**  
SJF is mathematically proven to give the minimum average waiting time for a given set of non-preemptive processes. This is because it always prioritizes short tasks, reducing the total time everyone spends waiting.

**Why does Round Robin have the best response time?**  
Because every process gets CPU access quickly (within one quantum of arrival), so no one waits long to *start* — even if they wait longer to *finish*.

**What is the convoy effect in FCFS?**  
If a long process arrives first, all shorter processes queue behind it — even if they'd only need a fraction of the time. SJF fixes this.

---

## 📄 License

MIT — free to use and learn from.
