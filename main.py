import os 
import sys
from google import genai
from dotenv import load_dotenv
from google.genai import types
from functions.get_files_info import get_files_info


def main():

    load_dotenv()

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    print("Arguments:", sys.argv)

    if len(sys.argv) < 2:
        print("Please provide a prompt as a command-line argument.")
        sys.exit(1)
    
    verbose_flag = False
    
    if len(sys.argv) == 3 and sys.argv[2] == "--verbose":
        verbose_flag=True
    

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
    
    if verbose_flag:
            print("User Prompt:", user_prompt)
            print("Prompt Tokens:", response.usage_metadata.prompt_token_count)
            print("Response Tokens:", response.usage_metadata.candidates_token_count)
    

print(get_files_info("calculator"))
# main()
    

