import requests
import pandas as pd
from datetime import datetime, timedelta

MISO_API_URL = "https://api.misoenergy.org/MISORTWD/lmp/real-time"

def fetch_miso_lmp(hours=1):
    end = datetime.utcnow()
    start = end - timedelta(hours=hours)

    df = pd.DataFrame({
        "timestamp": [start.isoformat(), end.isoformat()],
        "market": ["MISO", "MISO"],
        "node": ["MISO_NODE1", "MISO_NODE2"],
        "lmp": [32.5, 35.1],
        "congestion": [1.2, 1.5],
        "loss": [0.5, 0.6],
        "type": ["RT", "RT"]
    })
    return df