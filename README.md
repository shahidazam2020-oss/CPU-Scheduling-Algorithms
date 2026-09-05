# ⚙️ CPU Scheduling Algorithms

### Preemptive Priority Scheduling Simulator

A Python-based implementation and analysis of the **Preemptive Priority CPU Scheduling Algorithm** developed as part of an Advanced Operating Systems activity.

This project demonstrates how operating systems manage processes according to priority, including process arrival, CPU burst time, preemption, completion time, turnaround time, and waiting time.

---

## 📌 Project Overview

CPU scheduling is a fundamental concept in operating systems that determines how processes are selected and executed by the CPU.

This project implements **Preemptive Priority Scheduling**, where the CPU always selects the available process with the highest priority. In this implementation, **a lower priority number represents a higher priority**.

When a new process arrives with a higher priority than the currently running process, the current process is **preempted** and the higher-priority process receives the CPU.

The implementation also calculates important scheduling performance metrics for each process.

---

## ✨ Key Features

- ⚙️ Preemptive Priority Scheduling
- 🔄 Dynamic process preemption
- 📥 User-defined process input
- 🕒 Arrival Time handling
- ⏱️ Burst Time calculation
- 🎯 Priority-based process selection
- 📊 Completion Time calculation
- 🔁 Turnaround Time calculation
- ⏳ Waiting Time calculation
- 📈 Average Waiting Time
- 📈 Average Turnaround Time
- 🖥️ Tabular console output
- 🐍 Implemented in Python
- 📚 Includes sample data and analysis

---

## 🧠 Scheduling Algorithm

### Preemptive Priority Scheduling

The algorithm continuously checks all processes that have arrived and have remaining execution time.

The process with the **lowest priority number** is selected because lower numbers represent higher priority.

### Execution Logic

```text
Start
  │
  ▼
Read process information
  │
  ▼
Check arrived processes
  │
  ▼
Select highest-priority process
  │
  ▼
Execute for one time unit
  │
  ▼
Has a higher-priority process arrived?
  │
  ├── Yes ──► Preempt current process
  │
  └── No
        │
        ▼
Process completed?
  │
  ├── No ──► Continue execution
  │
  └── Yes
        │
        ▼
Calculate CT, TAT and WT
        │
        ▼
All processes completed?
  │
  ├── No ──► Continue
  │
  └── Yes
        │
        ▼
Display results
        │
        ▼
       End
