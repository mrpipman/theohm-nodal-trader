import schedule
import time
from ingest_all_nodal import run_all_ingests

def task():
    print("⏰ Avvio ingest nodale schedulato")
    run_all_ingests()

schedule.every().day.at("08:00").do(task)

print("🕓 Scheduler attivo per ingest nodale alle 08:00")

while True:
    schedule.run_pending()
    time.sleep(60)