pipeline {
    agent {
        label 'ubuntu-agent'
    }

    parameters {
        choice(
            name: 'SERVICE',
            choices: ['service1', 'service2'],
            description: 'Select the service to deploy'
        )
    }

    stages {
        stage('Build Docker Image') {
            steps {
                dir("${params.SERVICE}") {
                    sh "docker build -t ${params.SERVICE}:1.0 ."
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

                        docker tag "${SERVICE}:1.0" "$DOCKER_USER/${SERVICE}:1.0"
                        docker push "$DOCKER_USER/${SERVICE}:1.0"

                        docker logout
                    '''
                }
            }
        }

        // Mission 2 - Step 3: Deployment with Ansible
        // Temporarily disabled until Step 2 is completed.

        /*
        stage('Deploy with Ansible') {
            steps {
                sh 'ansible-playbook -i "localhost," -c local deploy-playbook.yml'
            }
        }
        */
    }
}