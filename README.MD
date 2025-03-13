Task Manager API 🚀

A Flask-based Task Manager API with MongoDB, Docker, and Jenkins CI/CD for automated deployment.

📌 Features

✅ CRUD Operations (Create, Read, Update, Delete) for Tasks
✅ MongoDB as Database
✅ Unit Testing with pytest
✅ CI/CD with Jenkins & Docker
✅ GitHub Integration for Auto Deployment

📂 Project Structure

task-manager-api/
│── .github/workflows/ # (Optional) GitHub Actions for CI/CD
│── tests/ # Unit tests
│── .gitignore # Ignore unnecessary files
│── Jenkinsfile # CI/CD pipeline script for Jenkins
│── Dockerfile # Containerization setup
│── requirements.txt # Dependencies
│── app.py # Main Flask Application
│── database.py # MongoDB connection
│── task_routes.py # Task API routes
│── models.py # Data models
└── README.md # Project documentation

🛠 Setup & Installation

1️⃣ Clone the Repository

git clone https://github.com/SOULHUZAIFA/task-manager-api.git
cd task-manager-api

2️⃣ Install Dependencies

pip install -r requirements.txt

3️⃣ Start MongoDB

Ensure MongoDB is running locally or use MongoDB Atlas.

4️⃣ Run the Application

python app.py

The API will be available at:
🔗 http://localhost:5000/tasks

🐳 Docker Setup

1️⃣ Build the Docker Image

docker build -t task-manager-api .

2️⃣ Run the Docker Container

docker run -d --name task-manager -p 5000:5000 task-manager-api

3️⃣ Verify the API

curl -X GET http://localhost:5000/tasks

🧪 Running Unit Tests

pytest tests/

🚀 CI/CD Pipeline with Jenkins

Jenkinsfile Pipeline

The pipeline: 1. Clones the GitHub repository 2. Builds a Docker image 3. Runs unit tests inside the container 4. Deploys the updated container

Setting Up Jenkins 1. Install Jenkins:

brew install jenkins-lts
brew services start jenkins-lts

    2.	Add GitHub Credentials in Jenkins.
    3.	Create a Jenkins Pipeline with the Jenkinsfile.
    4.	Trigger Builds Automatically on GitHub commits.

🚀 Deployment

Option 1: Deploy to Heroku 1. Login to Heroku:

heroku login

    2.	Create an app:

heroku create task-manager-api

    3.	Add MongoDB:

heroku addons:create mongolab:sandbox

    4.	Deploy:

git push heroku main

Option 2: Deploy with Docker

Use AWS, DigitalOcean, or VPS:

docker build -t task-manager-api .
docker run -d --restart always -p 5000:5000 task-manager-api

📌 API Endpoints

Method Endpoint Description
GET /tasks Get all tasks
POST /tasks Create a task
DELETE /tasks/:title Delete a task

🛠 Next Steps

✅ Add JWT Authentication
✅ Improve CI/CD with GitHub Actions
✅ Deploy to AWS (EC2 + Docker Compose)

📌 Contributing 1. Fork the repository 2. Create a new branch 3. Submit a pull request

Developed by Huzaifa 🚀🔥
