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
          docker.withRegistry('https://920055073134.dkr.ecr.us-east-1.amazonaws.com', 'ecr:us-east-1:Vinay'){
          docker.image('python-app').push('latest')
          }
        }
      }
    }
    stage('Docker deploy'){
      steps {
         withKubeConfig([credentialsId: 'Vinay', serverUrl: 'https://160371ABE9DB6F87DAC55937D2740CC5.gr7.us-east-1.eks.amazonaws.com']) {
          sh 'kubectl apply -f controller.json'
        }
      }
    }
  }
}
