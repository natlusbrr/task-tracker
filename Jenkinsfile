pipeline {
    agent any

    environment {
        IMAGE_NAME = 'task-tracker'
        CONTAINER_NAME = 'task-tracker-container'
    }

    stages {

        // STAGE 1: CHECKOUT CODE FROM GITHUB
        stage('Checkout Code') {
            steps {
                git(
                    url: 'https://github.com/natlusbrr/task-tracker.git',
                    credentialsId: 'github-https', // Set this if using a personal access token
                    branch: 'main'
                )
            }
        }

        // STAGE 2: BUILD DOCKER IMAGE
        stage('Build Docker Image') {
            steps {
                echo "Building Docker image..."
                sh "docker build -t ${IMAGE_NAME} ."
            }
        }

        // STAGE 3: RUN UNIT TESTS
        stage('Run Unit Tests') {
            steps {
                echo "Running tests..."
                sh "python3 -m unittest testApp.py"
            }
        }

        // STAGE 4: DEPLOY THE CONTAINER
        stage('Deploy') {
            steps {
                echo "Deploying container..."
                // Stop and remove previous container if it exists
                sh "docker stop ${CONTAINER_NAME} || true"
                sh "docker rm ${CONTAINER_NAME} || true"
                // Run the container with port mapping
                sh "docker run -d --name ${CONTAINER_NAME} -p 5000:5000 ${IMAGE_NAME}"
            }
        }
    }

    post {
        always {
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
