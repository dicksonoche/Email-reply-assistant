from groq import Groq
import os
from dotenv import load_dotenv
from .prompts import REPLY_PROMPT, format_context

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    print("WARNING: GROQ_API_KEY not found in environment variables")
    client = None
else:
    client = Groq(api_key=api_key)

def generate_reply(query, contexts):
    if not client:
        # Fallback response when Groq is not available
        return "I apologize, but I'm unable to generate a response at the moment due to missing API configuration. Please check your Groq API key setup."
    
    try:
        context_str = format_context(contexts)
        prompt = REPLY_PROMPT.format(context=context_str, query=query)
        
        # Use openai/gpt-oss-20b model via Groq API
        try:
            response = client.chat.completions.create(
                model="openai/gpt-oss-20b",
                messages=[{"role": "system", "content": prompt}],
                max_tokens=1000
            )
            return response.choices[0].message.content
        except Exception as e:
            error_str = str(e).lower()
            if any(keyword in error_str for keyword in ["model_not_found", "does not exist", "quota", "insufficient_quota", "429"]):
                # Fallback to a simple template-based response
                print(f"Groq API error, using fallback: {str(e)}")
                return generate_fallback_reply(query, contexts)
            else:
                raise e
                
    except Exception as e:
        print(f"Error generating reply: {str(e)}")
        return f"I apologize, but I encountered an error while generating your response: {str(e)}"

def generate_fallback_reply(query, contexts):
    """Generate a simple reply when Groq is not available"""
    if not contexts:
        return f"Thank you for your inquiry about '{query}'. I'd be happy to help you with this issue. Please provide more details so I can assist you better."
    
    # Use the first context as a template
    context = contexts[0]
    return f"Based on similar past interactions, here's a helpful response to your query about '{query}': {context.get('response', 'I apologize, but I need more information to provide a specific response.')}"