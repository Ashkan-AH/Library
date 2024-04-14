from . import jalali
def jalali_converter(date):
    month_list = ["فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور", "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند"]
    persian_tuple = jalali.Gregorian(date.year, date.month, date.day).persian_tuple()
    return  f"{persian_tuple[2]} {month_list[persian_tuple[1]-1]} {persian_tuple[0]}"