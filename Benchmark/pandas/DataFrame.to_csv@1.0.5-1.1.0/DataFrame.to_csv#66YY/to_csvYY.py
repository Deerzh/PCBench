import pandas as pd
df = pd.DataFrame({'name': ['Raphael', 'Donatello'], 'mask': ['red', 'purple'], 'weapon': ['sai', 'bo staff']})
df.to_csv(path_or_buf=None, sep=',', na_rep='', float_format=None, columns=None, header=True, index=False, index_label=None, mode='w', encoding=None)
