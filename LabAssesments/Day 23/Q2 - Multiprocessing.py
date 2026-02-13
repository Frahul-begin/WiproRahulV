import math
import time
from multiprocessing import Pool, cpu_count

numbers = [50000, 60000, 55000, 35000, 80000]

def compute_factorial(n):
    return math.factorial(n)

if __name__ == "__main__":

    # -------- Sequential Execution --------
    starttime1 = time.time()
    seq_results = []

    for num in numbers:
        result = compute_factorial(num)
        seq_results.append(result)
        print(f"Sequential: Factorial of {num} calculated")

    seqtime = time.time() - starttime1
    print(f"\nSequential calculation time: {seqtime:.2f} seconds")

    # -------- Multiprocessing Execution --------
    starttime2 = time.time()

    with Pool(cpu_count()) as pool:
        parallel_results = pool.map(compute_factorial, numbers)

    for num in numbers:
        print(f"Multiprocessing: Factorial of {num} calculated")

    paralleltime = time.time() - starttime2
    print(f"\nParallel calculation time: {paralleltime:.2f} seconds")
