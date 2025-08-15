#!/usr/bin/env python3
"""
Simple import test for Email Reply Drafter application.
This test only verifies that modules can be imported without errors.
"""

import sys
import os

# Add the project root to the Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

def test_basic_imports():
    """Test basic module imports."""
    try:
        print("Testing basic imports...")
        
        # Test app package import
        import app
        print("✅ app package imported successfully")
        
        # Test individual modules
        from app import retrieval
        print("✅ app.retrieval imported successfully")
        
        from app import generation
        print("✅ app.generation imported successfully")
        
        from app import prompts
        print("✅ app.prompts imported successfully")
        
        from app import main
        print("✅ app.main imported successfully")
        
        return True
        
    except Exception as e:
        print(f"❌ Import test failed: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

def test_dependency_imports():
    """Test external dependency imports."""
    try:
        print("\nTesting dependency imports...")
        
        import chromadb
        print("✅ chromadb imported successfully")
        
        import groq
        print("✅ groq imported successfully")
        
        import fastapi
        print("✅ fastapi imported successfully")
        
        import sentence_transformers
        print("✅ sentence_transformers imported successfully")
        
        return True
        
    except Exception as e:
        print(f"❌ Dependency import test failed: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("🧪 Import Test Suite")
    print("="*50)
    
    basic_imports = test_basic_imports()
    dependency_imports = test_dependency_imports()
    
    print(f"\n{'='*50}")
    print("IMPORT TEST SUMMARY")
    print(f"{'='*50}")
    
    print(f"Basic imports: {'✅ PASS' if basic_imports else '❌ FAIL'}")
    print(f"Dependency imports: {'✅ PASS' if dependency_imports else '❌ FAIL'}")
    
    if basic_imports and dependency_imports:
        print("\n🎉 All import tests passed!")
        sys.exit(0)
    else:
        print("\n⚠️  Some import tests failed. Check the errors above.")
        sys.exit(1) 