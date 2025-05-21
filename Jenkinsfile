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
                    branch: 'main'
                )
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker image..."
                bat "docker build -t %IMAGE_NAME% ."
            }
        }

        stage('Run Unit Tests') {
            steps {
                echo "Running unit tests..."
                bat "python -m unittest test_app.py"
            }
        }

        stage('Deploy') {
            steps {
                echo "Deploying container..."
                bat "docker stop %CONTAINER_NAME% || echo Not running"
                bat "docker rm %CONTAINER_NAME% || echo Not found"
                bat "docker run -d --name %CONTAINER_NAME% -p 5000:5000 %IMAGE_NAME%"
            }
        }
    }

    post {
        always {
            echo "Cleaning workspace..."
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
