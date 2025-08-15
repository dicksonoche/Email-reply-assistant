#!/usr/bin/env python3
"""
Comprehensive test runner for Email Reply Drafter application.
Runs all test modules and provides a summary of results.
"""

import sys
import os
import subprocess
import time

# Add the project root to the Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

def run_test_module(module_name):
    """Run a specific test module and return the result."""
    print(f"\n{'='*50}")
    print(f"Running {module_name}...")
    print(f"{'='*50}")
    
    start_time = time.time()
    
    try:
        # Run the test module as a subprocess
        result = subprocess.run([
            sys.executable, 
            os.path.join(os.path.dirname(__file__), f"{module_name}.py")
        ], capture_output=True, text=True, cwd=project_root)
        
        execution_time = time.time() - start_time
        
        if result.returncode == 0:
            print(f"✅ {module_name} completed successfully in {execution_time:.2f}s")
            print("Output:")
            print(result.stdout)
            return True
        else:
            print(f"❌ {module_name} failed with return code {result.returncode}")
            print("Error output:")
            print(result.stderr)
            if result.stdout:
                print("Standard output:")
                print(result.stdout)
            return False
            
    except Exception as e:
        print(f"❌ Error running {module_name}: {str(e)}")
        return False

def run_import_test():
    """Test basic import functionality."""
    print(f"\n{'='*50}")
    print("Testing basic imports...")
    print(f"{'='*50}")
    
    try:
        # Test core module imports
        from app.retrieval import retrieve_similar
        print("✅ app.retrieval imported successfully")
        
        from app.generation import generate_reply
        print("✅ app.generation imported successfully")
        
        from app.prompts import REPLY_PROMPT, format_context
        print("✅ app.prompts imported successfully")
        
        from app.main import app
        print("✅ app.main imported successfully")
        
        return True
        
    except Exception as e:
        print(f"❌ Import test failed: {str(e)}")
        return False

def main():
    """Main test runner function."""
    print("🧪 Email Reply Drafter - Test Suite")
    print("="*50)
    
    start_time = time.time()
    test_results = []
    
    # Test 1: Basic imports
    test_results.append(("Import Test", run_import_test()))
    
    # Test 2: API functionality
    test_results.append(("API Test", run_test_module("test_api")))
    
    # Test 3: ChromaDB functionality
    test_results.append(("ChromaDB Test", run_test_module("test_chromadb")))
    
    # Summary
    total_time = time.time() - start_time
    passed = sum(1 for _, result in test_results if result)
    total = len(test_results)
    
    print(f"\n{'='*50}")
    print("TEST SUMMARY")
    print(f"{'='*50}")
    
    for test_name, result in test_results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{test_name}: {status}")
    
    print(f"\nResults: {passed}/{total} tests passed")
    print(f"Total execution time: {total_time:.2f}s")
    
    if passed == total:
        print("\n🎉 All tests passed! Your application is ready to use.")
        return 0
    else:
        print(f"\n⚠️  {total - passed} test(s) failed. Please check the errors above.")
        return 1

if __name__ == "__main__":
    sys.exit(main()) 