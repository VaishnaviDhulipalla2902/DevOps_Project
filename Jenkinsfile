pipeline{
    environment{
        docker_image = ""
    }
    agent any
    stages{
        stage('Step 1: Git Clone'){
            steps{
                git branch: 'main', url: 'https://github.com/VaishnaviDhulipalla2902/DevOps_Project.git'
            }
        }   
    }
}