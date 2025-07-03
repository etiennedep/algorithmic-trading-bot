# strategies/cppi.py

import numpy as np

class CPPI:
    def __init__(self, floor_pct, multiplier, initial_capital):
        self.floor_pct = floor_pct
        self.multiplier = multiplier
        self.initial_capital = initial_capital
        self.floor = self.floor_pct * self.initial_capital
        self.portfolio_value = initial_capital

    def allocate(self):
        cushion = max(self.portfolio_value - self.floor, 0)
        risky_alloc = min(self.multiplier * cushion, self.portfolio_value)
        safe_alloc = self.portfolio_value - risky_alloc
        return risky_alloc, safe_alloc

    def rebalance_with_cost(self, risky_return, safe_return, previous_risky_alloc, cost_per_dollar):
        # 1. Calculate new allocations
        new_risky_alloc, new_safe_alloc = self.allocate()

        # 2. Compute transaction cost on change in risky position
        trade_amount = abs(new_risky_alloc - previous_risky_alloc)
        cost = trade_amount * cost_per_dollar
        self.portfolio_value -= cost

        # 3. Apply returns to each bucket
        self.portfolio_value = (
            new_risky_alloc * (1 + risky_return) +
            new_safe_alloc * (1 + safe_return)
        )
        return new_risky_alloc, cost

    def rebalance(self, risky_return, safe_return):
        # Legacy no-cost rebalancing
        risky_alloc, safe_alloc = self.allocate()
        self.portfolio_value = (
            risky_alloc * (1 + risky_return) +
            safe_alloc * (1 + safe_return)
        )
        return self.portfolio_value
