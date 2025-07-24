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

    # Print usage suggestions and exit if not 'args' are provided.
    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt goes here" [--verbose]')
        sys.exit(1)

    # Add user prompt to 'messages'
    user_prompt = " ".join(args)
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    if verbose:
        print(f"User prompt: {user_prompt}\n")

    # Loop prevent excessive LLM requests
    count = 0
    while count < 20:
        count += 1
        try:
            response = generate_content(client, messages, verbose)

            # Display final message.
            # (having 'response.text' after 'response.function_calls'
            # prevents "non-text parts" warning from API)
            if not response.function_calls and response.text:
                print("Final response:")
                print(response.text)
                break
        except Exception as e:
            print(f"Error: Failed to generate content: {e}")
            break


def generate_content(client, messages, verbose):
    # Makes call to API and gets response.
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=system_prompt
        ),
    )

    # Append candidates to 'messages'
    for candidate in response.candidates:
        messages.append(candidate.content)

    if verbose:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    if response.function_calls:
        # List for validation
        function_responses = []
        for function_call_part in response.function_calls:
            function_call_result = call_function(function_call_part, verbose)

            # Ensure function call is valid
            if (
                not function_call_result.parts
                or not function_call_result.parts[0].function_response
            ):
                raise Exception("Function call did not return a valid response.")
            if verbose:
                print(f"-> {function_call_result.parts[0].function_response.response}")

            function_responses.append(function_call_result.parts[0])

            # Append 'tool' to 'messages'
            function_call_content = types.Content(
                parts=function_call_result.parts, role="tool"
            )
            messages.append(function_call_content)

        # Validate that function responses were generated.
        if not function_responses:
            raise Exception("No function responses were generated")

    return response


if __name__ == "__main__":
    main()
