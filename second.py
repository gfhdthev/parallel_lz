#gfhdthev
#Лабораторная работа 6
#Второе задание


from multiprocessing import Process, Lock
import time

main_file = 'second.txt'
words = [
    'fvgnuvirepvbureviowpdfvbdv;biorewv',
    'vrerevrerevrevervre',
    'sfv n ntrbtrwsr;biorewv',
    '798098634;biorewv',
    'bsbvrebrtbn;biorewv',
    '65467453264435646;biorewv'
]

def write_word(lock, word):
    lock.acquire()
    try:
        with open(main_file, "a") as file:
            file.write(word + "\n")
    finally:
        lock.release()

def multi_processing():
    start = time.time()
    lock = Lock()
    processes = []

    for word in words:
        proc = Process(target=write_word, args=(lock, word))
        proc.start()
        processes.append(proc)

    for proc in processes:
        proc.join()

    mp_time = time.time() - start
    print(f"Многопроцессорное вычисление: {mp_time:.2f} сек")
