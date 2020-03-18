# DevOps
This repository explains practical implementation of DevOps practice in an organisation 

# Tools Used:
1. GitHub   - Code Repository
2. Jenkins - CI/CD
3. AWS EKS  - Container Orchestration
4. AWS ECR  - Image Repository

#Plugins Used:
1. Blue Ocean Plugin
2. AWS ECR Plugin
3. Docker Pipeline Plugin

In Groovy Script:
docker.withRegistry('https://xxxxx.dkr.ecr.us-east-1.amazonaws.com', 'ecr:us-east-1:creds')
The name creds is the credentails that you configured in Jenkins Global Configuration with AWS_ACCESS_KEY and AWS_SECRET_KEY
