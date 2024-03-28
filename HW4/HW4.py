"""
Задание №7
� Напишите программу на Python, которая будет находить
сумму элементов массива из 1000000 целых чисел.
� Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
� Массив должен быть заполнен случайными целыми числами
от 1 до 100.
� При решении задачи нужно использовать многопоточность,
многопроцессорность и асинхронность.
� В каждом решении нужно вывести время выполнения
вычислений.
"""

import random
import threading
import time
import multiprocessing
import asyncio

# def ar_sum():
#     summary = 0
#     for _ in range(1_000_000):
#         summary = summary + random.randint(1,100)
#     # print(summary)
#     return

#################Syncr######################
# start_syncr = time.time()
# for i in range(4):
#     ar_sum()
# print(f'Syncr {time.time() - start_syncr }')


#################Threads######################
# threads = []
#
#
# start_threads = time.time()
# for _ in range(4):
#     t = threading.Thread(target=ar_sum)
#     threads.append(t)
#     t.start()
#
# for t in threads:
#     t.join()
# print(f'Threads {time.time() - start_threads }')


#################Multiprocessing######################
# if __name__ == '__main__':
#
#     multiprocess = []
#
#     start_multiproc = time.time()
#     for _ in range(4):
#         p = multiprocessing.Process(target=ar_sum)
#         multiprocess.append(p)
#         p.start()
#
#     for p in multiprocess:
#         p.join()
#
#     print(f'Multiprocess {time.time() - start_multiproc }')

#################Async######################
async def ar_sum1():
    summary = 0
    for _ in range(1_000_000):
        summary = summary + random.randint(1,100)
    # print(summary)
    return

async def main():
    for _ in range(4):
        asyncio.create_task(ar_sum1())
if __name__ == '__main__':
    start_async = time.time()
    asyncio.run(main())
    print(time.time() - start_async)
