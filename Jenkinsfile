pipeline {
  agent any
  stages {
    stage('Lint Docker') {
      steps {
        sh 'hadolint Dockerfile'
      }
    }

    stage('docker build and push') {
      steps {
        sh 'aws ecr get-login-password --region us-east-1 | sudo docker login --username AWS --password-stdin 920055073134.dkr.ecr.us-east-1.amazonaws.com/python-app'
        sh 'sudo docker build -t python-app .'
        sh 'sudo docker build -t python-app .'
        sh 'sudo docker tag python-app:latest 920055073134.dkr.ecr.us-east-1.amazonaws.com/python-app:latest'
        sh 'sudo docker push 920055073134.dkr.ecr.us-east-1.amazonaws.com/python-app:latest'
      }
    }

  }
}
