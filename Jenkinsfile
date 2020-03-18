pipeline {
  agent any
  stages {
    stage('Lint Docker') {
      steps{
        sh 'hadolint Dockerfile'
      }
    }

    stage('Docker build'){
      steps{
        script{
          docker.build('python-app')
        }
      }
    }

    stage ('Docker push'){
      steps{
        script{
          docker.withRegistry('https://920055073134.dkr.ecr.us-east-1.amazonaws.com', 'ecr:us-east-1:python-app-ecr-credentials'){
          docker.image('python-app').push('latest')
          }
        }
      }
    }
  }
}
