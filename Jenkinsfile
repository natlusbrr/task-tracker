/*
Author: Sultan Ahmed
File: Jenkinsfile
Purpose: This Jenkinsfile defines a CI/CD pipeline using Jenkins and Docker.
It includes 3 stages:
  1. Checkout: Pulls code from GitHub repository.
  2. Build: Builds the Docker image for the Flask app.
  3. Test: Runs unit tests to ensure app functionality.
  4. Deploy: Deploys the Docker container to localhost.
This pipeline automates building, testing, and deploying a Python Flask app using Docker containers.
*/

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

        stage('Build') {
            steps {
                echo "Building Docker image"
                bat "docker build --platform=linux/amd64 -t task-tracker ."
            }
        }

        stage('Tests') {
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
