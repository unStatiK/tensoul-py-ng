import asyncio
import ujson
import os
from argparse import ArgumentParser

from tensoul import MajsoulPaipuDownloader


async def download(username: str, password: str, record_uuid: str, resource_version: str, package_version: str):
    async with MajsoulPaipuDownloader() as downloader:
        await downloader.login(username, password, resource_version, package_version)
        return await downloader.download(record_uuid, resource_version=resource_version)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("record", help="Your record UUID for load.")
    parser.add_argument("-u", "--username", help="Your account name.", dest="username")
    parser.add_argument("-p", "--password", help="Your account password.", dest="password")

    args = parser.parse_args()
    resource_version = "0.16.290"
    package_version = "4.0.51"

    logs = asyncio.run(download(args.username, args.password, args.record, resource_version, package_version))

    os.makedirs("records", exist_ok=True)
    with open(f"records/{args.record}.json", "w", encoding="utf-8") as f:
        ujson.dump(logs, f, ensure_ascii=False)
        print(f"record created in path: records/{args.record}.json")
