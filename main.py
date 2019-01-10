import time
from threading import Timer


class IntervalBatcher:
    def __init__(self, interval):
        self.interval = interval
        self.q = []
        self.timer = Timer(self.interval, self.trigger)

    def trigger(self):
        self.flush()
        self.timer = Timer(self.interval, self.trigger)
        self.timer.start()


    def flush(self):
        # TODO: How could we make this behavior configurable?
        # TODO: I'd love for IntervalBatcher to be more flexible. Any ideas?
        print(self.q)
        self.q = []

    def start(self):
        self.timer.start()

    def stop(self):
        self.timer.cancel()
        self.trigger()

    def put(self, item):
        self.q.append(item)


class Logger:
    def __init__(self, interval):
        self.batcher = IntervalBatcher(interval)


    def start(self):
        self.batcher.start()

    def stop(self):
        self.batcher.stop()

    def write_log(self, message):
        self.batcher.put(message)


if __name__ == "__main__":
    logger = Logger(interval=1.0)

    logger.start()
    for i in range(10):
        logger.write_log(f"Message {i}")
        time.sleep(.25)

    logger.stop()
