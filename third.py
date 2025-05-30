#gfhdthev
#Лабораторная работа 6
#Третье задание


import asyncio
import random
import time


async def producer(queue, id):
    for i in range(3):
        item = f"Item: {id}-{i}"
        await queue.put(item)
        print(f"Producer {id} produced-> {item}")
        await asyncio.sleep(random.uniform(0.1, 0.5))

async def consumer(queue):
    while True:
        item = await queue.get()
        if item is None:
            break
        print(f"Consumer consumed {item}")
        queue.task_done()

async def asyncio_def():
    start = time.time()
    queue = asyncio.Queue(maxsize=10)
    producers = [asyncio.create_task(producer(queue, i)) for i in range(3)]
    consumer_task = asyncio.create_task(consumer(queue))
    await asyncio.gather(*producers)
    await queue.join()
    await queue.put(None)
    await consumer_task
    mp_time = time.time()-start
    print(f'Асинхронное выполнение: {mp_time}')

def async_queue():
    asyncio.run(asyncio_def())