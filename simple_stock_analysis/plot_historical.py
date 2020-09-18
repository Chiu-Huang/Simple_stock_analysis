import matplotlib.pyplot as plt
plt.figure(figsize=(20,10))
lines = plt.plot(returns.drop('PORTFOLIO', axis=1), alpha=0.1)
plt.ylim((0,8))
plt.title('Portfolio Cumulative Return Over Time')
plt.plot(returns['PORTFOLIO'], alpha=1)
plt.legend(returns.columns)
plt.show()
