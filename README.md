# Petstore API Test Automation Framework

This repository contains a comprehensive Test Automation Framework (TAF) designed to validate key API endpoints of the [Swagger Petstore](https://petstore.swagger.io/). The framework ensures the quality and stability of core API functionality through automated testing with Python and pytest.

## 🎯 Overview

The framework provides automated testing capabilities for the Swagger Petstore API, focusing on:
- Pet management operations (CRUD)
- API endpoint validation
- Data integrity testing
- Error handling verification
- Authentication and authorization testing

## 🛠️ Technology Stack

- **Python 3.9+** - Core programming language
- **pytest** - Testing framework
- **requests** - HTTP library for API calls
- **FastAPI** - Web framework for development/mocking
- **Poetry** - Dependency management
- **pytest-html** - HTML test reporting   CHECK
- **pytest-xdist** - Parallel test execution   CHECK

## 📁 Project Structure

```
├── README.md              # Project documentation
├── requirements.txt       # Dependencies for running the tests without poetry
├── pyproject.toml         # Poetry configuration and dependencies
├── pytest.ini            # Pytest configuration
├── conftest.py           # Shared fixtures and test configuration
├── .env.example          # Template for environment variables
├── .gitignore           # Git ignore patterns
├── tests/               # Test modules directory
```

## 🚀 Quick Start

### Prerequisites

- Python 3.9 or higher
- Poetry (recommended) or pip

### Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd api-testing
   ```

2. **Install dependencies using Poetry:**
   ```bash
   poetry install
   ```

   **Or using pip:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   ```bash
   cp .env.example .env
   ```
   Edit the `.env` file and add your API key:
   ```
   PETSTORE_API_KEY=your_api_key_here
   ```

### Running Tests

1. **Run all tests:**
   ```bash
   poetry run pytest
   ```

2. **Run tests with HTML report:**
   ```bash
   poetry run pytest --html=reports/report.html --self-contained-html
   ```

3. **Run tests in parallel:**
   ```bash
   poetry run pytest -n auto
   ```

4. **Run specific test markers:**
   ```bash
   # Smoke tests
   poetry run pytest -m smoke
   
   # Regression tests
   poetry run pytest -m regression
   ```

5. **Run with verbose output:**
   ```bash
   poetry run pytest -v -s
   ```

## 🧪 Test Categories

### Test Markers

The framework uses pytest markers to categorize tests:

- **`@pytest.mark.smoke`** - Quick validation tests for basic functionality
- **`@pytest.mark.regression`** - Comprehensive tests covering all endpoints

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `PETSTORE_API_KEY` | API key for Petstore authentication | Yes |

## 🔄 Continuous Integration

The framework is designed to integrate with CI/CD pipelines:

1. **Environment Setup**: Ensure `PETSTORE_API_KEY` is set as a secret
2. **Dependency Installation**: Use Poetry or pip to install requirements
3. **Test Execution**: Run pytest with appropriate markers and reporting
4. **Artifact Collection**: Save HTML reports and logs

### Example CI Configuration

```yaml
- name: Run Tests
  run: |
    poetry install
    poetry run pytest --html=reports/report.html -m smoke
  env:
    PETSTORE_API_KEY: ${{ secrets.PETSTORE_API_KEY }}
```