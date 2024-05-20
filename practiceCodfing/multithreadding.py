from threading import Thread
import time

def my_function(name):
    print(f"Starting {name}")
    start_time = time.time()  
    time.sleep(2)  
    print(f"Finished {name} after {time.time() - start_time:.5f} seconds")

if __name__ == "__main__":
    threads = []
    for name in ["Alice", "Bob", "Charlie"]:
        thread = Thread(target=my_function, args=(name,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
