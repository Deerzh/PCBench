import pandas as pd
import numpy as np
df = pd.Series({'B': 0})
df.ewm(0.5,  None,  None,  None, min_periods=0, adjust=True, ignore_na=False).mean()
