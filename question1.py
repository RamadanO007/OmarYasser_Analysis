import matplotlib.pyplot as plt
import time

def power_i(x, n):
    result = 1
    for i in range(n):
        result *= x
    return result

def power_divid(x, n):
    if n == 0:
        return 1
    else:
        temp = power_divid(x, n // 2)
        if n % 2 == 0:
            return temp * temp
        else:
            return x * temp * temp

def measure_time(func, x, n, repetitions=1000):
    total_time = 0
    for _ in range(repetitions):
        start_time = time.time()
        func(x, n)
        end_time = time.time()
        total_time += (end_time - start_time) * 1e6  # Measuring in microseconds
    return total_time / repetitions

def main():
    n_values = [10**i for i in range(7)]  # Powers of 10 from 1 to 10^6
    iterations = 10  # Number of iterations to measure average time

    times_i = []
    times_divid = []

    for n in n_values:
        time_i = measure_time(power_i, 2, n, iterations)
        time_divid = measure_time(power_divid, 2, n, iterations)
        times_i.append(time_i)
        times_divid.append(time_divid)

    plt.figure(figsize=(10, 6))
    plt.plot(n_values, times_i, label='Iterative Power')
    plt.plot(n_values, times_divid, label='Divide and Conquer Power')
    plt.xlabel('Power Size (n)')
    plt.ylabel('Time (µs)')
    plt.xscale('log')
    plt.yscale('log')
    plt.title('Algorithm Scalability Comparison')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
