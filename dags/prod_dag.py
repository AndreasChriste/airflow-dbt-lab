from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator
from pendulum import datetime

# Caminho do projeto dbt (onde ficam dbt_project.yml e profiles.yml)
DBT_DIR = "/usr/local/airflow/projeto1"

with DAG(
    dag_id="dbt_pipeline_prod",
    start_date=datetime(2024, 1, 1),
    schedule=None,        # Executa apenas quando disparada manualmente
    catchup=False,
    tags=["dbt"],
) as dag:
    # Dummy inicial
    start = EmptyOperator(task_id="start")

    # dbt seed (target = prod)
    dbt_seed = BashOperator(
        task_id="dbt_seed_prod",
        bash_command=f"dbt seed --project-dir {DBT_DIR} --profiles-dir {DBT_DIR} --target prod",
    )

    # dbt run (target = prod)
    dbt_run = BashOperator(
        task_id="dbt_run_prod",
        bash_command=f"dbt run --project-dir {DBT_DIR} --profiles-dir {DBT_DIR} --target prod",
    )

    # Dummy final
    end = EmptyOperator(task_id="end")

    # Definindo a ordem das tarefas
    start >> dbt_seed >> dbt_run >> end
