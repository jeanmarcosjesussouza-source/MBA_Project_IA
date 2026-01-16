import random
import os
from datetime import datetime, timedelta

def gerar_log_gigante(num_linhas):
    # Pega o caminho da pasta onde o script está rodando
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(base_dir, "data")
    
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    caminho_completo = os.path.join(data_dir, "app.log")
    
    niveis = ["INFO", "ERROR", "DEBUG", "WARN"]
    mensagens = ["User login", "DB Connection failed", "Query executed in {}ms", "Access denied"]
    start_date = datetime(2024, 11, 8, 10, 0, 0)
    
    print(f"Salvando em: {caminho_completo}")
    print("Gerando 1 milhão de linhas... aguarde uns segundos.")
    
    with open(caminho_completo, 'w') as f:
        for i in range(num_linhas):
            data_atual = start_date + timedelta(seconds=i)
            level = random.choice(niveis)
            msg = random.choice(mensagens)
            if "{}" in msg:
                msg = msg.format(random.randint(50, 500))
            f.write(f"{data_atual.strftime('%Y-%m-%d %H:%M:%S')} {level} {msg}\n")
            
    print("Concluído com sucesso!")

if __name__ == '__main__':
    gerar_log_gigante(1000000)