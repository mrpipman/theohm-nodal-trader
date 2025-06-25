import pandas as pd
from datetime import datetime, timedelta

def fetch_ercot_lmp(hours=1):
    end = datetime.utcnow()
    start = end - timedelta(hours=hours)

    df = pd.DataFrame({
        "timestamp": [start.isoformat(), end.isoformat()],
        "market": ["ERCOT", "ERCOT"],
        "node": ["ERCOT_NODE1", "ERCOT_NODE2"],
        "lmp": [28.4, 30.7],
        "congestion": [0.7, 1.0],
        "loss": [0.3, 0.2],
        "type": ["RT", "RT"]
    })
    return df