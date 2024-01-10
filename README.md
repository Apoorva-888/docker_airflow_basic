# Airflow Dockerized Project
This project demonstrates how to set up Apache Airflow in a Dockerized environment for managing and orchestrating workflows.
## Getting Started
These instructions will help you set up and run Apache Airflow locally using Docker.
### Prerequisites
- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)
### Running the Project
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/airflow-docker-project.git
Navigate to the project directory:
  ```bash
  cd airflow-docker-project
Build and start the Docker containers:
  ```bash
  docker-compose up --build
This will build the Airflow image (if not already built) and start the Airflow services.
### Access the Airflow Web UI:
Open your web browser and go to http://localhost:8080. Log in with the default credentials:
- Username: admin
- Password: admin
### Explore and Trigger DAGs:
Navigate to the "DAGs" section in the Airflow Web UI to view and trigger your DAGs.
Shut Down Airflow:
When you are done, stop the services by pressing Ctrl + C in the terminal.
