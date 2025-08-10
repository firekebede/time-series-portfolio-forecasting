
import os
import yfinance as yf
import pandas as pd

# --- Configuration ---
ASSETS = ["TSLA", "BND", "SPY"]
START_DATE = "2015-07-01"
END_DATE = "2025-07-31"

RAW_DIR = "data/raw"
PROCESSED_DIR = "data/processed"

# Create folders if they don't exist
os.makedirs(RAW_DIR, exist_ok=True)
os.makedirs(PROCESSED_DIR, exist_ok=True)

# --- Function to fetch, clean, and save ---
def fetch_and_clean(ticker):
    print(f"Fetching data for {ticker}...")
    
    # Download data
    df = yf.download(ticker, start=START_DATE, end=END_DATE)
    
    # Save raw data
    raw_path = os.path.join(RAW_DIR, f"{ticker}_raw.csv")
    df.to_csv(raw_path)
    
    # Reset index (Date as a column)
    df.reset_index(inplace=True)
    
    # Ensure correct data types
    df["Date"] = pd.to_datetime(df["Date"])
    
    # Check & handle missing values (forward fill then backward fill)
    if df.isnull().values.any():
        print(f"Missing values found in {ticker}, filling...")
        df = df.fillna(method="ffill").fillna(method="bfill")
    
    # Save processed data
    processed_path = os.path.join(PROCESSED_DIR, f"{ticker}_cleaned.csv")
    df.to_csv(processed_path, index=False)
    
    print(f"✅ {ticker} processed and saved to {processed_path}")

# --- Main Loop ---
if __name__ == "__main__":
    for asset in ASSETS:
        fetch_and_clean(asset)
    print("🎯 All data fetched, cleaned, and saved.")