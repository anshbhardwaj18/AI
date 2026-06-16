# FIRST METHOD(WITH intit_chat_model)
# from dotenv import load_dotenv

# load_dotenv()

# from langchain.chat_models import init_chat_model

# models = init_chat_model("google_genai:gemini-2.5-flash-lite")

# response = models.invoke("What is LLM")
# print(response.content)

# SECOND MEHOTD(WITH Model class)
from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
models = ChatGoogleGenerativeAI(model = "gemini-2.5-flash-lite")
# response = models.invoke("or kya hal chal hai!!")
# print(response.content)
# print(ChatGoogleGenerativeAI)
print(models)