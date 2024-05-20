from multiprocessing import Process
import time

def my_function(name, t):
    print(f"Starting {name}")
    start_time = time.time()  
    time.sleep(t)  
    elapsed_time = time.time() - start_time
    print(f"Finished {name} after {elapsed_time:.5f} seconds")

if __name__ == "__main__":
    processes = []
    for name, t in [["Alice", 2], ["Bob", 2], ["Charlie", 2]]:
        process = Process(target=my_function, args=(name, t))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()
