from threading import Thread
import time

def get_thread(thread_name):
    time.sleep(1)
    print(f"Thread № {thread_name} is started! ")
start_1 = time.time()
for i in range(5):
    get_thread(i + 1)
end_1 = time.time()
print(end_1 - start_1)

threads = [Thread(target=get_thread, args=(i + 1, )) for i in range(5)]
start_2 = time.time()
for t in threads:
    t.start()
for t in threads:
    t.join()
end_2 = time.time()
print(end_2 - start_2)