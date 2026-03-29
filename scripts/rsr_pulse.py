import os
from datetime import datetime

# Tu ruta del showroom
REPO_PATH = r"C:\data1\datapro+-factory-special-showroom"

def emitir_pulso():
    ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_file = os.path.join(REPO_PATH, "HEARTBEAT.log")
    
    with open(log_file, "a") as f:
        f.write(f"💓 [RSR-TELEMETRY] System Online - Pulse Detected: {ahora}\n")
    
    print(f"Sincronización de latido completada: {ahora}")

if __name__ == "__main__":
    emitir_pulso()