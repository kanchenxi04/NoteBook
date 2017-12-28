import redis
import util


def run():
    r = util.getRedConn()
    p = r.pubsub()
    p.psubscribe("marketdata:USD*")
    while True:
        msg = p.get_message(timeout=5)
        if msg is None: continue
        if msg['data'] == "cmd:quit":
            break
        print(msg)


if __name__ == "__main__":
    run()
    
###############
#producer.py
import redis
import util

def run():
    r = util.getRedConn()

    pub_channel = "marketdata:USDT"
    pub_channel2 = "marketdata:USDCNY"

    for i in range(5):
        msg = r.publish(pub_channel, 1.5)
        print(msg)
        msg = r.publish(pub_channel2, 2.5)
        print(msg)
    r.publish(pub_channel, "cmd:quit")


if __name__ == "__main__":
    run()
##############
#util.py
import redis

def getRedConn():
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    return r
