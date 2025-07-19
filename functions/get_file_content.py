import os
from google.genai import types

from config import MAX_CHARS


def get_file_content(working_directory, file_path):
    abs_working_directory = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(abs_working_directory, file_path))

    # Ensure 'file_path' is within 'working_directory'.
    if not abs_file_path.startswith(abs_working_directory):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    # Ensure 'file_path' is a file type.
    if not os.path.isfile(abs_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    # Get file contents
    try:
        with open(abs_file_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)

            # Prevents passing large files to LLM to save on token usage
            if os.path.getsize(abs_file_path) > MAX_CHARS:
                file_content_string += (
                    f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                )

            return file_content_string
    except Exception as e:
        return f'Error reading file "{file_path}": {e}'


schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Returns contents of the specified file path as a string, constrained to the working directory. The string will be truncated at 10000 characters.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to get contents from, relative to the working directory",
            )
        },
        required=["file_path"],
    ),
)
