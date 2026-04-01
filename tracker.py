import pandas as pd
from datetime import datetime

CITIES = ["Hyderabad", "Bengaluru"]
TITLES = ["director", "head", "senior manager", "vp","Associate Director"]

def fetch_jobs():
    with open("roles.yaml") as f:
        config = yaml.safe_load(f)

    data = [
        [r["city"], r["company"], r["title"], r["url"]]
        for r in config["roles"]
    ]

    return pd.DataFrame(data, columns=["City","Company","Role Title","Job URL"])

def main():
    df = fetch_jobs()
    df["Date Pulled"] = datetime.today().strftime("%Y-%m-%d")
    df = df[["Date Pulled","City","Company","Role Title","Job URL"]]
    df.to_excel("GBS_Leadership_Roles.xlsx", index=False)

if __name__ == "__main__":
    main()
