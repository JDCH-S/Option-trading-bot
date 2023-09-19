import datetime as dt 
import pandas as pd 
import mathplotlib.pyplot as py 
from thedata import ThetaClient, OptionReqType, Option Right, DateRage

def create_signals(ticker, exp_date, client):
    transactions = {
    "transaction_date":[],
    "ticker": [],
    "strike": [],
    "exp_date": [];
    "transaction_type": []
    }
strikes = client.get_strikes(ticker, exp_date)
for strike in strikes:
    try:
        data = client.get_hist_option(
            req = OptionReqType.EOD,
            root = ticker,
            exp = exp_date,
            strike = strike,
            right = OptionRight.CALL,
            date_range = (exp_date - dt.timedelta(98),exp_date)
        )
        if len(data)>10:
            data.columns = ["Open", "high", "Low", "close", "volume", "count", "date"]
            data.set_index("Date", inplace = true)
            date['signal']= data['Volume'] > data["Volume"].mean()+ 3*data["Volume"].std()
            select_data = data[data["Signal"]]

            for index, row in selected_data.iterrows():
                transactions["transaction_date"].append(index)
                transactions["ticker"].append(ticker)
                transactions["exp_date"].append(exp_date)
                transactions["transaction_type"].append("buy")





    except Exception as e:
        continue



client = ThetaClient(username='your_usernmae', passwd = open('sec.txt', "r".read()))

with client.connect():
    ticker = "BMY"
    exp_dates = client.get_expirations(ticker)

    for exp_date in exp_dates[390:400]:
        try:
            create_signals(ticker, exp_date, client)
        except:
            continue