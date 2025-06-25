from ingest_nodal import ingest_pjm
from ingest_miso import ingest_miso
from ingest_ercot import ingest_ercot

def run_all_ingests():
    print("🚀 Avvio ingest multi-market nodale...")
    ingest_pjm()
    ingest_miso()
    ingest_ercot()
    print("✅ Tutti i mercati aggiornati!")

if __name__ == "__main__":
    run_all_ingests()