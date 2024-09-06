import threading
import time

def print_numbers(thread_name):
    for i in range(5):
        time.sleep(1)
        print(f"{thread_name} prints {i}")

# Create threads
thread1 = threading.Thread(target=print_numbers, args=("Thread-1",))
thread2 = threading.Thread(target=print_numbers, args=("Thread-2",))

# Start threads
thread1.start()
thread2.start()

# Wait for both threads to complete
thread1.join()
thread2.join()

print("Both threads have finished execution.")

#----------------------------------------------------------------------------------------

import threading

lock = threading.Lock()

def safe_print_numbers(thread_name):
    with lock:
        for i in range(5):
            print(f"{thread_name} prints {i}")

thread1 = threading.Thread(target=safe_print_numbers, args=("Thread-1",))
thread2 = threading.Thread(target=safe_print_numbers, args=("Thread-2",))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Both threads have finished execution.")


#--------------------------------------------------------------------------------------

import threading

# Create an RLock
rlock = threading.RLock()

def nested_lock():
    with rlock:
        print("Acquired RLock")
        # Simulate a nested call that also requires the lock
        nested_function()

def nested_function():
    with rlock:
        print("Nested function acquired RLock")

# Create and start a thread
thread = threading.Thread(target=nested_lock)
thread.start()
thread.join()

print("Thread has finished execution.")

#------------------------------------------------------------------------------------

import threading
import time

# Create a Semaphore with a count of 2
semaphore = threading.Semaphore(2)

def worker(thread_name):
    print(f"{thread_name} is trying to acquire semaphore")
    with semaphore:
        print(f"{thread_name} has acquired semaphore")
        time.sleep(2)  # Simulate some work
        print(f"{thread_name} is releasing semaphore")

# Create and start multiple threads
threads = [threading.Thread(target=worker, args=(f"Thread-{i}",)) for i in range(5)]

for t in threads:
    t.start()

for t in threads:
    t.join()

print("All threads have finished execution.")


