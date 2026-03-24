import os
import requests

# 1. API Configuration
API_KEY = os.getenv("HUGGINGFACE_API_KEY")
# THE NEW 2026 ROUTER URL (Mandatory to avoid 410 error)
API_URL = "https://router.huggingface.co/hf-inference/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# 2. Query Function
def query_api(prompt):
    """Query the Hugging Face Router with a prompt"""
    # Note: New router uses OpenAI-style message format
    payload = {
        "model": "Qwen/Qwen2.5-Coder-32B-Instruct", 
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 500
    }
    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        
        # Check for the 410 specifically to explain the fix
        if response.status_code == 410:
            return "Error 410: You are still hitting a retired endpoint. Ensure the URL is router.huggingface.co"
            
        response.raise_for_status() 
        result = response.json()
        return result['choices'][0]['message']['content']
        
    except Exception as e:
        return f"Error: {str(e)}"

# 3. Main Execution
if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    print("Querying Hugging Face Router...")
    result = query_api(user_prompt)
    print("\nResponse:")
    print(result)