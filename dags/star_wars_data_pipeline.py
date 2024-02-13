# Importa a classe DAG do módulo airflow.
from airflow import DAG
# Importa o PythonOperator do módulo de operadores do python.
from airflow.operators.python_operator import PythonOperator
# Importa a classe datetime do módulo datetime para definir datas e horas.
from datetime import datetime, timedelta

# Adiciona o diretório utils ao path para permitir importações dos scripts.
import sys
sys.path.append('/opt/airflow/dags/utils')

# Importa as funções dos scripts localizados no diretório utils.
from script_request import main as main
from script_results import generate_results_json as generate_results_json

# Define argumentos padrão que serão passados para cada tarefa do DAG.
default_args = {
    'owner': 'airflow',  # Define o proprietário do DAG, geralmente 'airflow' ou o nome de usuário do criador do DAG.
    'start_date': datetime.now() + timedelta(seconds=10) , # Define a data de início da execução do DAG.
    'schedule_interval': None,
    'retries': 5,  # Define o número de tentativas de reexecução em caso de falha.
}
