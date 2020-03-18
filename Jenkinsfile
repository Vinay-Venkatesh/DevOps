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
        sh 'docker build -t python-app .'
        sh 'docker build -t python-app .'
        sh 'docker tag python-app:latest 920055073134.dkr.ecr.us-east-1.amazonaws.com/python-app:latest'
        sh 'docker push 920055073134.dkr.ecr.us-east-1.amazonaws.com/python-app:latest'
      }
    }

  }
}
