def build_combined_prompt(user_input: str) -> str:
    rate_code = "\n\nRate the code on a scale of 1-10 for readability, maintainability, and best practices."
    
    example_response_as_json_str_java = """
    {
        "code": "public class Main {\\n    public static void main(String[] args) {\\n        System.out.println(\\\"Hello, World!\\\");\\n    }\\n}",
        "rating": 10
    }
    """

    combined_prompt = (
        "You are a code reviewer focusing on clean code principles. Review the following code "
        "and rewrite it to improve readability, maintainability, and best practices. "
        "Respond with the revised code in JSON format.\n\n"
        f"Code to review:\n{user_input}\n" + rate_code +
        f"\n\nExample response in JSON format:\n{example_response_as_json_str_java}"
    )
    
    return combined_prompt
