import asyncio
import nest_asyncio
from tensoul import MajsoulPaipuDownloader
from tensoul.cfg import ms_cfg

nest_asyncio.apply()


async def connect_and_serve():
    downloader = MajsoulPaipuDownloader()
    await downloader.start()
    await downloader.login(ms_cfg['ms_username'], ms_cfg['ms_password'])
    downloader.start_server(ms_cfg['server_host'], ms_cfg['server_port'])


asyncio.run(connect_and_serve())
