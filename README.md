# Vehicle-Insurance-MLOps

## 🚀 Overview
Welcome to **Vehicle-Insurance-MLOps**, an end-to-end machine learning operations (MLOps) project designed to automate the lifecycle of a vehicle insurance prediction model. This project follows industry best practices and integrates various tools and services, making it an ideal showcase for recruiters and industry professionals.

## 📌 Key Features
- **Automated Project Setup** with a structured template
- **Environment Management** using Conda
- **MongoDB Atlas Integration** for data storage
- **Logging & Exception Handling** for robust debugging
- **Data Processing Pipeline** including ingestion, validation, transformation, and feature engineering
- **Model Training & Evaluation** using state-of-the-art ML algorithms
- **AWS Integration** (S3, IAM, EC2, ECR) for model storage and CI/CD
- **Containerization & Deployment** with Docker & GitHub Actions
- **Self-hosted CI/CD Pipeline** on AWS EC2
- **Web App Interface** for easy model interaction

---

## 🛠️ Setup & Installation
### 1️⃣ Project Initialization
Execute the **template.py** script to generate the project structure:
```bash
python template.py
```

### 2️⃣ Dependency Management
Create a virtual environment and install dependencies:
```bash
conda create -n vehicle python=3.10 -y
conda activate vehicle
pip install -r requirements.txt
```
Verify installation:
```bash
pip list
```

### 3️⃣ MongoDB Atlas Setup
1. Create a MongoDB Atlas account and project.
2. Deploy a free-tier **M0** cluster.
3. Setup authentication and network access (`0.0.0.0/0`).
4. Copy and save the **MongoDB connection string**.
5. Push data to MongoDB using the `mongoDB_demo.ipynb` notebook.
6. Validate data ingestion via MongoDB Atlas UI.

---

## 📊 Data Pipeline
### 🏗 Data Ingestion
- Define database connection in `configuration.mongo_db_connections.py`
- Extract & transform data from MongoDB to Pandas DataFrame
- Implement `DataIngestionConfig` & `DataIngestionArtifact` classes
- Execute ingestion script via `training pipeline`

### ✅ Data Validation & Transformation
- Define schema in `config.schema.yaml`
- Implement `DataValidation` & `DataTransformation` classes
- Add feature engineering logic in `estimator.py`

---

## 🎯 Model Training & Evaluation
- Implement **model training pipeline**
- Tune hyperparameters & evaluate model performance
- Store models in **AWS S3** bucket (`my-model-mlopsproj`)

---

## ☁️ Cloud Services (AWS Integration)
### 🔑 IAM & S3 Setup
1. Create an IAM user with **AdministratorAccess** policy.
2. Generate access keys and configure them as environment variables.
3. Create an S3 bucket (`my-model-mlopsproj`) for model storage.

```bash
export AWS_ACCESS_KEY_ID="your-access-key"
export AWS_SECRET_ACCESS_KEY="your-secret-key"
export AWS_DEFAULT_REGION="us-east-1"
```

### 📦 Docker & GitHub Actions
- Create **Dockerfile** and `.dockerignore`
- Setup **GitHub Actions CI/CD** workflow
- Deploy models via **AWS ECR** and **EC2**

### 🚀 Deployment
- Host the application on **AWS EC2 Ubuntu instance**
- Expose API via **port 5080**

```bash
sudo apt-get update -y
sudo apt-get install docker.io
```

Validate deployment by accessing:
```
http://<EC2-PUBLIC-IP>:5080
```

---

## 🔄 Continuous Integration & Deployment (CI/CD)
- **Self-hosted GitHub Runner** on AWS EC2
- Automated Docker builds & pushes to **AWS ECR**
- Deployment pipeline triggered on **git push**

---

## 🎯 Usage
- **Train a new model**: `/training`
- **Make predictions**: `/predict`

---

## 💡 Conclusion
This project showcases an end-to-end **MLOps pipeline** for a **vehicle insurance prediction model**, integrating **ML, cloud services, CI/CD, and deployment**. It serves as an excellent demonstration of MLOps expertise, making it an impressive addition to any portfolio.

📢 **Connect with me for more insights on MLOps and ML deployment!** 🚀

