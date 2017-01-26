import redis


class Db(object):

    def __init__(self):
        self.r = redis.StrictRedis()

    def get_alarm_time(self):
        return self.r.get('ALARM_TIME_HOUR'), self.r.get('ALARM_TIME_MINUTE')

    def set_alarm_time(self, hour, minute):
        self.r.set('ALARM_TIME_HOUR', hour)
        self.r.set('ALARM_TIME_MINUTE', minute)

DB = Db()
