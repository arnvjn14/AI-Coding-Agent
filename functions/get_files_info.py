import os

def get_files_info(working_directory, directory=None):

    abs_working_directory = os.path.abspath(working_directory)

    if directory is None:
        directory = working_directory
    abs_directory = os.path.abspath(directory)
    if not abs_directory.startswith(abs_working_directory):
        raise ValueError("The specified directory is outside the working directory.")
    
    final_response=""
    contents=os.listdir(abs_directory)
    for content in contents:
        content_path=os.path.join(abs_directory,content)
        is_dir=os.path.isdir(content_path)
        size=os.path.getsize(content_path)
        final_response+=f" - {content}: file_size={size} bytes, is_dir={is_dir}\n"

    return final_response



