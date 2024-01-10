# my_dag.py
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator

# Define default_args dictionary to pass to the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Instantiate a DAG
dag = DAG(
    'my_dag',
    default_args=default_args,
    description='A simple Airflow DAG with three tasks',
    schedule_interval=timedelta(days=1),
)

# Task 1: BashOperator
task_bash = BashOperator(
    task_id='bash_task',
    bash_command='echo "Hello from Bash!"'
    # Add your additional Bash commands as needed.
    ,
    dag=dag,
)

# Task 2: PythonOperator
def python_function():
    print("Hello from Python!")

task_python = PythonOperator(
    task_id='python_task',
    python_callable=python_function,
    dag=dag,
)

# Task 3: DummyOperator
task_dummy = DummyOperator(
    task_id='dummy_task',
    dag=dag,
)

# Set task dependencies
task_bash >> task_python >> task_dummy
