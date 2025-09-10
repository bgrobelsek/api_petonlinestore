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
├── pyproject.toml         # Poetry configuration and dependencies
├── pytest.ini            # Pytest configuration
├── conftest.py           # Shared fixtures and test configuration
├── .env                  # Environment variables (API keys)
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

### Test Structure

Tests are organized by functionality and include:
- **Pet Operations**: Create, Read, Update, Delete pets
- **Data Validation**: Schema validation and data integrity
- **Error Handling**: Invalid requests and edge cases
- **Authentication**: API key validation

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `PETSTORE_API_KEY` | API key for Petstore authentication | Yes |

### pytest Configuration

The framework is configured in `pytest.ini`:
- Test discovery in `tests/` directory
- Custom markers for test categorization
- Logging configuration for debugging

### Fixtures

Common fixtures are defined in `conftest.py`:

- **`base_url`** - Petstore API base URL
- **`api_key`** - API authentication key
- **`session`** - Configured requests session with headers
- **`pet_payload`** - Default pet data for testing

## 📊 Reporting

### HTML Reports

Generate detailed HTML test reports:
```bash
poetry run pytest --html=reports/report.html --self-contained-html
```

Reports include:
- Test execution summary
- Pass/fail status for each test
- Detailed error messages and stack traces
- Test duration and performance metrics

### Console Output

The framework provides structured console output with:
- Test progress indicators
- Real-time pass/fail status
- Summary statistics
- Detailed error information for failed tests

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

## 📈 Best Practices

### Test Design
- Use descriptive test names that explain the scenario
- Implement proper test data setup and cleanup
- Utilize fixtures for common test dependencies
- Group related tests using pytest markers

### Maintenance
- Keep test data isolated and independent
- Use configuration files for test parameters
- Implement proper error handling and logging
- Regular updates to dependencies and test cases

### Debugging
- Use verbose output (`-v -s`) for detailed test information
- Check logs for API request/response details
- Utilize pytest's built-in debugging capabilities
- Review HTML reports for comprehensive test analysis

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-test`)
3. Add your tests following the established patterns
4. Ensure all tests pass (`poetry run pytest`)
5. Submit a pull request with a clear description

### Code Style
- Follow PEP 8 Python style guidelines
- Use meaningful variable and function names
- Add docstrings to fixtures and complex test functions
- Keep test methods focused on single scenarios

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📞 Support

For questions, issues, or contributions:
- Open an issue on GitHub
- Review existing documentation
- Check test logs and reports for debugging information

---

**Note**: This framework is designed for testing the public Swagger Petstore API. Ensure you have proper authorization and follow the API's terms of service when running tests.