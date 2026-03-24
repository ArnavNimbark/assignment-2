import os
from openai import OpenAI

# 1. API Configuration
# Initialize the client using the environment variable
# If you haven't set it yet, run: $env:OPENAI_API_KEY="your-key" in PowerShell
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 2. Query Function
def query_api(prompt):
    """Query the OpenAI API with a prompt"""
    try:
        # We'll use gpt-3.5-turbo or gpt-4o-mini for cost-efficiency
        response = client.chat.completions.create(
            model="gpt-4o-mini", 
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

# 3. Main Execution
if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    print("Querying OpenAI API...")
    
    result = query_api(user_prompt)
    
    print("\nResponse:")
    print(result)