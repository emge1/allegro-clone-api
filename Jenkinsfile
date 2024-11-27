pipeline {
    agent {
        docker { image 'python:3.11.7' }
    }
    environment {
        COMPOSE_FILE = "docker-compose.yml"
        REPO_URL = "https://github.com/emge1/allegro-clone-api.git"
        REPO_BRANCH = "main"
    }
    stages {
        stage('Checkout Code') {
            steps {
                git branch: "${REPO_BRANCH}", url: "${REPO_URL}"
            }
        }

        stage('Start Services with Docker Compose') {
            steps {
                sh "docker-compose down || true"
                sh "docker-compose up -d web jenkins"
            }
        }

        stage('Restore Cache') {
            steps {
                echo "Restore cache - optional setup for dependencies"
            }
        }

        stage('Run Tests') {
            steps {
                sh """
                    . ${VENV_DIR}/bin/activate
                    pytest --junitxml=test-reports/results.xml
                """
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                }
            }
        }

        stage('Store Artifacts') {
            steps {
                archiveArtifacts artifacts: 'test-reports/**', allowEmptyArchive: true
            }
        }
    }
    post {
        always {
            sh "docker-compose down || true"
            cleanWs()
        }
        success {
            echo 'Pipeline succesfully completed'
        }
        failure {
            echo 'Pipeline unsuccessfull'
    }
}
