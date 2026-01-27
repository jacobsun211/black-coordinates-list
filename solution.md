# Quick OpenShift Deployment Guide

## Step 1: Build & Push Docker Images
```bash
cd service-a
docker build -t jacobsun211/image-service-a:v1 -f app/Dockerfile .
docker push jacobsun211/image-service-a:v1

cd ../service-b
docker build -t jacobsun211/image-service-b:latest -f app/Dockerfile .
docker push jacobsun211/image-service-b:latest
```

## Step 2: Deploy to OpenShift
```bash

--------------------------------------------
# try this first
oc login --token=sha256~eCPcESwQOBa_UJ9orXLJ4zAE_0QtWoimDJ-HS1HALxE --server=https://api.rm1.0a51.p1.openshiftapps.com:6443
--------------------------------------------
# if not working do this !
oc login <your-token>


oc new-app jacobsun211/image-service-a:v1 --name=service-a
oc new-app jacobsun211/image-service-b:latest --name=service-b
oc new-app redis:alpine --name=redis
```

## Step 3: Configure Services
```bash
oc delete service service-a
oc expose deployment service-a --port=8000 --target-port=8000

oc delete service service-b
oc expose deployment service-b --port=8000 --target-port=8000
```

## Step 4: Expose to Internet
```bash
# oc create route edge service-a --service=service-a --port=8000
oc get route service-a 
```

Open that URL + `/docs` in browser. Done! 

***

## Problems We Had & Fixes

| Problem | Cause | Fix |
|---------|-------|-----|
| **App not available on public URL** | Route pointing to wrong port (8080 instead of 8000) | Fixed Dockerfile: changed `EXPOSE 8080` to `EXPOSE 8000`, rebuilt image, restarted deployment |
| **Service had no port mapping** | `oc new-app` created Service but didn't expose correct ports | Deleted Service, recreated with `oc expose deployment --port=8000 --target-port=8000` |
| **Port mismatch** | Dockerfile exposed 8080 but app ran on 8000 (mismatch) | Updated Dockerfile to match: `EXPOSE 8000` |
| **Docker build failed** | Dockerfile was in wrong folder (`service-a/app/` not `service-a/`) | Used `-f app/Dockerfile` flag to specify path explicitly |
| **Old image still running** | Pod using cached image without fix | Restarted deployment: `oc rollout restart deployment/service-a` to pull new image |

**Key lesson:** Always match ports in three places:
1. **Dockerfile EXPOSE** 
2. **App uvicorn port**
3. **Service/Route port mapping**

When they don't match, nothing works! 🎯


