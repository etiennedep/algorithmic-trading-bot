# CPPI Strategy User Guide

## Overview
This notebook implements a Constant Proportion Portfolio Insurance (CPPI) strategy using Python and yfinance data. The strategy dynamically allocates between a risky asset (SPY) and a safe asset (TLT), with transaction costs and interactive parameter tuning.

## How to Use

1. **Setup**
   - Ensure you have the `trading-bot` conda environment active.
   - Launch JupyterLab:  
     ```
     conda activate trading-bot
     jupyter lab
     ```
   - Open `notebooks/01_CPPI_development.ipynb`.

2. **Data Acquisition**
   - The notebook automatically downloads daily data for SPY and TLT using yfinance.

3. **Parameters**
   - `initial_capital`: Starting portfolio value (default: $100,000)
   - `floor_pct`: Minimum portfolio value as a fraction of initial capital (slider)
   - `multiplier`: Risk multiplier (slider)
   - `cost_per_dollar`: Transaction cost per dollar traded (default: 0.0005)

4. **Running the Simulation**
   - Use the interactive sliders at the end of the notebook to test different `floor_pct` and `multiplier` values.
   - The notebook will plot CPPI vs. Buy & Hold and print summary statistics. 

5. **Interpreting Results**
   - The plot shows the evolution of portfolio value under both strategies.
   - Summary statistics include initial/final value, total return, and total transaction costs.

## Requirements

- Python 3.11
- yfinance, pandas, numpy, matplotlib, ipywidgets
- See `requirements.txt` for the complete list

## Troubleshooting

- If data download fails, check your internet connection and try again.
- If widgets do not appear, ensure `ipywidgets` is installed and JupyterLab is restarted.

## File Structure

- `notebooks/01_CPPI_development.ipynb`: Main CPPI notebook
- `strategies/cppi.py`: CPPI strategy class
- `requirements.txt`: List of required Python packages

---



