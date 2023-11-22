
'''
asyncio stands for Asynchronous I/O or async for short, is 
programming pattern that allows for high performance I/O 
operations in a concurrent and non-blocking manner. In python,
async programming is achieved through the use of asyncio module
and asynchronous functions.

'''


#Example

import time
import asyncio


async def function1():
    await asyncio.sleep(1)
    print("func 1")


async def function2():
    await asyncio.sleep(1)
    print("func 2")


async def function3():
    await asyncio.sleep(4)
    print("func 3")

async def main():
    
    L = await asyncio.gather(
        function1(),
        function2(),
        function3(),
    )

    # task = asyncio.create_task(function1())

    # await function1()
    # await function2()
    # await function3()

asyncio.run(main())