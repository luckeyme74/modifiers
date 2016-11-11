class Time(object):
    """represents the time of day in hours, minutes and seconds"""
t = Time()
t.second = 876543
t.minute = 0
t.hour = 0
t.day = 0

def int_to_time(t):
    t.minute, t.second = divmod(t.second, 60)
    t.hour, t.minute = divmod(t.minute, 60)
    t.day, t.hour = divmod(t.hour, 24)
    if t.second >= 60:
        t.second -= 60
        t.minute += 1

    if t.minute >= 60:
        t.minute -= 60
        t.hour += 1

    if t.hour >= 24:
        t.hour -= 24
        t.day +=1
    print '%.2d:%.2d:%.2d:%.2d' % (t.day, t.hour, t.minute, t.second)

int_to_time(t)
