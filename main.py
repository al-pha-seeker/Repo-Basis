# main.py (optionnel, à mettre à la racine du projet)
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

base = Path("repo-basis")  # adapte si besoin
gc   = pd.read_csv(base/'data/gc_rate.csv', parse_dates=['date'])
fut  = pd.read_csv(base/'data/future_bund.csv', parse_dates=['date','expiry'])
bond = pd.read_csv(base/'data/bond_ctd.csv', parse_dates=['date','coupon_next_date'])

from importlib.machinery import SourceFileLoader
repo    = SourceFileLoader('repo', str(base/'src/repo.py')).load_module()
signals = SourceFileLoader('signals', str(base/'src/signals.py')).load_module()
bt      = SourceFileLoader('backtest', str(base/'src/backtest.py')).load_module()

df = gc.merge(fut, on='date').merge(bond, on='date')
df['days_to_expiry'] = (df['expiry'] - df['date']).dt.days.clip(lower=1)

df['IRR'] = [
    repo.implied_repo_rate(F=row.F, CF=row.CF, clean=row.clean, ai0=row.AI, ai_T=row.AI, days=int(row.days_to_expiry))
    for _, row in df.iterrows()
]
df['diff_IRR_GC'] = df['IRR'] - df['gc_on']
df['signal'] = [signals.signal_irr_vs_gc(i, g, 0.0025) for i, g in zip(df['IRR'], df['gc_on'])]

# backtest jouet
pnl, pos = bt.backtest(df['signal'].values, df['F'].values, df['gc_on'].values)
df['pnl'] = pnl

# plots simples
plt.figure()
plt.plot(df['date'], df['IRR'], label='IRR (simplified)')
plt.plot(df['date'], df['gc_on'], label='GC ON')
plt.title('IRR vs GC'); plt.legend(); plt.xlabel('date'); plt.ylabel('rate')
plt.show()

plt.figure()
plt.plot(df['date'], df['pnl'])
plt.title('Toy PnL (future only)'); plt.xlabel('date'); plt.ylabel('PnL (arb units)')
plt.show()

print(df[['date','F','clean','AI','gc_on','IRR','diff_IRR_GC','signal']].head(10))
