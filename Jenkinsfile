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
                script {
                    // Clean up any existing MongoDB container
                    sh 'docker ps -q --filter "name=mongodb" | grep -q . && docker stop mongodb && docker rm mongodb || true'
                    // Start MongoDB container
                    sh 'docker run -d --name mongodb -p 27017:27017 mongo'
                    // Wait for MongoDB to be ready
                    sh 'while ! docker exec mongodb mongosh --eval "db.adminCommand(\'ping\')"; do sleep 1; done'
                    // Run tests with MongoDB connection
                    sh 'docker run --rm --link mongodb:mongo -e MONGO_URI=mongodb://mongo:27017 $IMAGE_NAME pytest || exit 1'
                }
            }
            post {
                always {
                    // Clean up MongoDB container
                    sh 'docker stop mongodb && docker rm mongodb || true'
                }
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
