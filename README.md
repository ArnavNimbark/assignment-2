Done all questions from assignment except 1
took very long, some were tricky and some were very hard to do put i was able to put them together

AI API Integration Project
Generative AI Assignment - CampusPe

Project Description
This project demonstrates the integration of six different Generative AI providers using Python. The goal is to create a modular system where each AI service can be queried individually using environment variables for secure API key management.

## Setup Instructions
1. Clone the Repository: Ensure you are in your existing GitHub repository used for previous assignments.
2. Install Python: Ensure Python 3.10+ is installed (this project was tested on Python 3.14).
3. Install Dependencies: Run the following command to install all required libraries:
   powershell
   pip install -r requirements.txt
   

How to Obtain API Keys 
* OpenAI: Sign up at [platform.openai.com](https://platform.openai.com/).
* Groq: Obtain a key from [console.groq.com](https://console.groq.com/).
* Ollama: Download the software locally from [ollama.ai](https://ollama.ai/).
* Hugging Face: Create a token at [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens).
* Google Gemini:Generate a key at [makersuite.google.com](https://makersuite.google.com/app/apikey).
* Cohere: Sign up at [dashboard.cohere.com](https://dashboard.cohere.com/).

How to Run the Programs 
Before running any script, you must set your API keys as environment variables in your terminal to ensure they are not hardcoded. 

Windows PowerShell Examples:
powershell
$env:OPENAI_API_KEY="your_key_here" 
$env:GOOGLE_API_KEY="your_key_here"

Run a specific provider:
powershell
python openai_example.py
python gemini_example.py


Project Structure
* openai_example.py: Queries OpenAI GPT models.
* groq_example.py: Queries Groq Llama models.
* ollama_example.py: Queries local Ollama models.
* huggingface_example.py: Queries Hugging Face models via the 2026 Router.
* gemini_example.py: Queries Google Gemini.
* cohere_example.py: Queries Cohere models.
* requirements.txt: List of Python dependencies].
* screenshots/: Folder containing output verification for each API

Was unable to complete hugging face and openAI 
Hugging face: No working API
OpenAi: requires payment
