def build_number = env.BUILD_NUMBER

def testApp() {
    echo "testing application..."
    sh "pytest tests/"
    }

def buildApp() {
    withCredentials([usernamePassword(credentialsId: 'docker-credentials', passwordVariable: 'USERNAME', usernameVariable: 'PWD')]) {
        echo "building application..."
        sh "echo ${PWD} | docker login -u ${USERNAME} --password-stdin"
        sh "docker build -t sintia:1.0.${build_number} ."
        }
    }

def deployApp() {
    echo "deploying app ..."
    }