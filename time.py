def from_seconds(sec):
    min, sec = divmod(sec, 60)
    hrs, min = divmod(min, 60)
    days, hrs = divmod(hrs, 24)
    return days, hrs, min, sec


def to_seconds(days, hrs, min, sec, millisec=0):
    hrs = hrs + (days*24)
    min = min + (hrs*60)
    sec = sec + (min*60)
    seconds = sec + (millisec*1000)
    return seconds
