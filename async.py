import time
import asyncio

# The code below prints text, waits 2 sec and then do it again - 5 times in total

# def fetch_data():
#     print("Fetching data..")
#     time.sleep(2)
#
# for i in range(5):
#     fetch_data()

# The code below does same thing but do it in asynchronized way (simultaneously)

async def fetch_data_async():
    print("Fetching data..")
    await asyncio.sleep(2)

# creates async loop
loop = asyncio.new_event_loop()

# create a list of tasks and put the loop in it. Run it 5 times at the same time - without waiting
tasks = [
    loop.create_task(fetch_data_async()),
    loop.create_task(fetch_data_async()),
    loop.create_task(fetch_data_async()),
    loop.create_task(fetch_data_async()),
    loop.create_task(fetch_data_async()),
]

# run the loop and close it once finished
loop.run_until_complete(asyncio.wait(tasks))
loop.close()