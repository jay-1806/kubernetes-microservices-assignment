# Architecture BEFORE - Monolithic Application

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
│     Kubernetes Service              │
│     (my-app-service)                │
│     Port: 5000                      │
└──────────────┬──────────────────────┘
               │
               │ Load Balances to
               │
               ▼
┌─────────────────────────────────────┐
│   Kubernetes Deployment             │
│   (my-app-deployment)               │
│   Replicas: 3                       │
│                                     │
│   ┌─────────────────────┐          │
│   │  Pod 1: my-app      │          │
│   │  (Flask App)        │          │
│   │  Port: 5000         │          │
│   └─────────────────────┘          │
│                                     │
│   ┌─────────────────────┐          │
│   │  Pod 2: my-app      │          │
│   │  (Flask App)        │          │
│   │  Port: 5000         │          │
│   └─────────────────────┘          │
│                                     │
│   ┌─────────────────────┐          │
│   │  Pod 3: my-app      │          │
│   │  (Flask App)        │          │
│   │  Port: 5000         │          │
│   └─────────────────────┘          │
└─────────────────────────────────────┘
```

## Description:

**Monolithic Architecture:**
- Single application container
- All functionality in one codebase (app.py)
- 3 replicas for high availability
- Simple, but all components tightly coupled

**Components:**
1. **Application**: Single Flask app serving web pages
2. **Deployment**: 3 identical pods running the same app
3. **Service**: Exposes the app on NodePort 30000