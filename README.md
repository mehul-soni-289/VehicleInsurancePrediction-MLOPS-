# 🚀 Vehicle Data ML App – MLOps Project  

An end-to-end **MLOps project** created for the purpose of **learning and exploring MLOps concepts** such as reproducibility, automation, cloud deployment, and CI/CD pipelines.  
The project focuses more on **MLOps workflows** than on machine learning modeling itself.  

---

## 🌐 Deployed Project  
🔗 [Live App Link](http://54.82.106.112:5000/)  

---

## 🔑 Key Features  

### 📦 Project Structure & Automation  
- Auto-generated modular project structure with `template.py`  
- Reproducible environments via `requirements.txt`, `setup.py`, and `pyproject.toml`  
- Local package imports configured for scalable code management  

### 🗄️ Data Management  
- **MongoDB Atlas** used as the main data source  
- Dataset pushed to MongoDB via Jupyter notebooks  
- Data ingestion pipelines built to fetch, transform, and prepare data for ML workflows  

### 📊 Machine Learning Workflow (Minimal ML, More MLOps)  
- Pipeline includes:  
  **Data Ingestion → Validation → Transformation → Model Training → Evaluation → Pushing**  
- Schema-driven validation with `schema.yaml`  
- Models stored and versioned in **AWS S3** as a registry  

### 🛡️ Observability & Reliability  
- Centralized **logging** for every component  
- Custom **exception handling** for fault tolerance  
- Artifacts tracked in structured directories  

### ☁️ Cloud & Deployment  
- **AWS S3** → Model registry  
- **AWS IAM** → Secure credential & access management  
- **AWS ECR** → Container registry for storing Docker images  
- **AWS EC2 (Ubuntu 24.04)** → Hosting the deployed app  

### 🐳 CI/CD Pipeline  
- Containerized ML app with **Docker**  
- **GitHub Actions** workflow for automated CI/CD  
- **Self-hosted runner on EC2** for deployment automation  
- Secure credentials stored in **GitHub Secrets**  
- App hosted on **EC2 public IP with exposed port**  

---

## ⚙️ Tech Stack  

- **Languages & Tools**: Python, FastAPI, Jupyter Notebooks  
- **Data**: MongoDB Atlas, Pandas  
- **MLOps & Deployment**: Docker, GitHub Actions, AWS (EC2, S3, ECR, IAM)  
- **Version Control**: Git & GitHub  

---

## 📂 Project Workflow  

1. **Setup & Environment**  
   - Created virtual environment & installed dependencies  
   - Structured project for modular imports  

2. **Data Handling**  
   - Stored dataset in MongoDB Atlas  
   - Pulled & validated data through ingestion pipelines  

3. **Pipeline Building**  
   - Defined reusable entities, configs, and artifacts  
   - Built ingestion, validation, transformation & model trainer modules  

4. **Cloud Integration**  
   - Configured AWS S3 for model storage  
   - Set IAM credentials securely via environment variables  

5. **CI/CD Deployment**  
   - Dockerized ML app  
   - Pushed Docker images to AWS ECR  
   - Automated deployment using GitHub Actions + self-hosted EC2 runner  

6. **Serving the App**  
   - Hosted FastAPI app on AWS EC2 (accessible via public IP + port)  

---

## 🎯 Purpose of the Project  

🔹 To **learn and practice MLOps concepts** step by step  
🔹 To **understand how ML apps are deployed in production environments**  
🔹 To explore **CI/CD, containerization, and cloud workflows**  
🔹 To get hands-on with **AWS, Docker, GitHub Actions, and MongoDB Atlas**  

---

## 📌 Note  
The primary purpose of this project is to **explore and understand MLOps practices**.  
The machine learning part is intentionally kept simple, with most of the focus on **deployment, automation, and infrastructure setup**.  
