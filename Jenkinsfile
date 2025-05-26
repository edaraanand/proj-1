pipeline {
    // agent any

    // agent { label 'python-agent' }

    agent {
        docker {
            image 'python:3.10'  // Official Python image from Docker Hub
            args '-u root'       // Run as root if needed
        }
    }

    environment {
        MODEL_NAME = "model"
        DOCKER_IMAGE = "edaraanand/proj-1:${BUILD_NUMBER}"
        DOCKER_CREDENTIALS_ID = "docker-credentials"
    }

    stages {
        stage('Checkout Code') {
            steps {
                git url: 'git@github.com:edaraanand/proj-1.git', branch: 'master'
            }
        }

        stage('Check Python') {
            steps {
                sh 'python --version'
                sh 'python3 -m venv venv'
            }
        }
    
        stage('Setup Environment') {
            steps {
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate && pip3 install -r requirements.txt'
            }
        }

        stage('Data Preprocessing') {
            steps {
                sh '. venv/bin/activate && python3 scripts/preprocess_data.py'
            }
        }

        stage('Train Model') {
            steps {
                sh '. venv/bin/activate && python3 scripts/train_model.py'
            }
        }

        stage('Evaluate Model') {
            steps {
                sh '. venv/bin/activate && python3 scripts/evaluate_model.py'
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
                    docker.withRegistry('https://hub.docker.com', "${DOCKER_CREDENTIALS_ID}") {
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
