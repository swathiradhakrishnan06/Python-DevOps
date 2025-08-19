# DevOps Project Briefing: Building Real-World AWS Microservices with Python and FastAPI

## 1. Introduction and Core Philosophy
This briefing summarises key concepts and practical steps for building a real-world Python microservice, from initial scaffolding to continuous delivery and deployment on AWS. The core philosophy emphasises a structured, automated, and cloud-native approach to software development, particularly for microservices.

**Key Takeaways:**

- **Structured Development:** Avoids ad-hoc approaches (e.g., Jupyter Notebooks for main development) in favour of a defined project structure.
- **Cloud-Native Focus:** Leverages cloud development environments (e.g., GitHub Codespaces, AWS Cloud9) for co-location with cloud resources, streamlining development, debugging, and execution.
- **Automation through Makefiles:** Utilises Makefile as a central command hub for managing project lifecycle stages, including installation, formatting, linting, testing, building, and deployment. This "allows us to clearly articulate all the different things that we need to do for our project."
- **Continuous Integration/Continuous Delivery (CI/CD):** Establishes automated workflows (e.g., GitHub Actions, AWS CodeBuild) to ensure code quality, reproducibility, and efficient deployment. This is crucial for "making things better every time I make a change."
- **Containerisation:** Packages the application into Docker containers for isolated, reproducible, and portable deployment across various environments.
- **Microservices with FastAPI:** Implements web services using FastAPI, known for its performance and automatic API documentation.

---

## 2. Project Scaffolding and Initial Setup
The foundational step involves establishing a robust project structure and environment.

**Key Elements:**

- **Code Repository:** Typically GitHub, serving as the central hub for source code.
- **Makefile:** The "tool that keeps you organised when you're building on a software project" by defining key lifecycle commands (install, lint, test, deploy, format, build, all).
- **requirements.txt:** Specifies Python packages and "pin[s] the version numbers so that later if in two years somebody checks out my project we can be assured that it will work properly."
- **Source Code Directory (src):** Houses the core business logic, structured as a Python library with an `__init__.py` file to enable imports.
- **Test Code Directory (test_logic.py, test_main.py):** Dedicated files for unit and integration tests.
- **Dockerfile:** Defines how to build the application's Docker image.
- **main.py:** The entry point for the microservice.
- **buildspec.yml (for AWS CodeBuild):** Defines build commands for AWS CI/CD.
- **Virtual Environment:** Essential for Python projects to "not have package conflicts and or the system python is installed sometimes can have issues as well."

**Practical Steps:**

- Create Virtual Environment:  
````bash
  python3 -m venv .venv
  source .venv/bin/activate
````

Sourcing it in `.bashrc` for cloud environments ensures it's "sourced every time I open up a shell."

* Create Empty Files:

  ```bash
  touch requirements.txt Dockerfile Makefile main.py
  ```

* Create Library Structure:

  ```bash
  mkdir src
  touch src/__init__.py src/logic.py
  ```

* Populate Makefile: Define targets like `install`, `lint`, `test`, `deploy`, `format`, `build`, and an `all` target to run them sequentially.

```bash
install: pip install --upgrade pip && pip install -r requirements.txt
format: black *.py src/*.py
lint: pylint --disable=R,C *.py src/*.py
test: python -m pytest test_* --cov=src --cov=main
build: docker build -t deploy-fast-api .
```

---

## 3. Continuous Integration (CI) with GitHub Actions

CI automates the process of building and testing code changes, providing "instant feedback."

**Key Concepts:**

* **Automated Workflows:** Configured via YAML files in `.github/workflows/`.
* **Build, Test, Deploy:** The typical CI/CD pipeline stages.
* **Status Badges:** Integrates build status directly into the README.md for clear project health indication.

**Practical Steps:**

* Create Workflow File: `.github/workflows/devops.yml`.
* Define Jobs and Steps: Specify Python version (e.g., `python-version: '3.13'`).
* Install Dependencies: Runs `make install`.
* Format Code: Runs `make format`.
* Lint Code: Runs `make lint`. "This is a really great warning system or early warning system that will they'll tell us hey look at this you've got a problem here in your code you need to fix this."
* Test Code: Runs `make test`.

---

## 4. Building Command-Line Interface (CLI) Tool

A CLI tool serves as an intermediary step to test core logic and interact with the system before building a full microservice.

**Key Concept:**

* **Python Fire Library:** "Makes it really easy to write chameleon Tools in Python," allowing mapping functions directly to command-line arguments. It offers "amazing" meta-programming capabilities, automatically generating help menus from docstrings.

**Practical Steps:**

* Create CLI File: `cli_fire.py`.
* Import Logic and Fire:

  ```python
  from src.logic import Wiki, search_Wiki
  import fire
  ```
* Map Module to CLI:

  ```python
  fire.Fire(logic)
  ```

  Exposes all functions in the logic module as CLI commands. This enables a "more sophisticated chameleon tool" with an "interactive workflow."

---

## 5. Developing the FastAPI Microservice

This section details the creation of the web service using FastAPI, integrating the previously developed logic.

**Key Concepts:**

* **FastAPI:** A modern, fast (high-performance) web framework for building APIs with Python 3.7+, based on standard Python type hints. It automatically generates interactive API documentation (Swagger UI).
* **Endpoints:** Define specific URLs that clients can interact with (e.g., `/search`, `/wiki`, `/phrases`).
* **Uvicorn:** An ASGI server for running FastAPI applications.

**Practical Steps:**

* Install FastAPI and Uvicorn: Add `fastapi` and `uvicorn` to `requirements.txt`.
* `main.py` Implementation:

  ```python
  import uvicorn
  from src.logic import wiki_search, wiki, phrase
  from fastapi import FastAPI

  app = FastAPI()
  ```
* Define routes using decorators:

  ```python
  @app.get("/search/{value}")
  @app.get("/wiki/{name}")
  @app.get("/phrases/{name}")
  ```
* Implement logic within route functions to call `Wiki`, `search_Wiki`, and `phrases` from the `src` library.
* Include TextBlob for NLP functionalities like phrase extraction. "This is definitely an improvement of our code."

---

## 6. Containerisation with Docker

Packaging the application into a Docker container ensures environmental consistency and portability.

**Key Concepts:**

* **Dockerfile:** A text file containing instructions for building a Docker image.
* **Base Image:** Using `python:3.13-slim` for a smaller, more efficient image.
* **Working Directory:** Defines the directory inside the container where the application will run.
* **Exposed Ports:** Specifies the network ports the container listens on.
* **Corpora Download:** Crucial step for NLP libraries like TextBlob, as "it'll blow up because we didn't load that Library."

**Practical Steps:**

* Create Dockerfile:

  ```dockerfile
  FROM python:3.13-slim
  WORKDIR /app
  COPY . /app
  RUN pip install -r requirements.txt
  RUN python -m textblob.download_corpora
  EXPOSE 8080
  CMD ["python", "main.py"]
  ```

* Build Docker Image:

  ```bash
  make build
  ```

* Run Docker Container:

  ```bash
  make run
  ```

  This "makes a new isolated environment."

---

## 7. Continuous Delivery (CD) with AWS CodeBuild and ECR

The final stage involves automating the deployment of the containerised application to AWS.

**Key Concepts:**

* **Elastic Container Registry (ECR):** AWS's fully managed Docker container registry, allowing storage and management of Docker images.
* **AWS CodeBuild:** A fully managed continuous integration service that compiles source code, runs tests, and produces software packages that are ready to deploy. It "really finds the weaknesses in the reproducibility of your project."
* **Buildspec File (`buildspec.yml`):** Defines the build commands for CodeBuild.

**Practical Steps:**

* Create ECR Repository: In AWS ECR, create a new repository (e.g., `fast-api-wiki`).

* Configure AWS CodeBuild Project: Link to GitHub repository.

* Enable "rebuild every time a code build is changed" for continuous delivery.

* Select Amazon Linux 2 and standard runtime.

* Enable "Privileged" mode for Docker builds.

* Assign an IAM role with ECR push permissions.

* Use `buildspec.yml` for build commands.

* Update Makefile (Deploy Target):

  * Include ECR authentication command:

    ```bash
    aws ecr get-login-password | docker login ...
    ```
  * Add Docker build command (with ECR repository tag).
  * Add Docker push command to ECR.

* Create `buildspec.yml`:

  ```yaml
  version: 0.2
  phases:
    install:
      commands:
        - make install
        - python -m textblob.download_corpora
    build:
      commands:
        - make lint
        - make test
        - make format
        - make build
        - make deploy
  ```

  This ensures all quality gates are passed before deployment. "Everything passed!"

---

## 8. Conclusion

By following these structured steps, the project demonstrates a robust and automated workflow for developing, testing, and deploying Python microservices to AWS. The emphasis on Makefile, CI/CD, and containerisation provides a reproducible and efficient development lifecycle, crucial for modern DevOps practices.

---


