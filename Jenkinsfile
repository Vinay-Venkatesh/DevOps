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
            sh 'kubectl apply -f controller.json --token 11871835b3cda17d6ec49466c15a2ce3c2 --server https://160371ABE9DB6F87DAC55937D2740CC5.gr7.us-east-1.eks.amazonaws.com'
        }
      }
    }
}
