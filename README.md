# FastAPI Backend Template

A robust, production-ready template for building FastAPI applications with Python 3.13+.
This repository provides a solid foundation with best practices for development, testing, dockerization, and CI/CD.

## 🚀 Features

* **Modern Python**: Built on Python 3.13.
* **FastAPI**: High-performance web framework.
* **Dependency Management**: Uses [uv](https://github.com/astral-sh/uv) for lightning-fast package management.
* **Containerization**: Optimized Multi-stage Dockerfile and Docker Compose setup.
* **Code Quality**:
  * **Ruff**: Extremely fast linter and formatter.
  * **Mypy**: Static type checking.
  * **Pre-commit**: Git hooks for code quality assurance.
* **Testing**: `pytest` with coverage reporting (`pytest-cov`).
* **CI/CD**: Comprehensive GitHub Actions workflows:
  * Linting & Type Checking
  * Unit Tests
  * Docker Build & Test
  * Semantic Release
  * PR Labeling & Semantic Title checks
* **Automated Updates**: Renovate and Dependabot configuration included.

## 🛠️ Prerequisites

* [Python 3.13+](https://www.python.org/downloads/)
* [uv](https://github.com/astral-sh/uv) (Recommended) or pip
* [Docker](https://www.docker.com/) & Docker Compose

## 🏁 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/aGallea/fastapi-backend-template.git
cd fastapi-backend-template
```

### 2. Install dependencies

This project uses `uv` for dependency management.

```bash
# Install dependencies (including dev dependencies)
uv sync
```

### 3. Run locally

You can run the application using the helper script or directly with `uv`.

```bash
# Run with hot-reload (Development)
uv run uvicorn my_app.app:create_app --factory --reload
```

Or run the module directly:

```bash
uv run python -m my_app
```

The API will be available at `http://localhost:8080`.
API Documentation (Swagger UI): `http://localhost:8080/docs`

## 🐳 Docker

Run the application stack using Docker Compose:

```bash
docker-compose up --build
```

This will start the API service on port `8080`.

## 🧪 Testing

Run the test suite with `pytest`:

```bash
uv run pytest
```

Generate a coverage report:

```bash
uv run pytest --cov=my_app --cov-report=term-missing
```

## 🧹 Code Quality

Run linting and formatting checks:

```bash
# Format code
uv run ruff format .

# Lint code
uv run ruff check . --fix

# Type check
uv run mypy .
```

### Pre-commit Hooks

Install pre-commit hooks to ensure code quality before committing:

```bash
uv run pre-commit install
```

## 📂 Project Structure

```text
.
├── .github/            # GitHub Actions workflows
├── my_app/             # Application source codes
├── my_app/             # Application source code
│   ├── api/            # API routes and endpoints
│   ├── core/           # Core functionality (config, logging)
│   ├── app.py          # FastAPI application factory
│   └── __main__.py     # Entry point
├── tests/              # Test suite
├── scripts/            # Helper scripts
├── Dockerfile          # Docker build definition
├── docker-compose.yml  # Docker Compose configuration
├── pyproject.toml      # Project configuration and dependencies
└── README.md           # Project documentation
```

## 🔄 CI/CD Pipelines

The project includes several GitHub Actions workflows located in `.github/workflows`:

* **`test.yml`**: Runs unit tests on every push and PR.
* **`lint-backend.yml`**: Checks code style (Ruff) and types (Mypy).
* **`test-docker-compose.yml`**: Verifies the Docker build and runs integration tests.
* **`release.yml`**: Automates versioning and releases using Semantic Release.
* **`semantic-pr.yml`**: Enforces semantic commit messages for PR titles.

## 🤝 Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/amazing-feature`).
3. Commit your changes (`git commit -m 'feat: add amazing feature'`).
4. Push to the branch (`git push origin feature/amazing-feature`).
5. Open a Pull Request.

Please ensure your PR title follows [Conventional Commits](https://www.conventionalcommits.org/) format.

## 📄 License

[MIT](LICENSE)
