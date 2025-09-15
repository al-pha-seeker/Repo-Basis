
def accrued_interest(cpn_rate:float, freq:int, days_since_last:int, days_in_period:int, nominal:float=100.0) -> float:
    return nominal * (cpn_rate/freq) * (days_since_last/days_in_period)

def dirty_price(clean:float, ai:float) -> float:
    return clean + ai
