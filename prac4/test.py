from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables from .env
load_dotenv()

# Initialize Gemini chat model
model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.7,
)

prompt_A = "Suggest a unique name for a white cat"
prompt_B = "Give one creative cat name for a white-colored kitten"

response_A = model.invoke(prompt_A).content
response_B = model.invoke(prompt_B).content

print(f"Response A: {response_A}\n")
print(f"Response B: {response_B}")

