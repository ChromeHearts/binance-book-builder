### Binance Book Builder

Experimental project to collect binance's depth of book data

### Install

`pip3 install -r requirements.txt`

### Run

```
python3 main.py --ticker [BTCUSDT]

initial bid & ask
((Decimal('10063.67000000'), '0.09873400'), (Decimal('10064.66000000'), '0.01956800'))
RecvTime DelayFromBinance BID BID_QTY ASK ASK_QTY
1568157667615 102.8369140625 ((Decimal('10063.67000000'), '0.09873400'), (Decimal('10064.66000000'), '0.01831800'))
1568157667715 102.5087890625 ((Decimal('10063.67000000'), '0.09873400'), (Decimal('10064.66000000'), '0.01831800'))
1568157667815 102.688720703125 ((Decimal('10063.67000000'), '0.09873400'), (Decimal('10064.66000000'), '0.01831800'))
...
```
- first line will be the initial BBO
- then each line are latest data
- updates are 100ms which is the highest frequency Binance provide currently
