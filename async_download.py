import asyncio
import aiohttp

@asyncio.coroutine
def load(url, sem):
    with (yield from sem):
        response = yield from aiohttp.request('GET', url)
        return (yield from response.read_and_close(decode=True))


@asyncio.coroutine
def get_page(page, sem):
    text = yield from load(page, sem)
    print("URL: {}, TEXT: {}".format(page, text[:20]))


def async_download(url_list):
    loop = asyncio.get_event_loop()
    sem = asyncio.Semaphore(10)
    requests = [get_page(page, sem) for page in url_list]
    f = asyncio.wait(requests)
    loop.run_until_complete(f)
