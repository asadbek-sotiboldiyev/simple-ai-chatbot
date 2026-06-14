from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.messages import SystemMessage, HumanMessage, AIMessage
import os

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL")

llm = ChatGoogleGenerativeAI(
    model=GEMINI_MODEL,
    api_key=GEMINI_API_KEY,
    vertexai=False
)

context: list[SystemMessage | AIMessage | HumanMessage] = [
    SystemMessage(content="You are a helpful assistant")
]

def ask(message: str):
    context.append(HumanMessage(content=message))
    response = llm.invoke(context)
    context.append(AIMessage(content=response.content))
    return response.content

if __name__ == "__main__":
    print("> main module file executed and llm initialized")
