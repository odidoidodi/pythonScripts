
import re
import urllib.request

# Url is https://www.google.com/finance/quote/
# Used NASDAQ  ticker symbols.List below is example of most popular 100 of them:
nasdaq_symbols = [
    "AAPL", "MSFT", "AMZN", "GOOGL", "META", "TSLA", "NVDA", "PYPL", "INTC", "CSCO",
    "CMCSA", "PEP", "ADBE", "AVGO", "TXN", "COST", "NFLX", "TMUS", "CHTR", "SBUX",
    "AMGN", "QCOM", "MELI", "ATVI", "AMD", "GILD", "FISV", "BKNG", "ADI", "JD",
    "AMAT", "ADSK", "VRTX", "WBA", "MNST", "IDXX", "MU", "LRCX", "EXC", "ORLY",
    "NTES", "CTAS", "REGN", "SIRI", "ALXN", "SNPS", "ALGN", "ASML", "SGEN", "ROST",
    "XLNX", "EA", "SPLK", "KLAC", "VRSN", "CTSH", "MCHP", "SWKS", "CDNS", "DOCU",
    "INCY", "MXIM", "CHKP", "OKTA", "FOXA", "MXWL", "BMRN", "MRVL", "ANSS", "TMUSP",
    "TTWO", "MXL", "MRNA", "PTON", "MDLZ", "LBTYA", "ZM", "CRWD", "CTVA", "LULU", "CDW",
    "TTD", "SGMS", "VRSK", "ALXO", "ULTA", "FSLR", "CDAY", "VIAO", "PLUG", "ALVR", "IDCC",
    "ALAC", "BYND", "MNDY", "AMHC", "HOL", "BCAB", "PZAB", "JCOB", "BCDA", "JPST"]

url = "https://www.google.com/finance/quote/"
endUrl = ":NASDAQ"
stock = input("Enter your stock: ")
url = url + stock.upper() + endUrl
print("This data is fetched from " + url)

# Simple scrapping of data
data = urllib.request.urlopen(url).read()
data1 = data.decode("utf-8")
# print(data1)

# finding the key pattern in this case is:
m = re.search('data-last-price=', data1)
index = m.span()
# print(index)
start = index[0] + 16
end = index[1] + 8
newString = data1[start:end]

# Some regex from CHAT GPT because I was forgotten how to write this thinks.
res = re.findall(r'\d+\.\d+|\d+', newString)
for r in res:
    final = float(r)
    print(f"Current price of {stock.upper()} is {final} USD")
