import pandas as pd
from sqlalchemy import create_engine

# 1. Configurar a conexão com o MariaDB

usuario = 'root'
senha = '' 
host = 'localhost'
banco = 'Sustentabilidade_e_consumo'

engine = create_engine(f'mysql+pymysql://{usuario}:{senha}@{host}/{banco}')

# 2. Buscar os dados das leituras cruzando com os setores
query = """
SELECT 
    l.id_leitura,
    l.data_leitura,
    s.nome_setor,
    l.consumo_kwh
FROM tb_leituras l
INNER JOIN tb_setores s ON l.id_setor = s.id_setor;
"""

# 3. Carrega o resultado direto no Pandas
df = pd.read_sql(query, engine)

# 4. Processamento dos dados no Python
media_consumo = df['consumo_kwh'].mean()

# Criação de alerta: identifica medições com consumo acima de 300 kWh
df['status'] = df['consumo_kwh'].apply(lambda x: '⚠️ Alerta: Alto Consumo' if x > 300 else '✅ Normal')

# 5. Exibir os resultados organizados no terminal
print("\n" + "="*45)
print(f" MÉDIA GERAL DE CONSUMO: {media_consumo:.2f} kWh")
print("="*45 + "\n")

print("--- ANÁLISE DE ANOMALIAS DE ENERGIA ---")
print(df[['data_leitura', 'nome_setor', 'consumo_kwh', 'status']].to_string(index=False))
print("\n")