import pandas as pd


def run_rules_engine(df):
    def dynamic_global_variable(df):
        df_dict = df.to_dict('list')
        # print(df_dict)
        for name in df_dict:
            if name in ["Ticker", "Date"]:
                continue
            for i, val in enumerate(df_dict[name]):
                # print("%s_%s" % (df_dict["Ticker"][i], name), "=", df_dict[name][i])
                globals()["%s_%s" % (df_dict["Ticker"][i], name)] = df_dict[name][i]

    dynamic_global_variable(df)
    if QQQ_RSI14 > SPY_RSI14:
        print(">>> SPY Stronger")
    else:
        print(">>> QQQ Stronger")


def main():
  # df[df["Date"].isin(["2025-08-27", "2025-08-26"])][df["Ticker"].isin(["SPY", "QQQ"])].to_dict('list')
  data = {
      'Ticker': ['QQQ', 'QQQ', 'SPY', 'SPY'],
      'Date': ['2025-08-27', '2025-08-26', '2025-08-27', '2025-08-26'],
      'Close': [573.49, 572.61, 646.63, 645.16],
      'RSI14': [56.7, 55.86, 63.0, 61.68],
      }

  df = pd.DataFrame(data)
  print("Input Data:\n", df)
  run_rules_engine(df[df["Date"] == "2025-08-27"])

if __name__ == "__main__":
  main()
