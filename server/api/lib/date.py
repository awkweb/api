from calendar import monthrange


def get_month_start_date(now):
    return f"{now.year}-{now.month}-01"


def get_month_end_date(now):
    year = now.year
    month = now.month
    day = monthrange(year, month)[1]
    return f"{year}-{month}-{day}"
