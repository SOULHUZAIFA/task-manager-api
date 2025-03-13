pipeline {
    agent any

    environment {
        IMAGE_NAME = "task-manager-api"
        CONTAINER_NAME = "task-manager"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/SOULHUZAIFA/task-manager-api.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }
        stage('Run Unit Tests in Docker') {
            steps {
                sh 'docker run --rm $IMAGE_NAME pytest'
            }
        }
        stage('Stop Existing Container') {
            steps {
                script {
                    sh 'docker stop $CONTAINER_NAME || true'
                    sh 'docker rm $CONTAINER_NAME || true'
                }
            }
        }
        stage('Run New Container') {
            steps {
                sh 'docker run -d --name $CONTAINER_NAME -p 5000:5000 $IMAGE_NAME'
            }
        }
        stage('Cleanup') {
            steps {
                sh 'docker system prune -f'
            }
        }
    }
}