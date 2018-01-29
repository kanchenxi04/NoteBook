import json
class OrdBookBuck(object):
    def __init__(self, px, vol):
        self.px = px
        # self.px_str = px
        self.vol = vol
        # self.vol_str = vol

    def __str__(self):
        return ( str(self.px) + "\t" + str(self.vol))

class OrderBook(object):

    def __init__(self, jsonstr, level = 5):
        ordBook = json.loads(jsonstr)
        self.level = level
        self.ask = self.bookList( ordBook["asks"], 'ask' )
        self.bid = self.bookList( ordBook["bids"], 'bid' )


    def bookList(self, book, type):
        res = []
        for i in range(self.level):
            px = book[i][0]
            vol = book[i][1]
            res.append( OrdBookBuck(px, vol))
        if type == 'ask':
            res.reverse()
        return res

    def __str__(self):
        strres = "OrderBook:\n"
        for i in range(self.level):
            strres +=  ("\task " + str(self.level - i ) + "\t"  + str(self.ask[-(i+1)]) + "\n")
        strres += "\n"
        for i in range(self.level):
            strres += ("\tbid " + str(i+1) + "\t" + str(self.bid[i]) + "\n")
        return strres

if __name__ == "__main__":
    import marketdata
    ob = OrderBook( marketdata.getPxLoc() )
    print(ob)
