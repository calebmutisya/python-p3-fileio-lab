#Write the given content to a text file.

    # Args:
    # - file_name (str): The name of the file, including the file extension.
    # - file_content (str): The content to be written to the file.
def write_file(file_name, file_content):
    with open(f"{file_name}.txt",'w') as file:
        file.write(file_content)
# Append the given content to a text file.

#     Args:
#     - file_name (str): The name of the file, including the file extension.
#     - file_content (str): The content to be appended to the file.
def append_file(file_name, append_content):
    with open(f"{file_name}.txt",'a') as file:
        file.write(append_content)
# Read and return the content of a text file.

#     Args:
#     - file_name (str): The name of the file, including the file extension.

#     Returns:
#     - str: The content of the file.
def read_file(file_name):
    with open(f"{file_name}.txt",'r') as file:
        content= file.read()
    return content
