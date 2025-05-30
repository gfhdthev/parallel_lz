#gfhdthev
#Лабораторная работа 6
#Первое задание


import threading
import time
import os

path = "random_txt_files"
files = os.listdir(path)

def find(word='error'):
    list = []
    for one_file in files:
        with open(f'random_txt_files/{one_file}', "r") as file:
            content = file.read()
        if word in content:
            list.append(one_file)
    print(list)
    time.sleep(1)
    return list

# Синхронная запись
start = time.time()
find('error')
sync_time = time.time() - start
print(f"Синхронное: {sync_time:.2f} сек")


# Многопоточная запись
start = time.time()
threads = []
for i in range(10):
    t = threading.Thread(target=find)
    t.start()
    threads.append(t)
for t in threads:
    t.join()
thread_time = time.time() - start
print(f"Многопоточное: {thread_time:.2f} сек")

