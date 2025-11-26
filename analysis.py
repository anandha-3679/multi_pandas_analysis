import pandas as pd

datasets = {
    "dataset_24x3.csv": "data/dataset_24x3.csv",
    "dataset_38x3.csv": "data/dataset_38x3.csv",
    "dataset_43x4.csv": "data/dataset_43x4.csv"
}

def analyze(name, path):
    print("\n====================================================")
    print(f"📌 ANALYZING: {name}")
    print("====================================================")

    df = pd.read_csv(path)

    print("\n--- BASIC INFO ---")
    print(df.info())

    print("\n--- FIRST 5 ROWS ---")
    print(df.head())

    print("\n--- SHAPE ---")
    print(df.shape)

    print("\n--- COLUMN NAMES ---")
    print(df.columns.tolist())

    print("\n--- MISSING VALUES ---")
    print(df.isnull().sum())

    print("\n--- SUMMARY (NUMERIC) ---")
    print(df.describe())

    print("\n--- SUMMARY (CATEGORICAL) ---")
    print(df.describe(include='object'))

    print("\n--- UNIQUE VALUE COUNT ---")
    for col in df.columns:
        print(f"{col}: {df[col].nunique()}")

    print("\n--- VALUE COUNTS (CATEGORICAL) ---")
    for col in df.select_dtypes(include='object'):
        print(f"\nColumn: {col}")
        print(df[col].value_counts())

    print("\n--- CORRELATION (PANDAS ONLY) ---")
    print(df.corr(numeric_only=True))

    print("\n--- SAMPLE SORT ---")
    print(df.sort_values(by=df.columns[0]).head())

    print("\n--- GROUPING (IF ANY CATEGORICAL EXISTS) ---")
    cats = df.select_dtypes(include='object')
    if len(cats.columns) > 0:
        col = cats.columns[0]
        print(df.groupby(col).size())

    print("\n✔ DONE\n")


# RUN ANALYSIS FOR ALL 3 DATASETS
for name, path in datasets.items():
    try:
        analyze(name, path)
    except FileNotFoundError:
        print(f"⚠ File missing: {path}")
