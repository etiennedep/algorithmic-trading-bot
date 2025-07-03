from strategies.cppi import CPPI
from strategies.asset_selector import SimpleAssetSelector
import yfinance as yf
import pandas as pd

# Parameters
initial_capital = 100000
floor_pct = 0.8
multiplier = 3

# Set up CPPI and selectors
cppi = CPPI(floor_pct, multiplier, initial_capital)
selector = SimpleAssetSelector()

# Download daily data
risky_asset = selector.select_risky()[0]
safe_asset = selector.select_safe()[0]
start_date = '2022-01-01'
end_date = '2023-01-01'

# Download data - the key fix is handling the MultiIndex columns
risky_data_raw = yf.download(risky_asset, start=start_date, end=end_date)
safe_data_raw = yf.download(safe_asset, start=start_date, end=end_date)

# Extract close prices properly (yfinance returns MultiIndex columns)
risky_data = risky_data_raw['Close'].iloc[:, 0] if len(risky_data_raw['Close'].shape) > 1 else risky_data_raw['Close']
safe_data = safe_data_raw['Close'].iloc[:, 0] if len(safe_data_raw['Close'].shape) > 1 else safe_data_raw['Close']

# Create aligned DataFrame
data = pd.DataFrame({
    'risky': risky_data.pct_change().fillna(0),
    'safe': safe_data.pct_change().fillna(0)
})

# Run CPPI simulation
portfolio_values = []
for idx, row in data.iterrows():
    cppi.rebalance(row['risky'], row['safe'])
    portfolio_values.append(cppi.portfolio_value)

# Plot results
import matplotlib.pyplot as plt
plt.figure(figsize=(12, 6))
plt.plot(data.index, portfolio_values, label='CPPI Portfolio', linewidth=2)
plt.title('CPPI Portfolio Value Over Time')
plt.xlabel('Date')
plt.ylabel('Portfolio Value ($)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

print(f"Initial Capital: ${initial_capital:,.2f}")
print(f"Final Portfolio Value: ${portfolio_values[-1]:,.2f}")
print(f"Total Return: {(portfolio_values[-1]/initial_capital - 1)*100:.2f}%")
