# Pandas DataFrame to Latex

Pandas allows to export a DataFrame as latex table using `to_latex()` directive.

```python
import pandas as pd
df = pd.DataFrame({'col1': range(4), 'col2': pd.Series([2, 3], index=[2, 3])}, index=range(4))
print(df.to_latex())
```

Using parameter `index` it is also possible to hide index column.

```python
import pandas as pd
df = pd.DataFrame({'col1': range(4), 'col2': pd.Series([2, 3], index=[2, 3])}, index=range(4))
print(df.to_latex(index=False))
```

[Notebook](./dataframe-to-latex.ipynb)

[Source](https://stackoverflow.com/questions/14380371/export-a-latex-table-from-pandas-dataframe)

[Documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_latex.html)