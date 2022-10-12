from multiprocessing import Process
import os 
import time


def square_numbers():
  for i in range(100):
    i * i
    time.sleep(0.1)

if __name__ == "__main__":
processes = []
num_processes = os.cpu_count()

#create processes
for i in range(num_processes):
  p = Process(target=square_numbers)
  processes.append(p)
  
#start processing
for p in processes:
  p.start()
  
  
#join
for p in processes:
  p.join()
  

print('end main')


from threading import Thread

def square_numbers():
    for i in range(1000):
        result = i * i

        
if __name__ == "__main__":        
    threads = []
    num_threads = 10

    # create threads and asign a function for each thread
    for i in range(num_threads):
        thread = Thread(target=square_numbers)
        threads.append(thread)

    # start all threads
    for thread in threads:
        thread.start()

    # wait for all threads to finish
    # block the main thread until these threads are finished
    for thread in threads:
        thread.join()
