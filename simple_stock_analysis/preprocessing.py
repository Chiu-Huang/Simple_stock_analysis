returns = (historical/historical.iloc[0]).fillna(method='backfill')
daily_pct_change = np.log(returns.pct_change() + 1)
vols = daily_pct_change.std() * np.sqrt(252)
