import pandas as pd
df = pd.DataFrame(dict(name=['Raphael', 'Donatello'], mask=['red', 'purple'], weapon=['sai', 'bo staff']))
print(df.to_latex(None, columns=None, col_space=None, header=True, index=True, na_rep='NaN', formatters=None, float_format=None, sparsify=None, index_names=True, bold_rows=False, column_format=None, longtable=None, escape=None, encoding=None, decimal='.', multicolumn=None))
