#launch minikube and enable ingress
minikube start --driver="docker"
minikube addons enable ingress

#prepare storage (in order for Stateful containers to be working)
kubectl apply -f https://raw.githubusercontent.com/rancher/local-path-provisioner/master/deploy/local-path-storage.yaml
kubectl patch storageclass local-path -p '{"metadata": {"annotations":{"storageclass.kubernetes.io/is-default-class":"true"}}}'

#create pods
cd kubernetes-manifests
kubectl apply -f ingress.yaml
kubectl apply -f postgres-deployment.yaml
kubectl apply -f pgadmin-deployment.yaml
kubectl apply -f sintia-app-deployment.yaml
kubectl apply -f prometheus-deployment.yaml