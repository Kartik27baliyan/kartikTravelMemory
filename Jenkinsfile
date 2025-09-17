

pipeline {
    agent any
    stages {
        stage('Diagnose Python') {
            steps {
                sh '''
                    echo "Checking Python installations..."
                    which python || echo "python not found"
                    which python3 || echo "python3 not found"
                    which py || echo "py not found"
                    ls /usr/bin/python* || echo "No Python in /usr/bin/"
                    echo "PATH is: $PATH"
                '''
            }
        }
        pipeline {
    agent any
    environment {
        PROJECT = 'travel-memory-backend'
    }
    stages {
        stage('Build') {
            steps {
                dir('backend') {
                    sh 'python -m pip install --upgrade pip'
                    sh 'pip install -r requirements.txt'
                }
            }
        }
        stage('Test') {
            steps {
                dir('backend') {
                    sh 'pytest --junitxml=test-results.xml -v'
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
                to: "your-email@example.com"
            )
        }
        success {
            emailext (
                subject: "SUCCESS: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'",
                body: "Build successful!",
                to: "your-email@example.com"
            )
        }
    }
}
    }
}
