pipeline {
    agent any
    tools {
        python 'Python3'  // Must match the Name you configured
    }
    environment {
        PROJECT = 'travel-memory-backend'
    }
    stages {
        stage('Build') {
            steps {
                dir('backend') {
                    sh 'python -m pip install --upgrade pip'
                    sh 'python -m pip install -r requirements.txt'
                }
            }
        }
        stage('Test') {
            steps {
                dir('backend') {
                    sh 'python -m pytest --junitxml=test-results.xml -v'
                }
            }
            post {
                always {
                    junit 'backend/test-results.xml'
                }
            }
        }
        stage('Deploy to Staging') {
            when {
                expression { currentBuild.result == null || currentBuild.result == 'SUCCESS' }
            }
            steps {
                dir('backend') {
                    sh 'echo "Deploying to staging environment..."'
                    // Add deployment commands here
                }
            }
        }
    }
    post {
        failure {
            emailext (
                subject: "FAILED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'",
                body: "Check console output at ${env.BUILD_URL}",
                to: "thekartikbaliyan12@gmail.com"
            )
        }
        success {
            emailext (
                subject: "SUCCESS: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'",
                body: "Build successful!",
                to: "thekartikbaliyan12@gmail.com"
            )
        }
    }
}
