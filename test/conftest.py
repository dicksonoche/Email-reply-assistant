"""
Pytest configuration for Email Reply Drafter tests.
This file ensures proper import resolution during testing.
"""

import sys
import os

# Add the project root to the Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

# Test configuration
def pytest_configure(config):
    """Configure pytest with custom settings."""
    config.addinivalue_line(
        "markers", "integration: marks tests as integration tests"
    )
    config.addinivalue_line(
        "markers", "unit: marks tests as unit tests"
    )

def pytest_collection_modifyitems(config, items):
    """Automatically mark tests based on their location."""
    for item in items:
        if "test_api" in item.nodeid:
            item.add_marker("integration")
        elif "test_chromadb" in item.nodeid:
            item.add_marker("integration")
        else:
            item.add_marker("unit") 