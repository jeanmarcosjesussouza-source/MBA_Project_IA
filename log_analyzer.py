import re
import pandas as pd
import numpy as np
import os
import time
from datetime import datetime
from sklearn.ensemble import IsolationForest

# Caminho dentro do container Docker (conforme mapeamos no volumes)
LOG_FILE = "/data/app.log"

def preprocess_logs():
    data = []
    log_pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (.+)'
    
    if not os.path.exists(LOG_FILE):
        print(f"ERRO: Arquivo não encontrado em {LOG_FILE}")
        return None

    print(f"Lendo: {LOG_FILE}")
    with open(LOG_FILE, 'r') as file:
        for line in file:
            match = re.match(log_pattern, line)
            if match:
                ts_str, level, msg = match.groups()
                ts = datetime.strptime(ts_str, '%Y-%m-%d %H:%M:%S')
                level_num = {"INFO": 0, "DEBUG": 1, "WARN": 2, "ERROR": 3}.get(level, -1)
                data.append([ts.hour, level_num, len(msg)])
    
    return pd.DataFrame(data, columns=['hour', 'level_num', 'message_length'])

def analyze_logs():
    df = preprocess_logs()
    if df is None: 
        return

    print("IA processando anomalias...")
    # Isolation Forest: Algoritmo para detectar outliers
    model = IsolationForest(contamination=0.05, random_state=42)
    df['anomaly'] = model.fit_predict(df)
    
    anomalies = df[df['anomaly'] == -1]
    
    print("\n=== Amostra de Anomalias Encontradas ===")
    print(anomalies.head(10))
    print("\n=== Resumo Estatístico (Para seu print) ===")
    print(df.describe())
    
    print("\nProcessamento concluído. Container ativo por 30s para leitura...")
    time.sleep(30)

if __name__ == '__main__':
    analyze_logs()