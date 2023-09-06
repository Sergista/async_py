from time import time
import asyncio
import aiohttp
from datetime import datetime


async def fetch_content(url, session: aiohttp.ClientSession):  # get post put patch
    async with session.get(url, allow_redirects=True) as response:
        data = await response.read()
        write_image(data)


def write_image(data):
    filename = f"file-{datetime.now()}.jpeg"
    with open(filename, 'wb') as f:
        f.write(data)


async def main():
    t0 = time()  # запустили счетчик

    url = 'https://loremflickr.com/320/240'
    tasks = []  # collections.deque

    async with aiohttp.ClientSession() as session:
        for i in range(10):
            task = asyncio.create_task(fetch_content(url, session))
            tasks.append(task)

        await asyncio.gather(*tasks)

    print(time() - t0)


if __name__ == '__main__':
    asyncio.run(main())