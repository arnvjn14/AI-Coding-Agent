import os 
import sys
from google import genai
from dotenv import load_dotenv
from google.genai import types


def main():

    load_dotenv()

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    print("Arguments:", sys.argv)

    if len(sys.argv) < 2:
        print("Please provide a prompt as a command-line argument.")
        sys.exit(1)

    user_prompt = sys.argv[1]

    messages= [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]


    response = client.models.generate_content(
        model='gemini-2.0-flash-001', contents=messages
    )

    print(response.text)
    if response is None or response.usage_metadata is None:
        print("No response or usage metadata found.")
        return
    
    print("Prompt Tokens:", response.usage_metadata.prompt_token_count)
    print("Completion Tokens:", response.usage_metadata.candidates_token_count)

main()
    

