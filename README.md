# Simple Task Manager - Cloud-Native Deployment on AWS EKS

A production-ready FastAPI application deployed on Amazon EKS (Elastic Kubernetes Service) with full CI/CD automation using GitHub Actions and Infrastructure as Code using Terraform.

## 📋 Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Tech Stack](#tech-stack)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [Infrastructure Setup](#infrastructure-setup)
- [Application Deployment](#application-deployment)
- [CI/CD Pipeline](#cicd-pipeline)
- [API Documentation](#api-documentation)
- [Monitoring and Verification](#monitoring-and-verification)
- [Screenshots](#screenshots)
- [Troubleshooting](#troubleshooting)
- [Future Enhancements](#future-enhancements)
- [License](#license)

---

## 🎯 Overview

This project demonstrates a complete DevOps workflow for deploying a containerized Python FastAPI application to AWS EKS. It showcases infrastructure provisioning with Terraform, container orchestration with Kubernetes, and automated CI/CD pipelines with GitHub Actions.

### What This Project Does

- **Infrastructure as Code**: Provisions AWS VPC, EKS cluster, and managed node groups using Terraform
- **Containerization**: Packages a FastAPI application into Docker containers
- **Orchestration**: Deploys and manages containers on Kubernetes (EKS)
- **Automation**: Implements CI/CD pipelines for automated builds and deployments
- **High Availability**: Uses LoadBalancer service for public access and rolling updates for zero-downtime deployments

---

## 🏗️ Architecture

### High-Level Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                         GitHub Repository                        │
│  ┌────────────┐  ┌────────────┐  ┌────────────┐                │
│  │   Code     │  │ Terraform  │  │   K8s      │                │
│  │  (FastAPI) │  │  Configs   │  │ Manifests  │                │
│  └────────────┘  └────────────┘  └────────────┘                │
└─────────────────────────────────────────────────────────────────┘
                            │
                            │ Git Push (main branch)
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                     GitHub Actions (CI/CD)                       │
│  ┌──────────────────────┐      ┌─────────────────────────┐     │
│  │   CI Pipeline        │      │    CD Pipeline          │     │
│  │  - Build Docker      │──────▶  - Update kubeconfig   │     │
│  │  - Push to Registry  │      │  - Deploy to EKS        │     │
│  └──────────────────────┘      └─────────────────────────┘     │
└─────────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                      AWS Cloud (eu-north-1)                      │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │                      VPC (10.0.0.0/16)                    │  │
│  │  ┌─────────────────────────────────────────────────────┐  │  │
│  │  │              EKS Cluster (simple-app-eks)           │  │  │
│  │  │  ┌──────────────┐          ┌──────────────┐        │  │  │
│  │  │  │  Node Group  │          │  Node Group  │        │  │  │
│  │  │  │  (t3.small)  │          │  (t3.small)  │        │  │  │
│  │  │  │              │          │              │        │  │  │
│  │  │  │  ┌────────┐  │          │  ┌────────┐  │        │  │  │
│  │  │  │  │  Pod   │  │          │  │  Pod   │  │        │  │  │
│  │  │  │  │FastAPI │  │          │  │        │  │        │  │  │
│  │  │  │  └────────┘  │          │  └────────┘  │        │  │  │
│  │  │  └──────────────┘          └──────────────┘        │  │  │
│  │  └─────────────────────────────────────────────────────┘  │  │
│  │                            │                               │  │
│  │                            ▼                               │  │
│  │                  ┌──────────────────┐                      │  │
│  │                  │  Load Balancer   │                      │  │
│  │                  │   (AWS ELB)      │                      │  │
│  │                  └──────────────────┘                      │  │
│  └───────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
                            │
                            ▼
                    ┌───────────────┐
                    │   End Users   │
                    │  (Internet)   │
                    └───────────────┘
```

### Component Breakdown

1. **VPC Layer**: Custom VPC with public subnets across multiple availability zones
2. **EKS Control Plane**: Managed Kubernetes control plane by AWS
3. **Worker Nodes**: EC2 instances (t3.micro) running as Kubernetes nodes
4. **Application Pods**: FastAPI containers running the task manager application
5. **Load Balancer**: AWS ELB distributing traffic to healthy pods
6. **CI/CD**: GitHub Actions automating build and deployment

---

## 🛠️ Tech Stack

### Infrastructure & Cloud
- **Cloud Provider**: AWS (Amazon Web Services)
- **Region**: eu-north-1 (Stockholm)
- **Container Orchestration**: Kubernetes (via Amazon EKS)
- **Infrastructure as Code**: Terraform v1.5+
- **Networking**: AWS VPC, Subnets, Internet Gateway

### Application
- **Programming Language**: Python 3.12
- **Web Framework**: FastAPI 0.129.0
- **ASGI Server**: Uvicorn
- **Data Validation**: Pydantic

### DevOps & Automation
- **CI/CD**: GitHub Actions
- **Containerization**: Docker
- **Container Registry**: Docker Hub
- **Version Control**: Git & GitHub

### Monitoring & Management
- **Cluster Management**: kubectl
- **AWS CLI**: For EKS and AWS resource management

---

## ✨ Features

### Application Features
- ✅ RESTful API for task management (Create, Read, Delete)
- ✅ Health check endpoint for monitoring
- ✅ Input validation using Pydantic models
- ✅ Fast, asynchronous request handling with FastAPI
- ✅ In-memory data storage (suitable for demonstration)

### Infrastructure Features
- ✅ Fully automated infrastructure provisioning
- ✅ Multi-AZ deployment for high availability
- ✅ Auto-scaling capable node groups
- ✅ Public Load Balancer for internet access
- ✅ Rolling updates for zero-downtime deployments

### DevOps Features
- ✅ Automated CI/CD pipeline
- ✅ Containerized application deployment
- ✅ Infrastructure as Code (reproducible environments)
- ✅ Kubernetes-native deployment strategies
- ✅ Health checks and readiness probes

---

## 📦 Prerequisites

Before you begin, ensure you have the following installed and configured:

### Required Software
- **Terraform** >= 1.5.0 ([Download](https://www.terraform.io/downloads))
- **kubectl** >= 1.28 ([Install Guide](https://kubernetes.io/docs/tasks/tools/))
- **AWS CLI** >= 2.0 ([Install Guide](https://aws.amazon.com/cli/))
- **Docker** >= 20.10 ([Download](https://www.docker.com/get-started))
- **Git** ([Download](https://git-scm.com/downloads))

### AWS Requirements
- Active AWS Account
- IAM User with the following permissions:
  - EKS Full Access
  - EC2 Full Access
  - VPC Full Access
  - IAM permissions to create roles and policies
- AWS credentials configured locally:
  ```bash
  aws configure
  ```

### GitHub Requirements
- GitHub account
- Repository with Actions enabled
- GitHub Secrets configured:
  - `AWS_ACCESS_KEY_ID`
  - `AWS_SECRET_ACCESS_KEY`
  - `AWS_REGION`
  - `EKS_CLUSTER_NAME`
  - `ECR_REPOSITORY` (if using ECR)

---

## 📁 Project Structure

```
Simple_Task_Manager/
├── .github/
│   └── workflows/
│       ├── pipeline.yml          # CI pipeline (build & push)
│       └── deploy.yml            # CD pipeline (deploy to EKS)
├── app/
│   ├── src/
│   │   ├── main.py              # FastAPI application
│   │   ├── models.py            # Pydantic models
│   │   └── database.py          # In-memory database
│   └── requirements.txt         # Python dependencies
├── k8s/
│   ├── deployment.yaml          # Kubernetes Deployment
│   └── service.yaml             # Kubernetes Service (LoadBalancer)
├── terraform/
│   ├── provider.tf              # Terraform & provider configuration
│   ├── vpc.tf                   # VPC resources
│   ├── eks.tf                   # EKS cluster configuration
│   ├── variables.tf             # Input variables
│   └── outputs.tf               # Output values
├── Dockerfile                   # Docker image definition
└── README.md                    # This file
```

---

## 🚀 Infrastructure Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/isirakatakumbura/Simple_Task_Manager.git
cd Simple_Task_Manager
```

### Step 2: Configure AWS Credentials

```bash
aws configure
# Enter your AWS Access Key ID
# Enter your AWS Secret Access Key
# Enter eu-north-1 as default region
```

### Step 3: Initialize Terraform

```bash
cd terraform
terraform init
```

**Expected Output:**
```
Initializing modules...
Initializing the backend...
Initializing provider plugins...
Terraform has been successfully initialized!
```

### Step 4: Review Infrastructure Plan

```bash
terraform plan
```

This will show you all the resources that will be created:
- VPC with public subnets in 2 availability zones
- EKS cluster with managed node groups
- Security groups and IAM roles
- Internet gateway and route tables

### Step 5: Provision Infrastructure

```bash
terraform apply
```

Type `yes` when prompted.

**⏱️ This takes approximately 10-15 minutes.**

### Step 6: Verify Infrastructure

```bash
# List EKS clusters
aws eks list-clusters --region eu-north-1

# Get cluster details
aws eks describe-cluster --name simple-app-eks --region eu-north-1

# View Terraform outputs
terraform output
```

---

## 🎯 Application Deployment

### Step 1: Configure kubectl

```bash
# Update kubeconfig to connect to EKS cluster
aws eks update-kubeconfig --region eu-north-1 --name simple-app-eks

# Verify connection
kubectl cluster-info
kubectl get nodes
```

**Expected Output:**
```
NAME                                          STATUS   ROLES    AGE   VERSION
ip-10-0-xxx-xxx.eu-north-1.compute.internal   Ready    <none>   5m    v1.29.x
ip-10-0-xxx-xxx.eu-north-1.compute.internal   Ready    <none>   5m    v1.29.x
```

### Step 2: Deploy Application

```bash
# Navigate to k8s directory
cd ../k8s

# Apply deployment
kubectl apply -f deployment.yaml

# Apply service
kubectl apply -f service.yaml
```

**Expected Output:**
```
deployment.apps/simple-app created
service/simple-app-service created
```

### Step 3: Monitor Deployment

```bash
# Watch pods come up
kubectl get pods --watch

# Check deployment status
kubectl get deployments

# Check service status
kubectl get services
```

Wait for the LoadBalancer to provision (2-3 minutes):

```bash
kubectl get service simple-app-service --watch
```

### Step 4: Get Application URL

```bash
# Get LoadBalancer URL
kubectl get service simple-app-service -o jsonpath='{.status.loadBalancer.ingress[0].hostname}'
```

Example output:
```
a5c4c91d91ae44e2ebe68e3d2ed44dd1-2067036851.eu-north-1.elb.amazonaws.com
```

### Step 5: Test Application

Open in your browser:
```
http://<LOADBALANCER-URL>/health
```

Should return:
```json
{"status":"ok"}
```
---

## ⚙️ CI/CD Pipeline

### Pipeline Overview

The project uses two GitHub Actions workflows:

1. **CI Pipeline** (`pipeline.yml`): Builds and pushes Docker images
2. **CD Pipeline** (`deploy.yml`): Deploys to EKS cluster

### CI Pipeline Flow

```
Code Push to main
    │
    ▼
Checkout Code
    │
    ▼
Configure AWS Credentials
    │
    ▼
Login to Docker Registry
    │
    ▼
Build Docker Image
    │
    ▼
Tag Image (with git SHA)
    │
    ▼
Push to Docker Hub
    │
    ▼
Trigger CD Pipeline
```

### CD Pipeline Flow

```
CI Pipeline Success
    │
    ▼
Checkout Code
    │
    ▼
Configure AWS Credentials
    │
    ▼
Update kubeconfig
    │
    ▼
Update Deployment Image
    │
    ▼
Apply Kubernetes Manifests
    │
    ▼
Verify Rollout Status
    │
    ▼
Deployment Complete
```

### Triggering a Deployment

```bash
# Make a code change
git add .
git commit -m "Update feature"
git push origin main

# Watch the pipeline
# Go to GitHub → Actions tab
```

### Pipeline Features

- ✅ Automated builds on every push to main
- ✅ Image tagging with git commit SHA for traceability
- ✅ Zero-downtime rolling updates
- ✅ Automatic rollback on deployment failure
- ✅ Health check verification before completion

---

## 📚 API Documentation

### Base URL

```
http://<LOADBALANCER-URL>
```

### Endpoints

#### 1. Health Check

**Endpoint:** `GET /health`

**Description:** Check if the service is running

**Response:**
```json
{
  "status": "ok"
}
```

**Example:**
```bash
curl http://<LOADBALANCER-URL>/health
```

---

#### 2. List All Tasks

**Endpoint:** `GET /tasks`

**Description:** Retrieve all tasks

**Response:**
```json
[
  {
    "id": 1,
    "title": "Complete project",
    "description": "Finish the EKS deployment",
    "completed": false
  }
]
```

**Example:**
```bash
curl http://<LOADBALANCER-URL>/tasks
```

---

#### 3. Create Task

**Endpoint:** `POST /tasks`

**Description:** Create a new task

**Request Body:**
```json
{
  "title": "Task title (min 3 characters)",
  "description": "Task description (optional)",
  "completed": false
}
```

**Response:**
```json
{
  "id": 1,
  "title": "Task title",
  "description": "Task description",
  "completed": false
}
```

**Example (Browser Console):**
```javascript
fetch('http://<LOADBALANCER-URL>/tasks', {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: JSON.stringify({
    title: 'My Task',
    description: 'Task details',
    completed: false
  })
}).then(r => r.json()).then(d => console.log(d))
```

---

#### 4. Get Single Task

**Endpoint:** `GET /tasks/{task_id}`

**Description:** Retrieve a specific task by ID

**Response:**
```json
{
  "id": 1,
  "title": "Task title",
  "description": "Task description",
  "completed": false
}
```

**Example:**
```bash
curl http://<LOADBALANCER-URL>/tasks/1
```

---

#### 5. Delete Task

**Endpoint:** `DELETE /tasks/{task_id}`

**Description:** Delete a task by ID

**Response:**
```json
{
  "message": "Task deleted"
}
```

**Example:**
```bash
curl -X DELETE http://<LOADBALANCER-URL>/tasks/1
```

---

### API Testing Examples

**Using Browser Console:**

1. Open `http://<LOADBALANCER-URL>/health`
2. Press F12 → Console
3. Type: `allow pasting`
4. Use the fetch examples above

---

## 🔍 Monitoring and Verification

### Check Cluster Health

```bash
# View cluster information
kubectl cluster-info

# Check node status
kubectl get nodes -o wide

# View all resources
kubectl get all -n default
```

### Check Application Health

```bash
# View pod logs
kubectl logs -l app=simple-app

# Follow logs in real-time
kubectl logs -f -l app=simple-app

# Check pod details
kubectl describe pod -l app=simple-app

# Check deployment status
kubectl rollout status deployment/simple-app
```

### Check Load Balancer

```bash
# Get LoadBalancer details
kubectl describe service simple-app-service

# Check LoadBalancer in AWS Console
# Go to: EC2 → Load Balancers
```

### View Infrastructure State

```bash
cd terraform

# View current state
terraform show

# List all resources
terraform state list

# View specific resource
terraform state show module.eks.aws_eks_cluster.this[0]
```

---

## 🔧 Troubleshooting

### Common Issues and Solutions

#### Issue 1: Pods Stuck in Pending

**Symptom:**
```bash
kubectl get pods
# STATUS: Pending
```

**Cause:** Insufficient resources (t3.samll too small)

**Solution:**
```bash
# Update terraform/eks.tf to use t3.small
instance_types = ["t3.small"]

# Apply changes
cd terraform
terraform apply
```

---

#### Issue 2: Image Pull Error

**Symptom:**
```bash
kubectl get pods
# STATUS: ImagePullBackOff
```

**Cause:** Invalid image name or private registry without credentials

**Solution:**
```bash
# Check deployment image
kubectl get deployment simple-app -o yaml | grep image:

# Should be: isirakatakumbura/simple-app:latest
# Fix in k8s/deployment.yaml and reapply
kubectl apply -f k8s/deployment.yaml
```

---

#### Issue 3: LoadBalancer Stuck in Pending

**Symptom:**
```bash
kubectl get service
# EXTERNAL-IP: <pending>
```

**Cause:** AWS LoadBalancer creation takes time or IAM permissions issue

**Solution:**
```bash
# Wait 3-5 minutes
# Check service events
kubectl describe service simple-app-service

# Verify AWS LoadBalancer is being created
aws elb describe-load-balancers --region eu-north-1
```

---

#### Issue 4: Cannot Access LoadBalancer URL

**Symptom:** Browser cannot resolve LoadBalancer hostname

**Cause:** DNS propagation delay or LoadBalancer not fully ready

**Solution:**
```bash
# Wait a few minutes for DNS propagation
# Test DNS resolution
nslookup <LOADBALANCER-URL>

# Check LoadBalancer health in AWS Console
# EC2 → Load Balancers → Check status
```

---

#### Issue 5: Terraform Apply Fails

**Symptom:** Terraform errors during apply

**Common Causes & Solutions:**

**AWS Credentials:**
```bash
# Verify credentials
aws sts get-caller-identity

# Reconfigure if needed
aws configure
```

**State Lock:**
```bash
# If state is locked, force unlock (use carefully)
terraform force-unlock <LOCK_ID>
```

**Resource Conflicts:**
```bash
# Clean up and retry
terraform destroy
terraform apply
```

---

#### Issue 6: kubectl Cannot Connect to Cluster

**Symptom:**
```bash
kubectl get nodes
# Error: couldn't get current server API group list
```

**Solution:**
```bash
# Update kubeconfig
aws eks update-kubeconfig --region eu-north-1 --name simple-app-eks --force

# Verify cluster exists
aws eks describe-cluster --name simple-app-eks --region eu-north-1
```

---

#### Issue 7: CI/CD Pipeline Fails

**Common Causes:**

1. **Missing GitHub Secrets:**
   - Go to Settings → Secrets → Actions
   - Verify all required secrets are set

2. **Invalid Docker Image Name:**
   - Check `ECR_REPOSITORY` secret format
   - Should be: `simple-app` (not `/simple-app`)

3. **AWS Permission Issues:**
   - Verify IAM user has EKS and ECR permissions

---

### Debug Commands

```bash
# Get detailed pod information
kubectl describe pod <pod-name>

# Check pod logs
kubectl logs <pod-name>

# Check previous container logs (if pod restarted)
kubectl logs <pod-name> --previous

# Execute commands in pod
kubectl exec -it <pod-name> -- /bin/sh

# Check all events
kubectl get events --sort-by='.lastTimestamp'

# Check node resources
kubectl describe nodes

# Test service connectivity from within cluster
kubectl run -it --rm debug --image=busybox --restart=Never -- sh
# Then: wget -O- http://simple-app-service/health
```

---

## 🚀 Future Enhancements

### Planned Improvements

1. **Persistent Storage**
   - Replace in-memory database with PostgreSQL
   - Use AWS RDS or Kubernetes StatefulSet
   - Add PersistentVolumeClaims

2. **Monitoring & Observability**
   - Implement Prometheus for metrics collection
   - Add Grafana dashboards for visualization
   - Set up CloudWatch integration
   - Configure alerting rules

3. **Security Enhancements**
   - Move nodes to private subnets
   - Implement Network Policies
   - Add AWS Secrets Manager integration
   - Enable pod security policies
   - Implement RBAC (Role-Based Access Control)

4. **Scalability**
   - Configure Horizontal Pod Autoscaler (HPA)
   - Implement Cluster Autoscaler
   - Add replica sets for high availability
   - Use larger instance types (t3.medium)

5. **Advanced Networking**
   - Implement Ingress Controller (nginx/ALB)
   - Add custom domain with Route53
   - Configure SSL/TLS certificates
   - Implement API Gateway

6. **Testing**
   - Add unit tests (pytest)
   - Implement integration tests
   - Add end-to-end tests in CI pipeline
   - Performance testing

7. **Documentation**
   - Auto-generate API docs with FastAPI
   - Add Swagger UI endpoint
   - Create architecture diagrams
   - Add runbooks for operations

8. **Infrastructure Improvements**
   - Multi-environment setup (dev, staging, prod)
   - Implement Terraform workspaces
   - Add backup and disaster recovery
   - Implement blue-green deployments

9. **Developer Experience**
   - Add local development with Docker Compose
   - Implement hot-reload for development
   - Add pre-commit hooks
   - Create development documentation

10. **Cost Optimization**
    - Implement Spot Instances for worker nodes
    - Add resource limits and requests
    - Configure cluster autoscaling policies
    - Monitor and optimize resource usage

---

## 📝 Notes

### Important Considerations

1. **Cost Management:**
   - This setup incurs AWS costs (EKS cluster, EC2 instances, LoadBalancer)
   - Approximate cost: $70-100/month
   - Remember to destroy resources when not needed:
     ```bash
     cd terraform
     terraform destroy
     ```

2. **Data Persistence:**
   - Current setup uses in-memory storage
   - Data is lost when pods restart
   - For production, implement persistent database

3. **Security:**
   - Current setup uses public subnets for simplicity
   - Production should use private subnets with NAT Gateway
   - Implement proper IAM roles and policies
   - Enable encryption at rest and in transit

4. **Scalability:**
   - Current setup uses 2x t3.micro instances
   - For production load, use larger instances
   - Configure auto-scaling based on metrics

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Isira Katakumbura**

- GitHub: [@isirakatakumbura](https://github.com/isirakatakumbura)
- Repository: [Simple_Task_Manager](https://github.com/isirakatakumbura/Simple_Task_Manager)

---

## 🙏 Acknowledgments

- AWS for EKS and cloud infrastructure
- FastAPI for the excellent Python framework
- Terraform for infrastructure as code
- Kubernetes community for container orchestration
- GitHub Actions for CI/CD automation

---

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Troubleshooting](#troubleshooting) section
2. Create a new issue with detailed information

---

## 🎓 Learning Resources

- [AWS EKS Documentation](https://docs.aws.amazon.com/eks/)
- [Kubernetes Documentation](https://kubernetes.io/docs/)
- [Terraform AWS Provider](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Docker Documentation](https://docs.docker.com/)

---

**Made by Isira Ketakumbura**
