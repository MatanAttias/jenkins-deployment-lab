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

        stage('Deploy Docker Container') {
            steps{
                sh '''
                    docker rm -f service1 || true
                    docker run -d --name service1 -p 5000:5000 service1:1.1
                    '''
            }
        }
    }
}