# Other workflow tools: Luigi, SSIS(MSSQL), Bash scripting
# DAG: Directed Acyclic Graph

# Which command would you enter in the console to run the desired task?
airflow run etl_pipeline download_file 2020-01-08
# airflow run <dag_id> <task_id> <start_date>

# =====================================================

# What is DAG?
# Directed, there is an inherent flow representing dependencies between components.
# Acyclic, does not loop / cycle / repeat
# Graph, the actual set of components

# Import the DAG object
from airflow.models import DAG

# Define the default_args dictionary
default_args = {
  'owner': 'dsmith',
  'start_date': datetime(2020, 1, 14),
  'retries': 2
}

# Instantiate the DAG object
etl_dag = DAG('example_etl', default_args=default_args)

# =====================================================

# Multiple DAGs are already defined for you. How many DAGs are present in the Airflow system from the command-line?
airflow list_dags

# =====================================================

from airflow.models import DAG
default_args = {
  'owner': 'jdoe',
  'email': 'jdoe@datacamp.com'
}
dag = DAG( 'refresh_data', default_args=default_args )

from airflow.models import DAG
default_args = {
  'owner': 'jdoe',
  'start_date': '2019-01-01'
}
dag = DAG( dag_id="etl_update", default_args=default_args )

# =====================================================

# Which airflow command would you use to start the webserver on port 9090?
airflow webserver -p 9090

# Which of the following events have not run on your Airflow instance?
# Browse -> Logs

# DAGs -> Code To see what operators have been used
