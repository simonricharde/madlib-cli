from textwrap import dedent
import re

welcome_message = """
**************************************
Hello! Let's write a story. I'm going to prompt you for some parts
of speech and after I've everything I need, I'll tell you the
resulting story
**************************************
"""


def greeting():
    """Greet the user and provide instructions."""
    print(welcome_message)

def read_file(file_path):
    """Read the file path and return the data as string."""
    with open(file_path, 'r') as file:
        return file.read()

def write_file(file_path, output_content):
    """Write a file with the output contents at the given file path."""
    with open(file_path, 'w') as file:
        return file.write(output_content)

def get_templates(file_contents):
    """
    split the parts of speech that needs to be modified.
    """
    template_list = []
    end_position = 0
    braces_count = file_contents.count('{')
    for i in range(braces_count):
        start_position = file_contents.find('{', end_position) + 1
        end_position = file_contents.find('}', start_position)
        template = file_contents[start_position:end_position]
        template_list.append(template)
    return template_list

def remove_templates(file_contents):
    """
    Remove the parts of speech from the original content.
    """
    regex = r"\{.*?\}"
    input_contents = re.sub(regex, '{}', file_contents)
    return input_contents


def get_response(template, response_list):
    """User is prompted with the received template.

    Response list updated with user inputs.
    """
    user_response = input(f"Enter an {template}: ")
    response_list.append(user_response)
    


def user_responses(templates):
    """
    Responses received from the user
    """
    response_list = []

    for template in templates:
        get_response(template, response_list)

    return response_list

def result_story(file_contents):
    """
        Read the input contents and split the templates
        Remove the templates from the input contents.
        Prompt the user with the template list
        Get the user inputs and prepare the result contents
    """
    templates = get_templates(file_contents)
    input_contents = remove_templates(file_contents)
    responses = user_responses(templates)
    result_contents = input_contents.format(*responses)
    print(dedent(f"""
    ******************************************
    Here is the resulting story:
    {result_contents}
    ******************************************
    """))
    return result_contents

if __name__ == "__main__":
    greeting()
    file_contents = read_file('assets/sample_template.txt')
    result_contents = result_story(file_contents)
    write_file('assets/result_template.txt', result_contents)