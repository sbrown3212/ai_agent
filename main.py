import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

from functions.call_function import call_function
from prompts import system_prompt
from available_functions import available_functions


def main():
    load_dotenv()

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    verbose = "--verbose" in sys.argv
    args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]

    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt goes here" [--verbose]')
        sys.exit(1)

    user_prompt = " ".join(args)

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    if verbose:
        print(f"User prompt: {user_prompt}\n")

    generate_content(client, messages, verbose)


def generate_content(client, messages, verbose):
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=system_prompt
        ),
    )

    if verbose:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    if response.function_calls:
        for function_call_part in response.function_calls:
            # QUESTION: Should this be in a 'try...catch' statement? How do I raise a fatal error?
            result = call_function(function_call_part, verbose)
            # print(f"call_function returned: {result}")
            # print(f"result.parts: {result.parts}")

            try:
                function_response = result.parts[
                    0
                ].function_response.response  # ignore warnings???
                if verbose:
                    print(f"-> {function_response}")
            except (IndexError, AttributeError):
                raise Exception("Function call did not return a valid response")
    else:
        print(response.text)


if __name__ == "__main__":
    main()
