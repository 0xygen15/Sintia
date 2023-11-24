#!/usr/bin/env groovy

pipeline {
    agent any
    stages {
        stage("test") {
            steps {
                script {
                    echo "testing application..."
                    sh "pytest tests/"
                }
            }
        }
        stage("build") {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'docker-credentials', passwordVariable: 'USERNAME', usernameVariable: 'PWD')]) {
                    echo "building application..."
                    sh "echo ${PWD} | docker login -u ${USERNAME} --password-stdin"
                    sh "docker build -t sintia:1.0.${BUILD_NUMBER} ."
                        }
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