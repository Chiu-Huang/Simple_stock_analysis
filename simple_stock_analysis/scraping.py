cached_data={}
def stock_hist(symbol, start=None, end=None, cached_data=cached_data):
    '''Convenience function to get cached data '''
    if not symbol in cached_data:
        cached_data[symbol] = yf.download(symbol)
        print(F'Loaded {symbol} num values = {len(cached_data[symbol])}')
    return cached_data[symbol]
