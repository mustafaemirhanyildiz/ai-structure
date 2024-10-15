# This file contains the English language prompts for the GPT model.

def build_chat_prompt_user(user_input: str) -> tuple[str, str]: 
    rate_code = f"\n\nRate the code on a scale of 1-10 for readability, maintainability, and best practices."
    
    example_response_as_json_str_java = """
    {
        "code": "public class Main {\\n    public static void main(String[] args) {\\n        System.out.println(\\\"Hello, World!\\\");\\n    }\\n}",
        "rating": 10
    }
    """

    user_prompt = f"\n\nCode to review:\n{user_input}\n" + rate_code + f"\n\nExample response in JSON format:\n{example_response_as_json_str_java}"

    return user_prompt

def build_chat_prompt_system() -> str:
    system_prompt = (
        "You are a code reviewer focusing on clean code principles. Review the following code "
        "and rewrite it to improve readability, maintainability, and best practices. "
        "Respond with the revised code in JSON format."
    )
    
    return system_prompt

