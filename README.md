# Docker Git DevOps Project

## 📌 Project Overview

This project demonstrates a simple **Data Processing Python application** that is **containerized with Docker** and automatically **built and pushed to Docker Hub using GitHub Actions CI/CD**.

The Python script processes sample datasets using **Pandas and NumPy**, performs joins and transformations, and outputs the final result.

The main purpose of this project is to showcase:

* Docker containerization
* GitHub Actions CI/CD pipeline
* Automated Docker image build and push
* Basic data processing using Python

---

# 🏗️ Project Architecture

```
Developer
   │
   │ Push Code
   ▼
GitHub Repository
   │
   │ Trigger
   ▼
GitHub Actions CI/CD
   │
   │ Build Docker Image
   ▼
Docker Image Created
   │
   │ Push
   ▼
Docker Hub Repository
   │
   │ Pull
   ▼
Run Container Anywhere
(Local / Server / Cloud)
```

---


GitHub Actions CI/CD pipeline

<img width="2746" height="1042" alt="image" src="https://github.com/user-attachments/assets/c92a14db-5d03-4097-bb0e-60cdc6efa247" />


Automated Docker image build and push


<img width="3446" height="2154" alt="image" src="https://github.com/user-attachments/assets/da1134bf-1bcb-4541-b3ec-1f96688bb617" />




# 🔄 CI/CD Flow Diagram

```
+-------------+
|  Developer  |
+-------------+
        |
        | git push
        ▼
+------------------+
|  GitHub Repo     |
+------------------+
        |
        | Trigger Workflow
        ▼
+-----------------------+
| GitHub Actions CI/CD  |
| - Checkout Code       |
| - Login DockerHub     |
| - Build Docker Image  |
| - Push Image          |
+-----------------------+
        |
        ▼
+----------------------+
|   Docker Hub Repo    |
| mtousif2303/my-images|
+----------------------+
        |
        ▼
+----------------------+
| Run Container        |
| Anywhere (Docker)    |
+----------------------+
```

---

# 📂 Project Structure

```
docker-git-devops/
│
├── app.py                 # Python data processing script
├── Dockerfile             # Docker configuration
├── requirements.txt       # Python dependencies (optional)
├── .github/
│   └── workflows/
│       └── docker.yml     # GitHub Actions CI/CD workflow
└── README.md
```

---

# 🐳 Docker Setup

### Dockerfile

```
FROM python:latest
RUN pip install pandas numpy
WORKDIR /home
COPY . /home
CMD ["python","app.py"]
```

---

# ⚙️ GitHub Actions Workflow

The CI/CD pipeline performs the following steps:

1. Checkout repository code
2. Login to DockerHub
3. Build Docker image
4. Push image to DockerHub

Workflow file:

```
.github/workflows/docker.yml
```

---

# 🔐 Required GitHub Secrets

Add the following secrets in your repository settings:

| Secret Name        | Description                             |
| ------------------ | --------------------------------------- |
| DOCKERHUB_USERNAME | Your DockerHub username                 |
| DOCKERHUB_PASSWORD | Your DockerHub password or access token |

---

# 🚀 How It Works

1️⃣ Developer pushes code to GitHub
2️⃣ GitHub Actions workflow triggers automatically
3️⃣ Docker image is built using the Dockerfile
4️⃣ Image is pushed to DockerHub

DockerHub Image:

```
mtousif2303/my-images:mynewimage
```

---

# ▶️ Run the Container

Pull the image:

```
docker pull mtousif2303/my-images:mynewimage
```

Run the container:

```
docker run mtousif2303/my-images:mynewimage
```

---

# 📊 Technologies Used

* Python
* Pandas
* NumPy
* Docker
* GitHub Actions
* DockerHub

---

# 🎯 Learning Goals

This project demonstrates:

✔ Containerizing Python applications
✔ Automating builds using CI/CD
✔ Integrating Docker with GitHub Actions
✔ Publishing images to DockerHub

---

# 👨‍💻 Author

**Mohamed Tousif**

SAP Commerce Cloud Lead Developer
DevOps & Data Engineering Enthusiast
