import asyncio
import nest_asyncio
from tensoul import MajsoulPaipuDownloader
from tensoul.cfg import ms_cfg

nest_asyncio.apply()

APP_VERSION = "1.1.0"


async def connect_and_serve():
    downloader = MajsoulPaipuDownloader(True, APP_VERSION)
    await downloader.start()
    await downloader.login(ms_cfg['ms_username'],
                           ms_cfg['ms_password'],
                           ms_cfg['resource_version'],
                           ms_cfg['package_version'])
    downloader.start_server(ms_cfg['server_host'], ms_cfg['server_port'])


asyncio.run(connect_and_serve())
