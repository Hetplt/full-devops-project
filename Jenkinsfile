pipeline {

    agent any

    environment {
        DOCKER_IMAGE = "hetptl/full-devops-backend"
        DOCKER_TAG = "v1"
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                url: 'https://github.com/Hetplt/full-devops-project.git'
            }
        }

        stage('Docker Build') {
            steps {
                sh '''
                docker build -t $DOCKER_IMAGE:$DOCKER_TAG ./app
                '''
            }
        }

        stage('Docker Login') {
            steps {
                sh '''
                echo $DOCKER_PASSWORD | docker login \
                -u $DOCKER_USERNAME \
                --password-stdin
                '''
            }
        }

        stage('Docker Push') {
            steps {
                sh '''
                docker push $DOCKER_IMAGE:$DOCKER_TAG
                '''
            }
        }

    }
}
