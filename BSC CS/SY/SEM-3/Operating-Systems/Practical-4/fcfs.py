# Python3 program for implementation
# of FCFS scheduling

def findWaitingTime(processes, n,
                    bt, wt):
    wt[0] = 0

    for i in range(1, n):
        wt[i] = bt[i - 1] + wt[i - 1]


def findTurnAroundTime(processes, n, bt, wt, tat):

    for i in range(n):
        tat[i] = bt[i] + wt[i]


def findavgTime(processes, n, bt):

    wt = [0] * n
    tat = [0] * n
    total_wt = 0
    total_tat = 0

    findWaitingTime(processes, n, bt, wt)

    findTurnAroundTime(processes, n,
                       bt, wt, tat)

    print("Processes Burst time " +
          " Waiting time " +
          " Turn around time")

    for i in range(n):

        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]
        print(" " + str(i + 1) + "\t\t" +
              str(bt[i]) + "\t " +
              str(wt[i]) + "\t\t " +
              str(tat[i]))

    print("Average waiting time = " +
          str(total_wt / n))
    print("Average turn around time = " +
          str(total_tat / n))


if __name__ == "__main__":

    # process id's
    processes = [1, 2, 3, 4]
    print(len(processes))
    n = len(processes)

    # Burst time of all processes
    burst_time = [10, 5, 8, 5]

    findavgTime(processes, n, burst_time)
