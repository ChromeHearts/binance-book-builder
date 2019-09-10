#!/usr/bin/env python
from book import Book, Side

try:
    import ujson as json
except:
    import json
import asyncio
import websockets
import click
import os
import requests


async def run(ticker: str):
    hostname = "stream.binance.com"
    port = "9443"
    uri = "wss://" + hostname + ":" + port
    uri = os.path.join(uri, "ws", ticker.lower() + "@depth@100ms")
    book = Book(ticker)

    async with websockets.connect(uri) as websocket:
        snapshot_uri = "https://www.binance.com/api/v1/depth?symbol={T}&limit=1000".format(T=ticker.upper())
        snapshot = requests.get(url=snapshot_uri)
        sobj = json.loads(snapshot.content)

        for sstr, side in (('bids', Side.BID), ('asks', Side.ASK)):
            for prc, qty in sobj[sstr]:
                book.update_level(side, prc, qty)

        print(book.bbo())

        def update_book(data):
            for sstr, side in (('b', Side.BID), ('a', Side.ASK)):
                for prc, qty in data[sstr]:
                    book.update_level(side, prc, qty)

        while True:
            r = await websocket.recv()
            data = json.loads(r)
            if data['U'] > sobj['lastUpdateId'] or data['u'] > sobj['lastUpdateId']:
                update_book(data)
                break

        while True:
            r = await websocket.recv()
            data = json.loads(r)
            update_book(data)

            print(book.bbo())


@click.command("binance_build_book")
@click.option('-t', '--ticker', default="BTCUSDT", help="Ticker going to be display")
def main(ticker):
    asyncio.get_event_loop().run_until_complete(run(ticker))


if __name__ == "__main__":
    main()
