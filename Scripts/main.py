import anthropic

def generate_documentation(system_prompt_path, user_prompt_path, code_path, output_path):
    # Initialize the Anthropoc client
    client = anthropic.Anthropic(
        api_key="....",  # Replace with your actual API key
    )
#
    # Load system prompt from file
    with open(system_prompt_path, 'r') as file:
        system_prompt = file.read()

    # Load user prompt template from file and replace code placeholder
    with open(user_prompt_path, 'r') as file:
        user_prompt_template = file.read()

    # Load code snippet from file
    with open(code_path, 'r') as file:
        read_code = file.read()

    # Replace code placeholder in user prompt template
    user_prompt = user_prompt_template.replace("{{code}}", read_code)

    # Generate documentation using Anthropoc API
    message = client.messages.create(
        model="claude-3-5-sonnet-20240620",  # Adjust model as needed
        max_tokens=1067,
        temperature=0,
        system=system_prompt,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": user_prompt
                    }
                ]
            }
        ]
    )

    # Save generated documentation to output path
    with open(output_path, 'w') as file:
        file.write(message.content)

# Example usage:
system_prompt_path = r'D:\Nethermind\TechnicalWriter\Prompts\system_prompt.txt'
user_prompt_path = r'D:\Nethermind\TechnicalWriter\Prompts\User_prompt.txt'
code_path = r'D:\Nethermind\TechnicalWriter\Tests\Test_Code.txt'
output_path = r'D:\Nethermind\TechnicalWriter\Document_generated\Document.txt'

generate_documentation(system_prompt_path, user_prompt_path, code_path, output_path)
