pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/MagnusEquus/pytest_practice.git'
            }
        }
        stage('Install dependencies') {
            steps {
                bat 'python -m venv venv'
                bat './venv/bin/pip install -r requirements.txt'
            }
        }
        stage('Run tests') {
            steps {
                bat './venv/bin/pytest --maxfail=1 --disable-warnings'
            }
        }
    }
}