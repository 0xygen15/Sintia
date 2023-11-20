def testApp() {
    echo "testing application..."
    sh "pytest tests/"
    }

def buildApp() {
    echo "building application..."
    sh "docker build -t sintia:1.0 ."
    }