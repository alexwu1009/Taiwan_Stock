import pandas as pd
import requests
import io
import datetime
import time

def crawler(date_time):
    page_url = 'https://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date=' + date_time + '&type=ALLBUT0999'
    page = requests.get(page_url)
    use_text = page.text.splitlines()
    for i, text in enumerate(use_text):
        if text == '"證券代號","證券名稱","成交股數","成交筆數","成交金額","開盤價","最高價","最低價","收盤價","漲跌(+/-)","漲跌價差","最後揭示買價","最後揭示買量","最後揭示賣價","最後揭示賣量","本益比",':
            initial_point = i
            break
    df = pd.read_csv(io.StringIO(''.join([text[:-1] + '\n' for text in use_text[initial_point:]])))
    df['證券代號'] = df['證券代號'].apply(lambda x:x.replace('=', ''))
    df['證券代號'] = df['證券代號'].apply(lambda x:x.replace('"', ''))
    return df
def trans_date(date_time):
    return ''.join(str(date_time).split(' ')[0].split('-'))
def parse_n_days(start_date,n):
    df_dict = {}
    now_date = start_date
    for i in range(n):
        time.sleep(3)
        now_date = now_date - datetime.timedelta(days=1)
        try:
            df = crawler(trans_date(now_date))
            print("Current date" + ' ' +trans_date(now_date))
            df_dict.update({trans_date(now_date):df})
            print('Successful!!')
        except:
            print('Fails at'+ ' ' + trans_date(now_date))
    return df_dict 
    
    for key in result_dict.keys():
    result_dict[key].to_csv(str(key)+'.csv', index=False)
    print('SAVED')
