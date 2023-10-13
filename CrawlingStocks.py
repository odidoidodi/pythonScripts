import re
import urllib.request

nasdaq_symbols = ["AAPL", "GOOGL", "META", "TSLA", "NVDA", "PYPL", "INTC", "CSCO",
                  "CMCSA", "PEP", "ADBE", "AVGO", "TXN", "COST", "NFLX", "TMUS", "CHTR", "SBUX",
                  "AMGN", "QCOM", "MELI", "ATVI", "AMD", "GILD", "FISV", "BKNG", "ADI", "JD",
                  "AMAT", "ADSK", "VRTX", "WBA", "MNST", "IDXX", "MU", "LRCX", "EXC", "ORLY",
                  "NTES", "CTAS", "REGN", "SIRI", "ALXN", "SNPS", "ALGN", "ASML", "SGEN"]

endUrl = ":NASDAQ"
url_base = "https://www.google.com/finance/quote/"

for stock in nasdaq_symbols:
    url = url_base + stock.upper() + endUrl
    try:
        data = urllib.request.urlopen(url).read()
        data1 = data.decode("utf-8")
        m = re.search('data-last-price=', data1)
        if m:
            index = m.span()
            start = index[0] + 16
            end = index[1] + 8
            newString = data1[start:end]
            res = re.findall(r'\d+\.\d+|\d+', newString)
            for r in res:
                final = float(r)
                print(f"Current price of {stock.upper()} is {final} USD")
        else:
            print(f"Price data not found for {stock.upper()}.")
    except Exception as e:
        print(f"Error fetching data for {stock.upper()}: {e}")
