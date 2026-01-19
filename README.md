### Cloud-native retail analytics platform for supplier insights.  
    
>Built with ***FastAPI, GCP, Kubernetes, and BigQuery***.

> ## Architecture Overview

### Why FastAPI
- Chosen for building high-performance, cloud-native REST APIs
- Strong request/response validation using Pydantic
- Native async support suitable for data-intensive workloads
- Well-suited for microservices deployed on Kubernetes

### Primary Users
- Retail suppliers accessing sales and inventory analytics
- Internal merchant and analytics teams

### Problem Statement
- Retail data is large, fragmented, and difficult to analyze in real time
- Suppliers need timely insights into sales trends and inventory levels
- This platform centralizes retail data and exposes analytics via secure APIs

### High-Level Architecture
- API Layer: FastAPI-based REST services
- Auth Layer: Authentication and authorization
- Data Layer:
  - Postgres for transactional data
  - Redis for caching
  - BigQuery for analytics
- Analytics Layer: Aggregation and reporting services
- Infrastructure: GCP and Kubernetes

### Data Flow
1. Data is ingested via REST APIs
2. Stored in Postgres
3. Aggregated data is pushed to BigQuery
4. Cached analytics are stored in Redis
5. Insights are served via APIs

### Scalability & Reliability
- Stateless services enable horizontal scaling
- Caching improves performance
- Containerized cloud-native deployment
