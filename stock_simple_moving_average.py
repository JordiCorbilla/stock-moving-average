# Copyright 2020 Jordi Corbilla. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
import os
import secrets
import pandas as pd
from datetime import datetime
import yfinance as yf
import matplotlib.pyplot as plt


def PlotSimpleMovingAverage(ticker, start_date, project_folder):
    end_date = datetime.today()
    sec = yf.Ticker(ticker)
    print('End Date: ' + end_date.strftime("%Y-%m-%d"))

    # only download close price
    data = yf.download([ticker], start=start_date, end=end_date)[['Close']]
    data = data.reset_index()
    data.to_csv(os.path.join(project_folder, 'downloaded_data_' + ticker + '.csv'))
    data = data.set_index('Date')

    # define the average close price per day
    data['average_close_price'] = data.mean(axis=1)

    # visualize the first 5 columns
    print(data.head())

    # the simple moving average over a period of 90 days
    data['SMA_90'] = data.average_close_price.rolling(90, min_periods=1).mean()

    # the simple moving average over a period of 180 days
    data['SMA_180'] = data.average_close_price.rolling(180, min_periods=1).mean()

    plt.figure(figsize=(12, 5))
    plt.plot(data.Close, color='green')
    plt.plot(data.SMA_90, color='red')
    plt.plot(data.SMA_180, color='blue')
    plt.ylabel('Price [' + sec.info['currency'] + ']')
    plt.xlabel("Date")
    plt.title(sec.info['shortName'])
    plt.legend(["["+STOCK_TICKER+"] Close Price", "SMA 90 days", "SMA 180 days"])
    plt.savefig(os.path.join(project_folder, sec.info['shortName'].strip().replace('.', '') + '_price.png'))
    plt.show()


if __name__ == '__main__':
    STOCK_TICKER = 'GOOG'
    STOCK_START_DATE = pd.to_datetime('2004-08-01')
    TODAY_RUN = datetime.today().strftime("%Y%m%d")
    TOKEN = STOCK_TICKER + '_' + TODAY_RUN + '_' + secrets.token_hex(16)
    print('Ticker: ' + STOCK_TICKER)
    print('Start Date: ' + STOCK_START_DATE.strftime("%Y-%m-%d"))
    print('Test Run Folder: ' + TOKEN)

    # create project run folder
    PROJECT_FOLDER = os.path.join(os.getcwd(), TOKEN)
    if not os.path.exists(PROJECT_FOLDER):
        os.makedirs(PROJECT_FOLDER)

    PlotSimpleMovingAverage(STOCK_TICKER, STOCK_START_DATE, PROJECT_FOLDER)
