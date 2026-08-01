# Preemptive Priority Scheduling
# Given data set (Priority 1 = Highest)

processes = [
    {"pid": "P1", "arrival": 0, "burst": 10, "priority": 3},
    {"pid": "P2", "arrival": 2, "burst": 5,  "priority": 1},
    {"pid": "P3", "arrival": 4, "burst": 3,  "priority": 4},
    {"pid": "P4", "arrival": 6, "burst": 8,  "priority": 2},
    {"pid": "P5", "arrival": 8, "burst": 1,  "priority": 5},
]

n = len(processes)

remaining = [p["burst"] for p in processes]
completion = [0] * n
turnaround = [0] * n
waiting = [0] * n

time = 0
completed = 0

while completed < n:
    current = -1
    highest_priority = 10**9

    for i in range(n):
        if processes[i]["arrival"] <= time and remaining[i] > 0:
            if processes[i]["priority"] < highest_priority:
                highest_priority = processes[i]["priority"]
                current = i

    if current == -1:
        time += 1
    else:
        remaining[current] -= 1
        time += 1

        if remaining[current] == 0:
            completed += 1
            completion[current] = time
            turnaround[current] = completion[current] - processes[current]["arrival"]
            waiting[current] = turnaround[current] - processes[current]["burst"]

print("PID\tAT\tBT\tPR\tCT\tTAT\tWT")

total_wt = 0
total_tat = 0

for i in range(n):
    print(
        processes[i]["pid"], "\t",
        processes[i]["arrival"], "\t",
        processes[i]["burst"], "\t",
        processes[i]["priority"], "\t",
        completion[i], "\t",
        turnaround[i], "\t",
        waiting[i]
    )
    total_wt += waiting[i]
    total_tat += turnaround[i]

print("\nAverage Waiting Time =", total_wt / n)
print("Average Turnaround Time =", total_tat / n)
