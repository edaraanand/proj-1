pipeline {
    agent any

    environment {
        MODEL_NAME = "my-ml-model"
        DOCKER_IMAGE = "myregistry.com/ml-model:${BUILD_NUMBER}"
        DOCKER_CREDENTIALS_ID = "docker-credentials"
    }

    stages {
        stage('Checkout Code') {
            steps {
                git url: 'https://github.com/your-org/ml-project.git', branch: 'main'
            }
        }

        stage('Setup Environment') {
            steps {
                sh 'python -m venv venv'
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Data Preprocessing') {
            steps {
                sh '. venv/bin/activate && python scripts/preprocess_data.py'
            }
        }

        stage('Train Model') {
            steps {
                sh '. venv/bin/activate && python scripts/train_model.py'
            }
        }

        stage('Evaluate Model') {
            steps {
                sh '. venv/bin/activate && python scripts/evaluate_model.py'
            }
        }

        stage('Save Model Artifact') {
            steps {
                archiveArtifacts artifacts: 'models/*.pkl', fingerprint: true
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${DOCKER_IMAGE}", "-f Dockerfile .")
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('https://myregistry.com', "${DOCKER_CREDENTIALS_ID}") {
                        docker.image("${DOCKER_IMAGE}").push()
                    }
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f k8s/deployment.yaml'
            }
        }

        stage('Notify') {
            steps {
                echo "Deployment completed successfully. Model is live."
                // Optional: Integrate with Slack/Email
            }
        }
    }

    post {
        failure {
            echo "Pipeline failed. Investigate the logs."
            // Optional: Send notification on failure
        }
    }
}
