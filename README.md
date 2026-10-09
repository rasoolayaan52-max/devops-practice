# DevOps Practice: Automated Monitoring & Observability Stack

An end-to-end hands-on DevOps project demonstrating containerization, multi-service orchestration, automated continuous integration, and infrastructure observability.

---

## 🏗 Architecture Overview

- **Application (`monitor.py`)**: Lightweight Python system monitor checking environment metadata and operational status.
- **Containerization (`Dockerfile`)**: Standalone `python:3.12-slim` image packaged and run locally.
- **Multi-Service Orchestration (`docker-compose.yml`)**:
  - `web`: Nginx Alpine web server (port 8080).
  - `monitor`: Custom Python container running on the shared bridge network.
  - `prometheus`: Scrapes and stores operational time-series metrics (port 9090).
  - `grafana`: Real-time analytics visualization dashboards connected to Prometheus (port 3000).
- **Continuous Integration (`.github/workflows/ci.yml`)**: Automated GitHub Actions workflow testing code execution on every push to `main`.

---

## 🚀 Quick Start

### 1. Prerequisites
- Docker Desktop with WSL 2 backend
- Git & Python 3.12+

### 2. Launch the Multi-Container Stack
### 3. Service Access
- **Nginx Web Server**: [http://localhost:8080](http://localhost:8080)
- **Prometheus TSDB**: [http://localhost:9090](http://localhost:9090)
- **Grafana Dashboards**: [http://localhost:3000](http://localhost:3000)

### 4. Teardown
---

## 📅 10-Day Sprint Roadmap Completed
- **Day 1**: Linux terminal navigation, directory trees, local Git repository initialization.
- **Day 2**: Configured `main` branch, linked remote GitHub origin, and pushed initial code.
- **Day 3**: Authored Python system health check script (`monitor.py`).
- **Day 4**: Configured Docker Desktop with WSL 2 backend runtime.
- **Day 5**: Packaged script into a custom `Dockerfile` and verified Linux container runtime.
- **Day 6**: Orchestrated multi-container workloads using `docker-compose.yml` (Nginx + Monitor).
- **Day 7**: Configured GitHub Actions CI pipeline (`ci.yml`) for automated cloud testing.
- **Day 8**: Integrated Prometheus metrics collection on port 9090.
- **Day 9**: Deployed Grafana visualization connected to Prometheus data source on port 3000.
- **Day 10**: Production portfolio documentation, teardown testing, and sprint finalization.