#!/usr/bin/env python3
"""Self-contained validation metric calculator."""
from __future__ import annotations

from statistics import mean
import math

observed = [33.1, 39.7, 38.8, 39.3, 8.4]
predicted = [31.92, 31.58, 36.48, 25.30, 11.30]

errors = [y - yhat for y, yhat in zip(observed, predicted)]
rmse = math.sqrt(mean([err * err for err in errors]))
mae = mean([abs(err) for err in errors])
bias = mean(errors)

print(f"rmse={rmse:.6f}")
print(f"mae={mae:.6f}")
print(f"bias={bias:.6f}")
