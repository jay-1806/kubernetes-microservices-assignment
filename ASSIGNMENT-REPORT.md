# Kubernetes Microservices Assignment

**Student Name:** Jay Vithlani  
**Assignment:** Kubernetes Assignment

---

## Table of Contents
1. Introduction
2. Architecture Before - Monolithic Application
3. Architecture After - Microservices Application
4. Deployment Steps
5. Kubernetes Resources
6. Screenshots
7. Conclusion

---

## 1. Introduction

This assignment demonstrates the deployment of a containerized application on Kubernetes, followed by breaking it down into a microservices architecture.

**Technologies Used:**
- Docker
- Kubernetes (kind cluster)
- Python Flask
- kubectl

---

## 2. Architecture BEFORE - Monolithic Application

See: `architecture-before.md` for detailed diagram

**Summary:**
- Single Flask application
- 3 replicas for high availability
- Simple monolithic structure
- All code in one file (app.py)

**Files:**
- `app.py` - Main application
- `Dockerfile` - Container image
- `deployment.yaml` - Kubernetes deployment
- `service.yaml` - Kubernetes service

---

## 3. Architecture AFTER - Microservices Application

See: `architecture-after.md` for detailed diagram

**Summary:**
- Split into Frontend and Backend microservices
- Frontend: Handles UI (2 replicas)
- Backend: Provides API (2 replicas)
- Services communicate via internal APIs

**Files:**

**Frontend:**
- `app-frontend.py` - Frontend application
- `Dockerfile.frontend` - Frontend container
- `frontend-deployment.yaml` - Frontend Kubernetes deployment
- `frontend-service.yaml` - Frontend Kubernetes service

**Backend:**
- `app-backend.py` - Backend API
- `Dockerfile.backend` - Backend container
- `backend-deployment.yaml` - Backend Kubernetes deployment
- `backend-service.yaml` - Backend Kubernetes service

---

## 4. Deployment Steps

### Step 1: Created Docker Images
```bash
docker build -t my-simple-app .
docker build -f Dockerfile.frontend -t my-app-frontend .
docker build -f Dockerfile.backend -t my-app-backend .
```

### Step 2: Created Kubernetes Cluster
```bash
kind create cluster --name my-cluster
```

### Step 3: Loaded Images into Cluster
```bash
kind load docker-image my-simple-app --name my-cluster
kind load docker-image my-app-frontend --name my-cluster
kind load docker-image my-app-backend --name my-cluster
```

### Step 4: Deployed to Kubernetes
```bash
# Monolithic app
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

# Microservices
kubectl apply -f backend-deployment.yaml
kubectl apply -f backend-service.yaml
kubectl apply -f frontend-deployment.yaml
kubectl apply -f frontend-service.yaml
```

---

## 5. Kubernetes Resources

### Monolithic Application:
- Deployment: my-app-deployment (3 replicas)
- Service: my-app-service (NodePort 30000)

### Microservices Application:
- Backend Deployment: backend-deployment (2 replicas)
- Backend Service: backend-service (ClusterIP)
- Frontend Deployment: frontend-deployment (2 replicas)
- Frontend Service: frontend-service (NodePort 30001)

---

## 6. Screenshots

1. **pods-running.png** - Monolithic app pods
2. **services-running.png** - Monolithic app services
3. **k8s-all-resources.png** - All monolithic resources
4. **app-running.png** - Monolithic app in browser
5. **microservices-app-running.png** - Microservices app in browser
6. **microservices-pods.png** - Microservices pods
7. **microservices-services.png** - Microservices services
8. **microservices-all-resources.png** - All microservices resources

---

## 7. Conclusion

Successfully:
- Containerized application using Docker
- Deployed monolithic app to Kubernetes
- Broke down application into microservices
- Deployed microservices architecture on Kubernetes
- Demonstrated communication between services

**Key Learnings:**
- Kubernetes orchestration
- Microservices architecture benefits
- Service-to-service communication
- Container deployment at scale

---

## GitHub Repository

Repository Link: [To be added]

Contains:
- All source code files
- All Dockerfile configurations
- All Kubernetes YAML files
- Architecture diagrams
- This documentation