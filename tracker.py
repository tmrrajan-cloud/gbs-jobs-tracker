import pandas as pd
from datetime import datetime

CITIES = ["Hyderabad", "Bengaluru"]
TITLES = ["director", "head", "senior manager", "vp"]

def fetch_jobs():
    # Replace later with real scraping or API
    jobs = [
        ["Hyderabad", "Reckitt", "Senior Manager - GBS Migration", "https://careers.reckitt.com"],
        ["Bengaluru", "Standard Chartered", "Director - Global Business Services", "https://sc.com/careers"],
    ]
    return pd.DataFrame(jobs, columns=["City","Company","Role Title","Job URL"])

def main():
    df = fetch_jobs()
    df["Date Pulled"] = datetime.today().strftime("%Y-%m-%d")
    df = df[["Date Pulled","City","Company","Role Title","Job URL"]]
    df.to_excel("GBS_Leadership_Roles.xlsx", index=False)

if __name__ == "__main__":
    main()
