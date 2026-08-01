n = int(input("Enter number of processes: "))

pid = []
arrival = []
burst = []
priority = []
remaining = []
completion = []
waiting = []
turnaround = []

for i in range(n):
    print("\nProcess", i + 1)
    pid.append(i + 1)
    arrival.append(int(input("Arrival Time: ")))
    burst.append(int(input("Burst Time: ")))
    priority.append(int(input("Priority (lower number = higher priority): ")))
    remaining.append(burst[i])
    completion.append(0)
    waiting.append(0)
    turnaround.append(0)

time = 0
completed = 0

while completed < n:
    current = -1
    highest_priority = 10**9

    for i in range(n):
        if arrival[i] <= time and remaining[i] > 0:
            if priority[i] < highest_priority:
                highest_priority = priority[i]
                current = i

    if current == -1:
        time += 1
    else:
        remaining[current] -= 1
        time += 1

        if remaining[current] == 0:
            completed += 1
            completion[current] = time
            turnaround[current] = completion[current] - arrival[current]
            waiting[current] = turnaround[current] - burst[current]

print("\nPID\tAT\tBT\tPR\tCT\tTAT\tWT")

total_wt = 0
total_tat = 0

for i in range(n):
    print(
        pid[i], "\t",
        arrival[i], "\t",
        burst[i], "\t",
        priority[i], "\t",
        completion[i], "\t",
        turnaround[i], "\t",
        waiting[i]
    )
    total_wt += waiting[i]
    total_tat += turnaround[i]

print("\nAverage Waiting Time =", total_wt / n)
print("Average Turnaround Time =", total_tat / n)
