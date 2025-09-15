DAYCOUNT_BASE = 360

def year_fraction(days:int, base:int=DAYCOUNT_BASE) -> float:
    return days / base

def interest_simple(notional:float, rate:float, days:int, base:int=DAYCOUNT_BASE) -> float:
    return notional * rate * (days/base)
