pipeline {
    agent any

    environment {
        MY_ENV = 'This is a test environment variable'
    }

    options {
        timeout(time: 10, unit: 'MINUTES')
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Lalit1202/test.git'
            }
        }

        stage('Build') {
            steps {
                echo "Building the code..."
                echo "Env var: ${env.MY_ENV}"
            }
        }

        stage('Test') {
            steps {
                echo "Running tests..."
                sh 'echo Testing...'
            }
        }

        stage('Deploy') {
            steps {
                echo "Deploying application..."
            }
        }
    }

    post {
        success {
            echo 'Build and deploy succeeded!'
        }
        failure {
            echo 'Build failed. Check logs.'
        }
    }
}
