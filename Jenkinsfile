pipeline {
    agent {
        label 'ubuntu-agent'
    }

    stages {
        stage('Build Docker Image') {
            steps {
                dir('service1') {
                    sh 'docker build -t service1:1.0 .'
                }
            }
        }
    }
}