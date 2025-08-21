import argparse
import sys

import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_text



def print_decision_rules(csv_file):
    # Load your CSV data
    df = pd.read_csv(csv_file)
    # Features (drop numdays if you want to test both ways)
    X = df.drop(columns=["perchange"])
    y = df["perchange"].astype(int)

    # Train Decision Tree
    clf = DecisionTreeClassifier(max_depth=4, random_state=42)  # limit depth for readable rules
    clf.fit(X, y)

    # Print decision rules
    rules = export_text(clf, feature_names=list(X.columns))
    print(rules)


def parse_input():
    DESC = """
    Usage: %(prog)s version_id
    """
    EXAMPLES = """
    eg: python3 %(prog)s v1
    python3 %(prog)s v3
    """
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter, description=DESC,
                                   epilog=EXAMPLES)
    parser.add_argument('csv_file', help='CSV File')
    if len(sys.argv) < 2:
        parser.parse_args(['-h'])
    args = parser.parse_args()
    return args


def main():
    args = parse_input()
    print_decision_rules(args.csv_file)


if __name__ == "__main__":
  main()
