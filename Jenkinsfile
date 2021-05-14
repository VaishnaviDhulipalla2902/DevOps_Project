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
        stage('Step 2: Build'){
            steps{
                sh 'pip3 install --upgrade -r requirements.txt'
            }
        }
        stage('Step 3: Testing'){
            steps{
                sh 'pip3 install coverage'
                sh 'coverage run ./manage.py test'
            }
        }
        stage('Step 4: Build docker image') {
            steps {
                script {
                    docker_image = docker.build "vaishnavi2902/personal_library:latest"
                }
            }
        }
        stage('Step 5: Push docker image to hub') {
            steps {
                script {
                    docker.withRegistry('', 'docker') {
                        docker_image.push()
                    }
                }
            }
        }
        stage('Step 6: Ansible Deployment'){
            steps{
                ansiblePlaybook becomeUser: null, 
                colorized: true,
                credentialsId: 'docker',
                installation: 'Ansible',
                disableHostKeyChecking: true, 
                inventory: 'deployment/inventory', 
                playbook: 'deployment/deploy.yml', 
                sudoUser: null  
            }          
        }       
    }
}