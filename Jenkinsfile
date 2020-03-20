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
            sh 'sudo kubectl --kubeconfig /home/ubuntu/.kube/config apply -f controller.json'
            sh 'sudo kubectl --kubeconfig /home/ubuntu/.kube/config apply -f service.json'
        }
      }
    }
}
