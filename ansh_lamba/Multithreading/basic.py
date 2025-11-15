import time
from concurrent.futures import ThreadPoolExecutor

# A sample function to simulate some work
def task(name):
    print(f"Starting task {name}")
    time.sleep(2)  # simulate work
    print(f"Finished task {name}")
    return f"Result from {name}"

# Using ThreadPoolExecutor
def main():
    with ThreadPoolExecutor(max_workers=3) as executor:
        # Submit multiple tasks
        futures = [executor.submit(task, i) for i in range(5)]

        # Collect results as they complete
        for future in futures:
            print(future.result())

if __name__ == "__main__":
    main()
