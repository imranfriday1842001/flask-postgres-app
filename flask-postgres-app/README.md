🚀 Flask + PostgreSQL + Docker + Kubernetes App

This project is a Flask web application backed by a PostgreSQL database, containerized using Docker and deployable on Kubernetes.
It’s a perfect end-to-end example for learning how to build, containerize, and deploy a full-stack Python microservice.

🧩 Features

- Flask backend
- PostgreSQL database
- Dockerized for easy deployment
- Kubernetes-ready manifests

---

## Prerequisites
- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [kubectl](https://kubernetes.io/docs/tasks/tools/) (optional, for Kubernetes deployment)

---

## Run Locally with Docker

1. Pull the Docker image:
```bash
docker pull imranfriday1842001/flask-postgres-app:latest
Build and start containers:

docker-compose up --build


Open your browser at http://localhost:5050
 to see the app running.

Stop containers:

docker-compose down

📦 Docker Hub

Pull the Docker image directly:

docker pull imranfriday1842001/flask-postgres-app:latest

☸️ Kubernetes Deployment

Make sure Docker Desktop Kubernetes is enabled.

Deploy the stack:

kubectl apply -f k8s-manifests/


Check the pods:

kubectl get pods -n flask-postgres-app


Access the app using the LoadBalancer port.

📂 Project Structure
flask-postgres-app/
├── app/                   # Flask application
├── Dockerfile             # Web container build instructions
├── docker-compose.yml     # Docker Compose stack
├── README.md              # Project documentation
└── requirements.txt       # Python dependencies

✨ Notes

The app is development-ready. For production, use a WSGI server like Gunicorn.

Database data is persisted using Docker volumes.

Change ports in docker-compose.yml if 5050 or 5432 is already in use.

📖 References

Flask Documentation

PostgreSQL Documentation

Docker Documentation

Kubernetes Documentation
