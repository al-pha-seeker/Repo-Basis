import numpy as np

def backtest(signals, future_prices, gc_series, tick_cost=0.0001):
    pos = 0
    pnl = np.zeros(len(future_prices))
    for t in range(1, len(future_prices)):
        pnl[t] = pnl[t-1] + pos*(future_prices[t]-future_prices[t-1])
        s = signals[t]
        if s == "ENTER_LONG_CASH_SHORT_FUT" and pos != -1:
            pnl[t] -= tick_cost; pos = -1
        elif s == "ENTER_SHORT_CASH_LONG_FUT" and pos != 1:
            pnl[t] -= tick_cost; pos = 1
        elif s == "FLAT" and pos != 0:
            pnl[t] -= tick_cost; pos = 0
    return pnl, pos
