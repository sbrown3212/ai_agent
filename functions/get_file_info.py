import os


def get_files_info(working_directory, directory=None):
    project_root = os.getcwd()
    working_dir_path = os.path.abspath(os.path.join(project_root, working_directory))

    if not directory:
        directory = "."

    full_path = os.path.abspath(os.path.join(working_dir_path, directory))

    if not full_path.startswith(working_dir_path):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory.'

    if not os.path.isdir(full_path):
        return f'Error: "{directory}" is not a directory.'

    try:
        contents_info = []
        for item in os.listdir(full_path):
            item_path = os.path.join(full_path, item)
            name = item
            size = os.path.getsize(item_path)
            is_dir = os.path.isdir(item_path)

            contents_info.append(f"- {name}: file_size={size} bytes, is_dir={is_dir}")

        return "\n".join(contents_info)

    except Exception as e:
        return f"Error: Failed to get contents info. {e}"
