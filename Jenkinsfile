pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/MagnusEquus/pytest_practice.git'
            }
        }
        stage('Install dependencies') {
            steps {
                sh 'python -m venv venv'
                sh './venv/bin/pip install -r requirements.txt'
            }
        }
        stage('Run tests') {
            steps {
                sh './venv/bin/pytest --maxfail=1 --disable-warnings'
            }
        }
    }
}