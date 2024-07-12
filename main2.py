from dotenv import load_dotenv

load_dotenv()
api_key = os.environ["MISTRAL_API_KEY"]
from llama_index.core.agent import ReActAgent
from llama_index.llms.openai import OpenAI
from llama_index.core.tools import FunctionTool
import logging
import sys
#these two lines are used for debugging and watching what's happening in the background
# logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
# logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader,Settings
from llama_index.llms.mistralai import MistralAI
from llama_index.embeddings.mistralai.base import MistralAIEmbedding
from llama_index.core import ServiceContext
import os
from dotenv import load_dotenv
from llama_parse import LlamaParse
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
import requests
import numpy as np
import os
from getpass import getpass
from llama_index.tools.code_interpreter.base import CodeInterpreterToolSpec

def multiply(a: float, b: float) -> float:
    """Multiply two numbers and returns the product"""
    return a * b

multiply_tool = FunctionTool.from_defaults(fn=multiply)
def add(a: float, b: float) -> float:
    """Add two numbers and returns the sum"""
    return a + b

add_tool = FunctionTool.from_defaults(fn=add)

Settings.llm = MistralAI(model="mistral-medium", api_key=api_key)
Settings.embed_model = MistralAIEmbedding(model_name='mistral-embed', api_key=api_key)

code_spec = CodeInterpreterToolSpec()
tools = code_spec.to_tool_list() + [multiply_tool, add_tool]


agent = ReActAgent.from_tools(tools, verbose=True)
# response = agent.chat("write a python code that make the sum of 5+5")
# print(response)
