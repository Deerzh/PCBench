import pandas as pd
df = pd.DataFrame(dict(name=['Raphael', 'Donatello'], mask=['red', 'purple'], weapon=['sai', 'bo staff']))
print(df.to_latex(None, columns=None, col_space=None))
