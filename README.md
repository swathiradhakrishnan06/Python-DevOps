[![Python package](https://github.com/swathiradhakrishnan06/Python-DevOps/actions/workflows/devops.yml/badge.svg)](https://github.com/swathiradhakrishnan06/Python-DevOps/actions/workflows/devops.yml)

---

# 📘 Python DevOps – Wikipedia API

A FastAPI-based microservice that provides:

* 🔎 **Search results** from Wikipedia
* 📄 **Summaries of articles**
* 📝 **Key noun phrases** extracted using **TextBlob**

This project also demonstrates **DevOps practices** with:

* ✅ Automated testing (Pytest + coverage)
* ✅ Linting & formatting (Pylint + Black)
* ✅ Docker containerization
* ✅ CI/CD with **GitHub Actions**
* ✅ Deployment to **AWS ECR**

---

## 🚀 Features

* **FastAPI Endpoints**

  * `GET /` → Service health
  * `GET /search/{term}` → Wikipedia search suggestions
  * `GET /wiki/{name}` → Wikipedia article summary
  * `GET /phrase/{name}` → Extract noun phrases from summary

* **CLI Support** using `fire`:

  ```bash
  python cli-fire.py wiki "Artificial Intelligence"
  ```

---

## 🛠️ Installation

Clone the repository:

```bash
git clone https://github.com/swathiradhakrishnan06/Python-DevOps.git
cd Python-DevOps
```

Install dependencies:

```bash
make install
```

Run the FastAPI app:

```bash
python main.py
```

The API will be available at 👉 [http://localhost:8080](http://localhost:8080)

---

## 📦 Docker

Build and run the container:

```bash
make build
docker run -p 8080:8080 deploy-fastapi
```

---

## ⚡ Makefile Commands

| Command             | Description                        |
| ------------------- | ---------------------------------- |
| `make install`      | Install dependencies               |
| `make format`       | Format code with Black             |
| `make lint`         | Lint with Pylint                   |
| `make test`         | Run tests with Pytest & coverage   |
| `make build`        | Build Docker container             |
| `make run`          | Run Docker container               |
| `make deploy`       | Deploy to AWS ECR                  |
| `make all`          | Run install → lint → test → deploy |

---

## ✅ Testing

Run tests with **Pytest**:

```bash
make test
```

Example test output:

```
test_main.py::test_read_main PASSED
test_logic.py::test_wiki PASSED
```

---

## 🔄 CI/CD – GitHub Actions

Located at `.github/workflows/devops.yml`, the pipeline runs on each `push`:

* Install dependencies
* Run **linting**
* Run **tests**
* Run **code formatting**
* Build **Docker container**

---

## ☁️ Deployment to AWS ECR

1. Authenticate Docker with AWS:

   ```bash
   aws ecr get-login-password --region us-east-1 \
   | docker login --username AWS --password-stdin <account>.dkr.ecr.us-east-1.amazonaws.com
   ```
2. Build & tag:

   ```bash
   docker build -t fastapi-wiki .
   docker tag fastapi-wiki:latest <account>.dkr.ecr.us-east-1.amazonaws.com/fastapi-wiki:latest
   ```
3. Push:

   ```bash
   docker push <account>.dkr.ecr.us-east-1.amazonaws.com/fastapi-wiki:latest
   ```

---

## 📂 Project Structure

```
.
├── main.py              # FastAPI entrypoint
├── cli-fire.py          # CLI interface (fire)
├── src/
│   └── logic.py         # Wikipedia + TextBlob logic
├── test_main.py         # API tests
├── test_logic.py        # Logic tests
├── requirements.txt     # Dependencies
├── Dockerfile           # Docker build
├── Makefile             # DevOps automation
└── .github/workflows/   # GitHub Actions CI/CD
```

---

## 🧑‍💻 Tech Stack

* **Python 3.8+**
* **FastAPI**
* **Wikipedia API**
* **TextBlob NLP**
* **Pytest**
* **Pylint / Black**
* **Docker**
* **AWS ECR**
* **GitHub Actions**

---

→ [DETAILED\_README.md](./DETAILED_README.md)

---
## 📜 License

MIT License © 2025 [Swathi Radhakrishnan](https://github.com/swathiradhakrishnan06)

---


