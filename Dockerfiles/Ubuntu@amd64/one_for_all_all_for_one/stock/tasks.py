from stock.celery import app

import pandas as pd
from datetime import datetime


def get_url(stock_id, year = datetime.today().year, month = datetime.today().month):
    return 'http://www.twse.com.tw/ch/trading/exchange/STOCK_DAY/genpage/Report{year}{month:02}/{year}{month:02}_F3_1_8_{stock_id}.php?STK_NO={stock_id}&myear={year}&mmon={month:02}'.format(stock_id = stock_id, year = year, month = month)


@app.task
def get_table(stock_id, year = datetime.today().year, month = datetime.today().month):
    
    url = get_url(stock_id, year, month) 
    targetTableIndex = 0
    
    table = pd.read_html(url,
                         attrs = {'border': '0' , 
                                  'width': '598', 
                                  'align': 'center', 
                                  'cellpadding': '0', 
                                  'cellspacing': '1', 
                                  'class': 'board_trad'},
                         header = 1
                        )[targetTableIndex]
    
    table['個股代號'] = stock_id
    table = table.reindex(columns = ['個股代號', '日期', '成交股數', '成交金額', '開盤價', '最高價', '最低價', '收盤價', '漲跌價差', '成交筆數'])
    
    return table.tail(1).values