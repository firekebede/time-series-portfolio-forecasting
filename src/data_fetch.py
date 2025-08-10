import yfinance as yf
import pandas as pd
from pathlib import Path

def fetch_data(tickers, start, end, save_dir="data/raw"):
    Path(save_dir).mkdir(parents=True, exist_ok=True)
    data = {}
    for t in tickers:
        df = yf.download(t, start=start, end=end, progress=False)
        df.reset_index(inplace=True)
        df.to_csv(f"{save_dir}/{t}.csv", index=False)
        data[t] = df
    return data

if __name__ == "__main__":
    tickers = ["TSLA", "BND", "SPY"]
    start = "2015-07-01"
    end = "2025-07-31"
    fetch_data(tickers, start, end)
