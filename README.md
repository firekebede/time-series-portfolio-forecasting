# time-series-portfolio-forecasting
Time Series Forecasting for Portfolio Management Optimization (TSLA, BND, SPY)

Overview

This project walks you through forecasting Tesla (TSLA) stock prices, building an optimized investment portfolio, and testing its performance. The aim is to make stock analysis approachable and understandable.

What the Project Does

Collects historical data for TSLA, BND, and SPY.

Preprocesses the data to ensure clean, chronological time series.

Forecasts TSLA prices using ARIMA (statistical model) and LSTM (deep learning model).

Optimizes a portfolio combining TSLA with BND and SPY using Modern Portfolio Theory.

Backtests the portfolio against a simple benchmark (60% SPY / 40% BND) to see how it would have performed.

Why It's Useful

Helps understand how forecasting models work.

Shows how to balance risk and reward in a portfolio.

Demonstrates the importance of backtesting before real investments.

How to Use

Make sure you have Python installed with libraries: yfinance, pandas, numpy, matplotlib, tensorflow, pmdarima.

Run each task step-by-step:

Task 1: Load and preprocess data.

Task 2: Train ARIMA and LSTM models.

Task 3: Forecast future prices and visualize trends.

Task 4: Optimize portfolio weights.

Task 5: Backtest strategy and compare against benchmark.

Review plots, metrics, and tables to interpret results.

Key Takeaways

ARIMA is quick and interpretable but may miss complex patterns.

LSTM captures non-linear trends but requires more data.

Optimized portfolios can outperform simple benchmarks.

Backtesting validates model-driven investment strategies.

Notes

Always consider real-world factors like transaction costs and market liquidity.

This project is for educational purposes and not financial advice.
