import sys
import datetime

from db import DB
import alarm
from settings import logger


def main():
    hour, minute = DB.get_alarm_time()

    logger.debug("Checking time")
    now = datetime.datetime.now()
    logger.debug("Alarm time: {}".format((hour, minute)))
    logger.debug("Now time: {}".format((now.hour, now.minute)))

    if not (int(hour) == int(now.hour) and int(minute) == int(now.minute)):
        return True

    return alarm.execute_alarm()


if __name__ == "__main__":
    sys.exit(main())
