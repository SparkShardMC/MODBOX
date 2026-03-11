from datetime import datetime, timedelta

def current_utc_time():
    """
    Return current UTC time.
    """
    return datetime.utcnow()

def add_minutes_to_now(minutes):
    """
    Return UTC time X minutes from now.
    """
    return datetime.utcnow() + timedelta(minutes=minutes)

def format_datetime(dt, fmt="%Y-%m-%d %H:%M:%S"):
    """
    Format a datetime object into a string.
    """
    return dt.strftime(fmt)
