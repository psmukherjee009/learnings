# learnings

# Code to move df row columns to global variables

```python
def run_rules_engine(df):
  def dynamic_global_variable(df):
    df_dict = df.to_dict('list')
    for name in df_dict:
      globals()[name] = df_dict[name][0]

  dynamic_global_variable(df)
```