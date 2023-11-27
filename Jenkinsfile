#!/usr/bin/env groovy

pipeline {
    agent any
    stages {
        stage("test") {
            steps {
                script {
                    sh 'pip install pytest'
                    sh 'pytest tests/'
                }
            }
        }

        stage("build") {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'docker-credentials', passwordVariable: 'USERNAME', usernameVariable: 'PASSWORD')]) {
                    echo "building application..."
                    sh 'echo #{PASSWORD} | docker login -u ${USERNAME} --password-stdin'
                    sh 'docker build -t sintia:1.0.${BUILD_NUMBER} .'
                    }
                }
            }
        }

        stage("deploy") {
            steps {
                script {
                    echo "deploying app ..."
                }
            }
        }   
    }
        
}
