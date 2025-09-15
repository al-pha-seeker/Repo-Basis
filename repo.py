
def implied_repo_rate(F:float, CF:float, clean:float, ai0:float, ai_T:float, days:int, base:int=360) -> float:
    num = F*CF + ai_T - (clean + ai0)
    den = (clean + ai0)
    return (num/den) * (base/days)

def implied_repo_rate_with_coupon(F:float, CF:float, clean:float, ai0:float, ai_T:float, days:int, coupon:float=0.0, reinvest_rate:float=0.0, base:int=360) -> float:
    coupon_effect = coupon * (1 + reinvest_rate * (days/base))
    num = F*CF + ai_T + coupon_effect - (clean + ai0)
    den = (clean + ai0)
    return (num/den) * (base/days)
