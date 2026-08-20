from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq

from dotenv import load_dotenv
load_dotenv()

def get_llm(model_name):

    if model_name == "openai":
        return ChatOpenAI(
            model="gpt-4o-mini"
        )

    elif model_name == "gemini":
        return ChatGoogleGenerativeAI(
            model="gemini-1.5-flash"
        )
    
    elif model_name == "groq":
        return ChatGroq(
            model="llama-3.3-70b-versatile"
        )
    
    else:
        raise ValueError("Unsupported model")

