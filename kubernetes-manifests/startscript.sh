#launch minikube and enable ingress
minikube start --driver="docker"
minikube addons enable ingress

#prepare storage
kubectl apply -f https://raw.githubusercontent.com/rancher/local-path-provisioner/master/deploy/local-path-storage.yaml
kubectl patch storageclass local-path -p '{"metadata": {"annotations":{"storageclass.kubernetes.io/is-default-class":"true"}}}'

#create pods
kubectl apply -f "*.yaml"

echo ""