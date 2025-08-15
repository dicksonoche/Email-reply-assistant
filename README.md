# Email Reply Drafter - AI-Powered Customer Support Assistant

A sophisticated AI-powered application that generates professional customer support replies based on similar past interactions. Built with FastAPI, ChromaDB, and Groq AI, this system provides intelligent, context-aware responses for customer service teams.

## 🏗️ Architecture Overview

The application follows a microservices architecture with multiple interfaces:

- **REST API** (FastAPI) - HTTP-based interface for web applications
- **gRPC Server** - High-performance RPC interface for microservices
- **Streamlit Frontend** - User-friendly web interface for testing and demonstration
- **ChromaDB** - Vector database for semantic similarity search
- **Groq AI** - LLM provider using the `openai/gpt-oss-20b` model

## 🚀 Features

- **Semantic Search**: Find similar past customer interactions using vector embeddings
- **AI-Powered Generation**: Generate contextually relevant replies using Groq's LLM
- **Multiple Interfaces**: REST API, gRPC, and web frontend
- **Professional Tone**: Optimized for customer support with Apple-style responses
- **Fallback Handling**: Graceful degradation when AI services are unavailable
- **Scalable Design**: Built with modern Python frameworks for production use

## 📁 Project Structure

```
email-reply/
├── app/                          # Core application modules
│   ├── __init__.py
│   ├── main.py                  # FastAPI REST server
│   ├── generation.py            # AI reply generation logic
│   ├── retrieval.py             # ChromaDB similarity search
│   └── prompts.py               # AI prompt templates
├── frontend/                     # Streamlit web interface
│   └── app.py                   # Streamlit application
├── protobuf/                     # gRPC protocol definitions
│   ├── email.proto              # Protocol buffer schema
│   ├── email_pb2.py            # Generated Python classes
│   └── email_pb2_grpc.py       # Generated gRPC stubs
├── scripts/                      # Utility scripts
│   └── prepare_data.py          # Data preparation utilities
├── test/                         # Test suite and testing utilities
│   ├── __init__.py              # Test package initialization
│   ├── conftest.py              # Pytest configuration
│   ├── run_tests.py             # Comprehensive test runner
│   ├── test_api.py              # API functionality tests
│   ├── test_chromadb.py         # ChromaDB connection tests
│   ├── test_imports.py          # Import verification tests
│   └── requirements-test.txt     # Testing dependencies
├── chroma_db/                    # Vector database storage
├── data/                         # Training and test data
├── grpc_server.py               # gRPC server implementation
├── run_tests.sh                 # Quick test runner script
├── requirements.txt              # Python dependencies
└── README.md                    # This file
```

## 🛠️ Technology Stack

### Backend
- **FastAPI** - Modern, fast web framework for building APIs
- **ChromaDB** - Vector database for similarity search
- **Sentence Transformers** - Text embedding models
- **Groq** - AI inference platform with `openai/gpt-oss-20b` model

### Frontend
- **Streamlit** - Rapid web application development
- **Requests** - HTTP library for API communication

### Communication
- **gRPC** - High-performance RPC framework
- **Protocol Buffers** - Data serialization format

### Development & Testing
- **Python 3.8+** - Core programming language
- **Uvicorn** - ASGI server for FastAPI
- **Pandas** - Data manipulation and analysis

## 📋 Prerequisites

- Python 3.8 or higher
- Groq API key
- Sufficient disk space for ChromaDB (recommended: 1GB+)
- Internet connection for AI model inference

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone <repository-url>
cd email-reply
```

### 2. Create Virtual Environment
```bash
python -m venv cust-env
source cust-env/bin/activate  # On Windows: cust-env\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Environment Configuration
Create a `.env` file in the project root:
```bash
GROQ_API_KEY=your_groq_api_key_here
```

Or set environment variables directly:
```bash
export GROQ_API_KEY="your_groq_api_key_here"
```

### 5. Get Groq API Key
1. Visit [Groq Console](https://console.groq.com/)
2. Sign up or log in to your account
3. Generate a new API key
4. Add it to your environment variables

## 🎯 Usage

### Starting the REST API Server
```bash
cd app
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

The API will be available at:
- **API Base**: http://localhost:8000
- **Interactive Docs**: http://localhost:8000/docs
- **Alternative Docs**: http://localhost:8000/redoc

### Starting the gRPC Server
```bash
python grpc_server.py
```

The gRPC server runs on port 50051.

### Starting the Streamlit Frontend
```bash
cd frontend
streamlit run app.py
```

The web interface will be available at http://localhost:8501.

## 📚 API Reference

### REST API Endpoints

#### `GET /`
Returns API information and available endpoints.

**Response:**
```json
{
  "message": "Email Reply Drafter API",
  "description": "AI-powered customer support reply generation",
  "endpoints": {
    "POST /draft_reply": "Generate a reply for a customer query",
    "GET /docs": "Interactive API documentation (Swagger UI)",
    "GET /redoc": "Alternative API documentation"
  }
}
```

#### `GET /health`
Health check endpoint for monitoring.

**Response:**
```json
{
  "status": "healthy",
  "service": "Email Reply Drafter API"
}
```

#### `POST /draft_reply`
Generates a customer support reply based on the query.

**Request Body:**
```json
{
  "text": "My iPhone battery is draining too fast"
}
```

**Response:**
```json
{
  "reply": "Thank you for contacting Apple Support regarding your iPhone battery issue..."
}
```

### gRPC Service

#### `EmailService.DraftReply`
Generates replies using the gRPC interface.

**Request:**
```protobuf
message QueryRequest {
  string text = 1;
}
```

**Response:**
```protobuf
message ReplyResponse {
  string reply = 1;
}
```

## 🔧 Configuration

### ChromaDB Settings
- **Database Path**: `./chroma_db/`
- **Collection Name**: `support_queries`
- **Embedding Model**: `all-MiniLM-L6-v2`
- **Similarity Results**: 3 (configurable in `retrieval.py`)

### AI Model Configuration
- **Provider**: Groq
- **Model**: `openai/gpt-oss-20b`
- **Max Tokens**: 1000
- **Temperature**: Default (not specified)

### Server Configuration
- **REST API Port**: 8000
- **gRPC Port**: 50051
- **Streamlit Port**: 8501

## 🧪 Testing

### Quick Test Runner (Recommended)
```bash
# Run all tests with automatic setup
./run_tests.sh
```

This script will:
- Check for virtual environment
- Install dependencies if needed
- Run the comprehensive test suite
- Provide detailed results

### Running All Tests Manually
```bash
# Run the comprehensive test suite
python test/run_tests.py
```

### Individual Test Modules
```bash
# Test API components
python test/test_api.py

# Test ChromaDB connection
python test/test_chromadb.py

# Test basic imports only
python test/test_imports.py
```

### Using Pytest (Recommended)
```bash
# Install testing dependencies
pip install -r test/requirements-test.txt

# Run all tests with pytest
pytest test/

# Run with coverage
pytest test/ --cov=app --cov-report=html

# Run specific test categories
pytest test/ -m "integration"  # Integration tests
pytest test/ -m "unit"         # Unit tests
```

### Test API Components
The test suite verifies:
- Module imports and dependencies
- Retrieval functionality
- Generation functionality
- ChromaDB connectivity
- API endpoint functionality

### Test ChromaDB Connection
This script verifies:
- ChromaDB connection
- Collection access
- Query functionality
- Database integrity

### Manual API Testing
```bash
# Test the draft_reply endpoint
curl -X POST "http://localhost:8000/draft_reply" \
     -H "Content-Type: application/json" \
     -d '{"text": "My iPhone screen is cracked"}'
```

## 📊 Data Management

### ChromaDB Collection Structure
The `support_queries` collection stores:
- **Query**: Customer's original question
- **Response**: Support agent's reply
- **Embeddings**: Vector representations for similarity search

### Adding Training Data
Use the `scripts/prepare_data.py` script to:
- Load customer support data
- Generate embeddings
- Populate the ChromaDB collection

## 🚀 Deployment

### Production Considerations

#### Environment Variables
```bash
# Required
GROQ_API_KEY=your_production_key

# Optional
LOG_LEVEL=INFO
CHROMA_DB_PATH=/path/to/persistent/storage
MAX_WORKERS=10
```

#### Docker Deployment
Create a `Dockerfile`:
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8000 50051 8501

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```