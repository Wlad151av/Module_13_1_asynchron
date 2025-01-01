import time
import asyncio

async def start_strongman(nm,pow):
    print(f'Силач {nm} начал соревнования.')
    for i in range(1,6):
        await asyncio.sleep(6/pow)
        print(f'Силач {nm} поднял {i} шар' )
    print(f'Силач {nm} закончил соревнования.')

async def start_tournament():
    print('Start')
    task1 = asyncio.create_task(start_strongman('Pasha', 3))
    task2 = asyncio.create_task(start_strongman('Denis', 4))
    task3 = asyncio.create_task(start_strongman('Apollon', 5))
    await task1
    await task2
    await task3
    print('Finish')



start = time.time()
asyncio.run(start_tournament())
finish = time.time()

print(f'Working time = {round(finish-start, 2)} c')


