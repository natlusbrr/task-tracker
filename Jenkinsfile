pipeline {
    agent any

    environment {
        IMAGE_NAME = 'task-tracker'
        CONTAINER_NAME = 'task-tracker-container'
    }

    stages {
        stage('Checkout Code') {
            steps {
                git(
                    url: 'https://github.com/natlusbrr/task-tracker.git',
                    credentialsId: 'github-https', 
                    branch: 'main'
                )
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker image"
                bat "docker build -t %IMAGE_NAME% ."
            }
        }

        stage('Run Unit Tests') {
            steps {
                echo "Running unit tests"
                bat '"C:\\Users\\ImExp\\AppData\\Local\\Programs\\Python\\Python310\\python.exe" -m unittest testApp.py'
            }
        }

        stage('Deploy') {
        steps {
        echo "Deploying container"
        bat '''
        docker stop task-tracker-container || echo Not running
        docker rm task-tracker-container || echo Not found
        docker run -d --name task-tracker-container -p 5000:5000 task-tracker
        '''
    }
}
    }

    post {
        always {
            echo "Cleaning workspace"
            cleanWs()
        }
        failure {
            echo "The pipeline failed"
        }
        success {
            echo "Pipeline was completed successfully"
        }
    }
}
