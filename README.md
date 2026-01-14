
### localhost
```bash
docker-compose down
docker-compose build redis
docker-compose up
```

### k8s
```bash
minikube start
kubectl apply -f k8s/
kubectl get pods
kubectl port-forward pod/<pod name> 8080:8000
kubectl port-forward service/service-b 8000:8000
```

### open shift
```bash
oc new-app jacobsun211/image-service-a:v1 --name=service-a
oc new-app jacobsun211/image-service-b:latest --name=service-b
oc new-app redis:alpine --name=redis
oc expose service/service-a

oc get pods
oc get route service-a -o jsonpath='{.spec.host}'
```
>>>>>>> 7529ab18be6184405884d09a7f8680593719610b
