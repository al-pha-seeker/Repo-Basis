
def signal_irr_vs_gc(irr:float, gc_rate:float, threshold:float=0.0025):
    diff = irr - gc_rate
    if diff > threshold:
        return "ENTER_LONG_CASH_SHORT_FUT"
    elif diff < -threshold:
        return "ENTER_SHORT_CASH_LONG_FUT"
    return "FLAT"