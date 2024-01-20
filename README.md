# tensoul-py-ng

Convert MahjongSoul log into tenhou.net/6 format. (Inspired by https://github.com/Equim-chan/tensoul)

Fork from https://github.com/ssttkkl/tensoul-py

This version has many patches for integration with pantheon system (https://github.com/MahjongPantheon/pantheon).

Tensoul format is backward compatibility with original tenhou.net/6 format.

## Usage

You need to have an account from CN server, because only accounts from CN server has the ability to login with username and password.

```python
from tensoul import MajsoulPaipuDownloader

host = "127.0.0.1"
port = 8080
username = "foo@bar.com"
password = "foobar"
record_uuid = "123456-abcdefgh-1234-abcd-1234-12345678abcd"  # taken from majsoul log link: https://game.maj-soul.com/1/?paipu=<this_part>_a12345678

downloader = MajsoulPaipuDownloader()
await downloader.start()
await downloader.login(username, password)
downloader.start_server(host, port)
```

See example.py also

## Thanks

https://github.com/MahjongRepository/mahjong_soul_api

https://github.com/ssttkkl/tensoul-py

https://repo.riichi.moe/library.html#resources-majplus
