# Use the official Apache Airflow image
FROM apache/airflow:2.2.3

# Switch to root user to install additional dependencies
USER root

# Install any additional dependencies if needed
# For example, if you need extra Python packages:
# RUN pip install ...

# Switch back to the airflow user
USER airflow

# Copy the DAG file into the container
COPY my_dag.py /opt/airflow/dags/my_dag.py
