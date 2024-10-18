import google.generativeai as genai
import os
from dotenv import load_dotenv
import json


load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


def review_code_for_clean_principles(code_string:str):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content("You are code reviewer focusing on clean code principles." +
                          "Review the following code and rewrite it to improve readability,"+
                          "maintainability, and best practices. Respond with the revised code"+
                          "in JSON format.\n\nCode to review:\n" + code_string + "\n\nRate the code "+
                         "on a scale of 1-10 for readability, maintainability, and best practices." +
                        "\n\nExample response in JSON format:\n{\n    \"code\": \"public class Main "+
                        "{\\n    public static void main(String[] args) {\\n "+
                        "System.out.println(\\\"Hello, World!\\\");\\n    }\\n}\",\n    \"rating\": 10\n}")
    return response.text