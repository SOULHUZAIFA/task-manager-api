pipeline {
    agent any

    environment {
        IMAGE_NAME = "task-manager-api"
        CONTAINER_NAME = "task-manager"
        DOCKER_HOST = "unix:///Users/huzaifamehdi/.docker/run/docker.sock"
        PATH = "/usr/local/bin:${PATH}"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/SOULHUZAIFA/task-manager-api.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh '/usr/local/bin/docker build -t task-manager-api .'
            }
        }
        stage('Run Unit Tests in Docker') {
            steps {
                sh 'docker run --rm $IMAGE_NAME pytest || exit 1'
            }
        }
        stage('Stop Existing Container') {
            steps {
                script {
                    sh 'docker ps -q --filter "name=$CONTAINER_NAME" | grep -q . && docker stop $CONTAINER_NAME && docker rm $CONTAINER_NAME || true'
                }
            }
        }
        stage('Run New Container') {
            steps {
                sh 'docker run -d --name $CONTAINER_NAME -p 5001:5000 $IMAGE_NAME'
            }
        }
        stage('Cleanup') {
            steps {
                sh 'docker image prune -f'
            }
        }
    }
}
