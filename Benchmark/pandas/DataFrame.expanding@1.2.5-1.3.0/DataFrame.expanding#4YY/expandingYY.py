import pandas as pd
import numpy as np
df = pd.DataFrame({'B': [0, 1, 2, np.nan, 4]})
df.expanding(2,  None).sum()
