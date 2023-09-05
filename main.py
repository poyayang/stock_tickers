import yfinance as yf
from datetime import datetime
import pandas as pd





def data_history(): 
    company=['NVDA', 'AAPL', 'TSLA', 'GOOGL']
    tickers=yf.Tickers(company)
    end_date=datetime.now().strftime('%Y-%m-%d')
    company_hist=tickers.history(period='max', start='2023-08-01', end=end_date, interval='1h')
    reframe_hist=company_hist.stack(level=1).rename_axis(['Date', 'Ticker']).reset_index(level=1)

    print(reframe_hist)



def company_institutional_holders(): 
    holders_data={}
    company=input("Enter company stock code: ").split() # split() works for both singular and multiple codes
    for holders in company: 
        ticker=yf.Ticker(holders)
        holders_data[holders]=ticker.get_institutional_holders()

    for holders, holders_df in holders_data.items():
        print(f'Institutional Holders for {holders}: \n')
        print(holders_df)
        print('='*100)


def cash_flow_history():
    holders_cashflow={}
    company=input("Enter company stock code: ").split() # split() works for both singular and multiple codes
    for cashflow in company: 
        ticker=yf.Ticker(cashflow)
        holders_cashflow[cashflow]=ticker.get_cash_flow()

    for cashflow, cashflow_df in holders_cashflow.items(): 
        print(f'Cashflow history for {cashflow}:\n')
        print(cashflow_df)
        print('///'*50)


def options_chain(): 
    company=input('Enter the company stock code:')
    ticker=yf.Ticker(company)
    options=ticker.option_chain()
    option_puts=options.puts
    option_calls=options.calls
    print("Put Options:")
    print(option_puts)
    print("=" * 50)
    print("Call Options:")
    print(option_calls)



company_institutional_holders()