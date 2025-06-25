from fetch_pjm import fetch_pjm_lmp
import pandas as pd
from datetime import datetime, timedelta

BASE_URL = "https://api.pjm.com/api/v1"  # Placeholder (PJM LMP is on Data Miner 2)

# URL costruito per scaricare LMP nodali DA o RT (qui esempio RT)
URL_TEMPLATE = (
    "https://dataminer2.pjm.com/feed/rt_lmp_by_location/definition"
    "?startRow=0&rowCount=5000"
)

HEADERS = {
    "User-Agent": "Mozilla/5.0",
}

def fetch_pjm_lmp(feed="rt_lmp_by_location", hours=1):
    """Scarica LMP nodali Real-Time o Day-Ahead"""
    end = datetime.utcnow()
    start = end - timedelta(hours=hours)

    url = f"https://dataminer2.pjm.com/feed/{feed}/csv?startdatetime={start:%Y-%m-%dT%H:00Z}&enddatetime={end:%Y-%m-%dT%H:00Z}"
    print(f"🔗 Download: {url}")
    response = requests.get(url, headers=HEADERS)
    if response.status_code != 200:
        raise Exception(f"Errore fetch PJM: {response.status_code}")

    df = pd.read_csv(pd.compat.StringIO(response.text))
    df = df.rename(columns={
        "Datetime": "timestamp",
        "Location": "node",
        "LMP": "lmp",
        "Congestion": "congestion",
        "Loss": "loss"
    })
    df["market"] = "PJM"
    df["type"] = "RT" if "rt" in feed else "DA"
    return df[["timestamp", "market", "node", "lmp", "congestion", "loss", "type"]]