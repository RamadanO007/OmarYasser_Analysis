import time
import matplotlib.pyplot as plt
import random

# Merge Sort implementation
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Binary Search for pairs
def binary_search(arr, target):
    pairs = []
    for num in arr:
        complement = target - num
        low = 0
        high = len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == complement:
                pairs.append((num, complement))
                break
            elif arr[mid] < complement:
                low = mid + 1
            else:
                high = mid - 1
    return pairs

def find_pairs_with_sum(S, target):
    merge_sort(S) 
    return binary_search(S, target)

def measure_time(n_values):
    times = []
    for n in n_values:
        arr = [random.randint(1, 100) for _ in range(n)]  # Generating random array
        start_time = time.time()
        result = find_pairs_with_sum(arr, 100) 
        end_time = time.time()
        times.append(end_time - start_time)
    return times

def plot_graph(n_values, times):
    plt.plot(n_values, times, marker='o', linestyle='-', color='green')
    plt.xlabel('Size of n')
    plt.ylabel('Time (seconds)')
    plt.title('Algorithm Scalability')
    plt.grid(True)
    plt.show()

n_values = [10**i for i in range(7)]  # Powers of 10 from 1 to 10^6

execution_times = measure_time(n_values)

plot_graph(n_values, execution_times)
