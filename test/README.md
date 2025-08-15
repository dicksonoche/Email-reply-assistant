# Test Suite Documentation

This directory contains the comprehensive test suite for the Email Reply Drafter application.

## 🧪 Test Files Overview

### Core Test Files
- **`test_imports.py`** - Verifies all module imports work correctly
- **`test_api.py`** - Tests API functionality and AI generation
- **`test_chromadb.py`** - Tests ChromaDB connectivity and queries
- **`run_tests.py`** - Comprehensive test runner that executes all tests

### Configuration Files
- **`conftest.py`** - Pytest configuration and test markers
- **`requirements-test.txt`** - Testing-specific dependencies
- **`__init__.py`** - Makes this directory a Python package

## 🚀 Quick Start

### Run All Tests (Recommended)
```bash
# From project root
./run_tests.sh
```

### Run Individual Tests
```bash
# Test imports only
python test/test_imports.py

# Test API functionality
python test/test_api.py

# Test ChromaDB
python test/test_chromadb.py

# Run comprehensive suite
python test/run_tests.py
```

### Using Pytest
```bash
# Install testing dependencies
pip install -r test/requirements-test.txt

# Run all tests
pytest test/

# Run with coverage
pytest test/ --cov=app --cov-report=html
```

## 📋 Test Categories

### Unit Tests
- **Import Tests** - Verify module imports work
- **Function Tests** - Test individual functions
- **Configuration Tests** - Verify settings and config

### Integration Tests
- **API Tests** - Test complete API endpoints
- **Database Tests** - Test ChromaDB operations
- **AI Tests** - Test Groq API integration