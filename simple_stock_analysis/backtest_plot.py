def diversicheck(symbols, start_day=0, time_horizon=365, **active):
    filtered = [symbol for symbol in symbols if active.get(symbol, True)]
    prices = pd.concat((stock_hist(symbol)['Adj Close'] for symbol in filtered), axis=1, keys=filtered).dropna(axis=0)
    
    
    start_dates = prices.index[0] + datetime.timedelta(days = start_day)
    end_dates = start_dates + datetime.timedelta(days=time_horizon)
    
    prices = prices.loc[start_dates:end_dates]
    
    unit_pos = prices / prices.iloc[0,:]
    basket = unit_pos.sum(axis=1) / unit_pos.shape[1]
    unit_pos.plot(figsize=(20,10),title='Stocks Cumulative Return over time', alpha=0.3)
    basket.plot(figsize=(20,10),legend = True)
    print(f'backtest from {start_dates} to {end_dates}')

prf_stocks = ['SPY','AAPL', 'TSLA', 'FB','IBM', 'GOOG']
active = dict(zip(prf_stocks, [True] * len(prf_stocks)))
_ = interact(diversicheck, symbols =fixed(prf_stocks), start_day=IntSlider(min=0,max=252*10),
             time_horizon=IntSlider(min=0,value=365,max=252*5),**active)
