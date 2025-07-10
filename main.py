import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types


def main():
    load_dotenv()

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    args = sys.argv[1:]

    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt goes here"')
        sys.exit(1)

    # flags = ["--verbose", "-v"]

    verbose = False
    
    parse_flags = True
    prompt_args = []
    for arg in args:
        if arg == "--":
            parse_flags = False
            continue
        if parse_flags and (arg == "--verbose" or arg == "-v"):
            verbose = True
        else:
            prompt_args.append(arg)

    if len(prompt_args) == 0:
        print("Please provide a prompt.")
        print('Usage: python main.py "your prompt goes here"')
        sys.exit(1)

    user_prompt = " ".join(prompt_args)

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    response = client.models.generate_content(
        model='gemini-2.0-flash-001', contents=messages
    )

    if verbose:
        print(f'User prompt: {user_prompt}\n')

    print(response.text)

    if verbose:
        print(f'\nPrompt tokens: {response.usage_metadata.prompt_token_count}')
        print(f'Response tokens: {response.usage_metadata.candidates_token_count}')


if __name__ == "__main__":
    main()
