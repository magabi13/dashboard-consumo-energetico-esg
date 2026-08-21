# 📊 Dashboard de Consumo Energético & Gestão ESG

Este repositório contém uma solução para monitoramento de consumo de energia (kWh) e análise de custos por setor, desenvolvida com o objetivo de apoiar a tomada de decisões focada em eficiência operacional e metas de sustentabilidade (ESG).


---

## 📂 Estrutura do Repositório

* `dashboard de consumo energético.pbix`: Relatório interativo desenvolvido no Power BI.
* `analise_energia.py`: Script em Python para processamento de dados e análise complementar.
* `tb_leituras.csv`: Base de dados contendo os registros diários de consumo por setor.
* `tb_setores.csv`: Tabela com o cadastro dos setores operacionais e suas respectivas tarifas de custo por kWh.
* `excel.xlsx`: Planilha do Excel com a organização e consolidação inicial dos dados.
---

## 💡 Funcionalidades do Dashboard

* **Métricas Principais (KPIs):** Visualização consolidada do Consumo Total (1.565 kWh) e Custo Total em Reais (R$ 1.102,50).
* **Distribuição do Consumo:** Gráfico de rosca detalhando a representatividade de cada setor (Produção, Escritório, Depósito e Refeitório).
* **Evolução Diária:** Gráfico de colunas empilhadas para acompanhar variações de consumo ao longo dos dias.
* **Filtros Dinâmicos:** Botoeira interativa por setor para análise isolada dos dados.

---

## 🛠️ Tecnologias Utilizadas

* **Power BI** (Power Query para ETL e DAX para modelagem de métricas)
* **Python** (Pandas para manipulação e validação dos dados)
* **SQL / MySQL (XAMPP)**: Criação e estruturação do banco de dados relacional para armazenar os registros de consumo e setores.

---

