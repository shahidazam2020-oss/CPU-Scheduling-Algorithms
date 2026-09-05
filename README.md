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

---
```

# 📊 Scheduling Metrics

The simulator calculates the following metrics:

Completion Time (CT)

The time at which a process finishes execution.

Turnaround Time (TAT)
TAT = CT - AT

Where:

CT = Completion Time
AT = Arrival Time
Waiting Time (WT)
WT = TAT - BT

Where:

TAT = Turnaround Time
BT = Burst Time

The assignment also specifies Response Time (RT) as a required scheduling metric.

---

# 🧪 Sample Input

The project uses the following test dataset:

| Process | Arrival Time | Burst Time | Priority |
|:-------:|-------------:|-----------:|---------:|
| P1 | 0 | 10 | 3 |
| P2 | 2 | 5 | 1 |
| P3 | 4 | 3 | 4 |
| P4 | 6 | 8 | 2 |
| P5 | 8 | 1 | 5 |

> **Priority Rule:** Lower priority number = higher priority.

🔄 Example Execution

The sample execution proceeds as follows:

Time 0 ──► P1 starts execution

Time 2 ──► P2 arrives
            P2 has higher priority
            P1 is preempted

Time 2-7 ─► P2 completes

Time 7-15 ─► P4 executes

Time 15-23 ─► P1 resumes and completes

Time 23-26 ─► P3 executes and completes

Time 26-27 ─► P5 executes and completes

The sample analysis shows that P2 preempts P1 because P2 has the highest priority among the available processes.

---

# 📈 Sample Results
| PID | AT | BT | Priority | CT | TAT | WT |
|:---:|---:|---:|:--------:|---:|----:|---:|
| P1  |  0 | 10 |    3     | 23 |  23 | 13 |
| P2  |  2 |  5 |    1     |  7 |   5 |  0 |
| P3  |  4 |  3 |    4     | 26 |  22 | 19 |
| P4  |  6 |  8 |    2     | 15 |   9 |  1 |
| P5  |  8 |  1 |    5     | 27 |  19 | 18 |

These values correspond to the sample analysis provided with the project.

---

# 💡 Key Observations

| # | Observation |
|:---:|:---|
| 1 | **P2** executes immediately after arrival because it has the highest priority. |
| 2 | **P1** is executed in two separate intervals because it is preempted by **P2**. |
| 3 | Processes with lower priority can experience longer waiting times. |
| 4 | Preemptive Priority Scheduling can lead to **starvation** for low-priority processes. |
| 5 | The scheduling results demonstrate the effect of process priority on CPU allocation. |

---
# 🛠️ Technologies Used

| Technology | Purpose |
|:---|:---|
| 🐍 **Python** | Algorithm implementation |
| 💻 **VS Code** | Development environment |
| 🖥️ **Terminal** | Program execution |
| 📚 **Operating Systems** | CPU scheduling concepts |
├── 📄 **Advanced CPU Scheduling Algorithms.docx** |
├── 🐍 python priority_preemptive.py |
├── 🐍 python3 priority_preemptive.py |
├── 🖼️ Capture-2.PNG |
└── 📖 README.md |

---
File Description

python priority_preemptive.py
Main Python implementation of the Preemptive Priority Scheduling algorithm.

python3 priority_preemptive.py
Python 3 version of the scheduling implementation.

Advanced CPU Scheduling Algorithms.docx
Contains the assignment requirements, sample dataset, execution analysis, results, and documentation.

Capture-2.PNG
Contains an example of the program execution/output.

# 🚀 Getting Started
## 1. Clone the Repository

Clone this repository to your local machine using Git.

## 2. Install Python

Make sure Python 3 is installed on your system.

Check your Python installation:

python --version

or:

python3 --version
## 3. Run the Program

Navigate to the project directory and run:

python "python priority_preemptive.py"

For Python 3:

python3 "python3 priority_preemptive.py"
# 🖥️ User Input

The program asks the user to enter:

Number of processes

Process 1
Arrival Time:
Burst Time:
Priority:

Process 2
Arrival Time:
Burst Time:
Priority:

The same process information is collected for all processes.

The program then generates a scheduling results table.

# 📋 Example Output

| PID | AT | BT | PR | CT | TAT | WT |
|:---:|---:|---:|---:|---:|---:|---:|
| 1 | 0 | 10 | 3 | 23 | 23 | 13 |
| 2 | 2 | 5 | 1 | 7 | 5 | 0 |
| 3 | 4 | 3 | 4 | 26 | 22 | 19 |
| 4 | 6 | 8 | 2 | 15 | 9 | 1 |
| 5 | 8 | 1 | 5 | 27 | 19 | 18 |

Average Waiting Time = 10.2
Average Turnaround Time = 15.6
🎯 Learning Objectives

This project provides practical understanding of:

CPU scheduling
Process management
Process arrival and execution
Preemption
Priority-based scheduling
Ready queue concepts
Scheduling performance metrics
Waiting and turnaround time
Operating system process management
⚠️ Limitations

The current implementation focuses specifically on Preemptive Priority Scheduling.

The implementation provided in this repository calculates:

Completion Time
Turnaround Time
Waiting Time
Average Waiting Time
Average Turnaround Time

The assignment specification additionally lists Response Time as a required metric, so RT can be added as a future enhancement.

🔮 Future Improvements

Possible improvements include:

 Add Response Time (RT)
 Generate automatic Gantt charts
 Add non-preemptive Priority Scheduling
 Add Round Robin Scheduling
 Add Shortest Job First (SJF)
 Add Shortest Remaining Time First (SRTF)
 Add Multilevel Feedback Queue (MLFQ)
 Create a graphical user interface
 Add automated test cases
 Export scheduling results to CSV
 Compare multiple scheduling algorithms
📚 Academic Context

Subject: Advanced Operating Systems
Topic: Priority Scheduling – Preemptive
Language: Python

The project was developed to demonstrate the implementation, execution, and analysis of a CPU scheduling algorithm. The assignment requires the source code to be publicly available and the repository to include clear documentation for setup, execution, and algorithm explanation.

👨‍💻 Author

Shahid Azam

Computer Science / IT

⭐ Project Highlights
⚙️ Algorithm        → Preemptive Priority Scheduling
🐍 Language         → Python
🎯 Priority Rule    → Lower number = Higher Priority
🔄 Scheduling       → Preemptive
📊 Metrics          → CT, TAT, WT
📈 Analysis         → Average WT & Average TAT
📚 Domain           → Operating Systems
⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

Built for learning, experimentation, and practical understanding of CPU scheduling algorithms.


### One important improvement

Your current repository looks good structurally, but the **README is the biggest missing piece**. Your assignment itself specifically requires a clear README with setup/run instructions, algorithm summary, and design choices. :contentReference[oaicite:7]{index=7}

I would also recommend adding a **Gantt Chart image** to the README. For this dataset, the sequence is:

**P1 → P2 → P4 → P1 → P3 → P5**

That would make the repository look significantly more complete and professi
