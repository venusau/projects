def leastInterval(tasks, n):
    # Step 1: Count the frequency of each task
    task_freq = {}
    for task in tasks:
        if task in task_freq:
            task_freq[task] += 1
        else:
            task_freq[task] = 1
    
    # Step 2: Find the task with the maximum frequency
    max_freq = 0
    for freq in task_freq.values():
        max_freq = max(max_freq, freq)
    
    # Step 3: Calculate the number of tasks with maximum frequency
    max_freq_tasks = 0
    for freq in task_freq.values():
        if freq == max_freq:
            max_freq_tasks += 1
    
    # Step 4: Calculate the total intervals needed
    total_intervals = (max_freq - 1) * (n + 1) + max_freq_tasks
    
    # Return the maximum of total_intervals and the length of tasks list
    return max(total_intervals, len(tasks))

# Example usage:
tasks1 = ["A","A","A","B","B","B"]
n1 = 2
print(leastInterval(tasks1, n1))  # Output: 8

tasks2 = ["A","C","A","B","D","B"]
n2 = 1
print(leastInterval(tasks2, n2))  # Output: 6

tasks3 = ["A","A","A","B","B","B"]
n3 = 3
print(leastInterval(tasks3, n3))  # Output: 10
