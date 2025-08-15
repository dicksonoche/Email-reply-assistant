#!/bin/bash
# Test runner script for Email Reply Drafter
# This script ensures tests run with the correct Python interpreter

echo "🧪 Email Reply Drafter - Test Runner"
echo "======================================"

# Check if virtual environment exists
if [ ! -d "cust-env" ]; then
    echo "❌ Virtual environment 'cust-env' not found!"
    echo "Please create it first: python -m venv cust-env"
    exit 1
fi

# Check if virtual environment is activated
if [ -z "$VIRTUAL_ENV" ]; then
    echo "📦 Activating virtual environment..."
    source cust-env/bin/activate
fi

# Check if dependencies are installed
echo "🔍 Checking dependencies..."
if ! cust-env/bin/python -c "import chromadb, groq, fastapi" 2>/dev/null; then
    echo "❌ Dependencies not installed. Installing now..."
    pip install -r requirements.txt
fi

echo "✅ Dependencies ready!"
echo ""

# Run the comprehensive test suite
echo "🚀 Running comprehensive test suite..."
cust-env/bin/python test/run_tests.py

# Exit with the test result
exit $? 