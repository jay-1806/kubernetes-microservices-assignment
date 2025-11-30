# Architecture AFTER - Microservices Application

## Diagram:
```
┌─────────────────────────────────────┐
│         User Browser                │
└──────────────┬──────────────────────┘
               │
               │ HTTP Request
               │
               ▼
┌─────────────────────────────────────┐
│   Frontend Service                  │
│   (frontend-service)                │
│   Port: 5000                        │
│   Type: NodePort (30001)            │
└──────────────┬──────────────────────┘
               │
               │ Routes to
               │
               ▼
┌─────────────────────────────────────┐
│   Frontend Deployment               │
│   Replicas: 2                       │
│                                     │
│   ┌─────────────────────┐          │
│   │  Pod 1: Frontend    │          │
│   │  (app-frontend.py)  │──┐       │
│   │  Port: 5000         │  │       │
│   └─────────────────────┘  │       │
│                            │       │
│   ┌─────────────────────┐  │       │
│   │  Pod 2: Frontend    │  │       │
│   │  (app-frontend.py)  │──┤       │
│   │  Port: 5000         │  │       │
│   └─────────────────────┘  │       │
└────────────────────────────┼───────┘
                             │
                             │ Internal API Call
                             │ http://backend-service:5001/api/message
                             │
                             ▼
┌─────────────────────────────────────┐
│   Backend Service                   │
│   (backend-service)                 │
│   Port: 5001                        │
│   Type: ClusterIP (Internal)        │
└──────────────┬──────────────────────┘
               │
               │ Routes to
               │
               ▼
┌─────────────────────────────────────┐
│   Backend Deployment                │
│   Replicas: 2                       │
│                                     │
│   ┌─────────────────────┐          │
│   │  Pod 1: Backend     │          │
│   │  (app-backend.py)   │          │
│   │  Port: 5001         │          │
│   └─────────────────────┘          │
│                                     │
│   ┌─────────────────────┐          │
│   │  Pod 2: Backend     │          │
│   │  (app-backend.py)   │          │
│   │  Port: 5001         │          │
│   └─────────────────────┘          │
└─────────────────────────────────────┘
```

## Description:

**Microservices Architecture:**
- Application split into 2 independent services
- Each service has its own deployment and service
- Services communicate via internal APIs
- Better scalability and maintainability

**Components:**

1. **Frontend Microservice:**
   - Handles user interface
   - Calls backend for data
   - 2 replicas for availability
   - Exposed externally via NodePort

2. **Backend Microservice:**
   - Provides API endpoints
   - Returns data/messages
   - 2 replicas for availability
   - Only accessible internally (ClusterIP)

**Benefits:**
- Independent scaling of frontend/backend
- Easier to update individual services
- Better separation of concerns
- Can use different technologies for each service