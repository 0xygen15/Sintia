#!/usr/bin/env groovy

def gv

pipeline {
    agent any
    stages {
        stage("init") {
            steps {
                gv = load "script.groovy"
            }
        }
        stage("test") {
            steps {
                script {
                    gv.testApp()
                }
            }
        }
        stage("build") {
            steps {
                script {
                    gv.testApp()
                }
            }
        }
    }

}