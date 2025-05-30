#gfhdthev
#Лабораторная работа 6
#Второе задание


from multiprocessing import Process, Lock

import time

main_file = 'second.txt'

def f(l, i):
    l.acquire()
    try:
        file = open(main_file, "a")
        file.write('fvgnuvirepvbureviowpdfvbdv;biorewv')
        file.write('vrerevrerevrevervre')
        file.write(' sfv n ntrbtrwsr;biorewv')
        file.write('798098634;biorewv')
        file.write('bsbvrebrtbn;biorewv')
        file.write('65467453264435646;biorewv')
    finally:
        l.release()

if __name__ == '__main__':
    start = time.time()
    lock = Lock()

    for num in range(7):
        Process(target=f, args=(lock, num)).start()

    mp_time = time.time() - start
    print(f"Многопроцессорное вычисление: {mp_time:.2f} сек")

