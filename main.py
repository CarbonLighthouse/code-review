import time


class Logger:
    def write_log(self, message):
        print(message)


if __name__ == "__main__":
    # execute only if run as a script
    logger = Logger()

    for i in range(10):
        logger.write_log(f"Message i")
        time.sleep(.5)
