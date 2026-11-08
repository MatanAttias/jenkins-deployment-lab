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

        stage('Tag and Push to DockerHub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-credentials',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_TOKEN'
                )]) {
                    sh '''
                        set +x
                        echo "$DOCKER_TOKEN" | docker login -u "$DOCKER_USER" --password-stdin
                        docker tag service1:1.0 "$DOCKER_USER/service1:1.0"
                        docker push "$DOCKER_USER/service1:1.0"
                        docker logout
                    '''
                }
            }
        }
    }
}