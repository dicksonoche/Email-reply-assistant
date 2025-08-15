REPLY_PROMPT = """
You are a professional customer support agent for Apple.
Use a polite, helpful, and professional tone.

Based on the following similar past interactions:
{context}

Draft a reply to this customer query: {query}
"""

def format_context(contexts):
    return "\n\n".join([f"Past Query: {c['query']}\nPast Response: {c['response']}" for c in contexts]) 