# Projeto Airflow + dbt

Este é um projeto desenvolvido **para praticar conhecimentos em Engenharia de Dados** utilizando **Apache Airflow** e **dbt (data build tool)**.  

A arquitetura segue o padrão **raw → staging → core**, equivalente às camadas **bronze → silver → gold** em data lakes:  

- **Raw (Bronze)**: dados crus, vindos diretamente da fonte.  
- **Staging (Silver)**: dados limpos e padronizados.  
- **Core (Gold)**: dados refinados para análise de negócio e dashboards.  

O projeto não é para produção, mas sim um **laboratório de prática**, ideal para aprender a estruturar pipelines de dados modernos.

---

## 🚀 Como configurar e rodar o projeto

1. Definir a porta do Postgres (evita conflito com a 5432(postgres) local):  
   ```bash
   astro config set postgres.port 5433

2. Start no projeto e  verificação das dags no airflow porta 8080
    ```
    astro dev start

 
