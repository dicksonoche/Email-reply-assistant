#!/usr/bin/env python3
import sys
import os

# Add the project root to the Python path to resolve imports
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

def test_imports():
    try:
        print("Testing imports...")
        from app.retrieval import retrieve_similar
        print("✅ retrieval module imported successfully")
        
        from app.generation import generate_reply
        print("✅ generation module imported successfully")
        
        return True
    except Exception as e:
        print(f"❌ Import error: {str(e)}")
        return False

def test_retrieval():
    try:
        print("\nTesting retrieval...")
        from app.retrieval import retrieve_similar
        
        contexts = retrieve_similar("My iPhone battery is draining too fast")
        print(f"✅ Retrieved {len(contexts)} contexts")
        print(f"📝 Sample context: {contexts[0] if contexts else 'None'}")
        
        return True
    except Exception as e:
        print(f"❌ Retrieval error: {str(e)}")
        return False

def test_generation():
    try:
        print("\nTesting generation...")
        from app.generation import generate_reply
        
        # Mock contexts for testing
        mock_contexts = [{'query': 'test query', 'response': 'test response'}]
        
        reply = generate_reply("My iPhone battery is draining too fast", mock_contexts)
        print(f"✅ Generated reply: {reply[:100]}...")
        
        return True
    except Exception as e:
        print(f"❌ Generation error: {str(e)}")
        return False

if __name__ == "__main__":
    print("Testing API components...")
    
    if test_imports():
        test_retrieval()
        test_generation()
    
    print("\nTest completed!") 