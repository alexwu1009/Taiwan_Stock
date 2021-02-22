import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn; seaborn.set()

stockNo = '2330.TW'
start_date = '2020-01-01'
df = yf.download(stockNo, start=start_date)
df = df.reset_index()

print('=================== First Observation ===================')

aveng_close = df['Close'].mean() # 觀測平均值
plt.figure(figsize=(15, 5))
plt.plot(df['Date'], df['Close'], label='TW')
plt.axhline(y = aveng_close, color='r', ls='--', alpha=0.5, label='aveng_close') #製作平均值虛線
plt.title('TW Stock', fontsize=20, color='g')
plt.xlabel('DATE', fontsize=15, color='g')
plt.ylabel('CLOSE', fontsize=15, color='g')
plt.legend(facecolor='white', fontsize=20)
plt.show()

print('=================== Second Observation ===================')

df2 = df.tail(9) # 為了製作近期2月圖示，抓取後9個
df2 = df2.set_index('Date') #index設定為Date
aveng_close = df2['Close'].mean()
plt.figure(figsize=(15, 5))
plt.plot(df2['Close'], label='2330.TW')
plt.axhline(y = aveng_close, color='r', ls='--', alpha=0.5, label='aveng_close')
plt.fill_between(df2.index, aveng_close, df2['Close'],
                 where=df2['Close'] >= aveng_close, color='gray',
                 alpha=0.5, interpolate=True)  #填補顏色強調成長趨勢 
#增添箭頭及註釋文字
date_0222 = df2.index[-1] #以日期為X
plt.annotate(
    'Keep going down',
    xy=(date_0222, 650),
    xycoords='data',
    xytext=(date_0222, 660),
    textcoords='data',
    horizontalalignment='center',
    arrowprops=dict(facecolor='r', arrowstyle='fancy')
)

plt.title('TW Stock', fontsize=20, color='g')
plt.xlabel('DATE', fontsize=15, color='g')
plt.ylabel('CLOSE', fontsize=15, color='g')
plt.legend(facecolor='white', fontsize=20)
plt.show()

# from the message, the 2330 is going down in the future. 
