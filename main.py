import os
import sys
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


def main():
    if len(sys.argv) != 2:
        print("Unable to find prompt. Please include a single prompt in quotation marks in the command following the file name.")
        sys.exit(1)

    contents = sys.argv[1]
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', contents=contents
    )

    print(response.text)
    print(f'Prompt tokens: {response.usage_metadata.prompt_token_count}')
    print(f'Response tokens: {response.usage_metadata.candidates_token_count}')
    


if __name__ == "__main__":
    main()
