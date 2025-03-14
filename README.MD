# Task Manager API 🚀

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)](https://flask.palletsprojects.com/)
[![MongoDB](https://img.shields.io/badge/MongoDB-5.0+-brightgreen.svg)](https://www.mongodb.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

```mermaid
graph TD
    A[Client] --> B[API Gateway]
    B --> C[Task Manager API]
    C --> D[MongoDB]
    C --> E[Authentication Service]
    C --> F[Logging Service]
    style A fill:#f9f,stroke:#333,stroke-width:4px
    style B fill:#bbf,stroke:#333,stroke-width:4px
    style C fill:#fbb,stroke:#333,stroke-width:4px
    style D fill:#bfb,stroke:#333,stroke-width:4px
    style E fill:#fbf,stroke:#333,stroke-width:4px
    style F fill:#ffb,stroke:#333,stroke-width:4px
```

A robust Flask-based Task Manager API with MongoDB integration, Docker containerization, and Jenkins CI/CD pipeline for automated deployment.

## 📋 Table of Contents

- [Features](#-features)
- [Architecture](#-architecture)
- [Project Structure](#-project-structure)
- [Setup & Installation](#-setup--installation)
- [Running with Docker](#-running-with-docker)
- [API Documentation](#-api-documentation)
- [Testing](#-testing)
- [CI/CD Pipeline](#-cicd-pipeline)
- [Deployment](#-deployment)
- [Contributing](#-contributing)
- [License](#-license)

## ✨ Features

- **CRUD Operations**: Full Create, Read, Update, Delete functionality for tasks
- **MongoDB Integration**: Scalable NoSQL database backend
- **Unit Testing**: Comprehensive test coverage with pytest
- **Docker Support**: Easy containerization and deployment
- **CI/CD Pipeline**: Automated testing and deployment with Jenkins
- **RESTful API**: Clean and well-documented endpoints
- **Scalable Architecture**: Designed for easy scaling and maintenance

[Rest of content truncated for brevity]
