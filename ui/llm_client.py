# from llm_axe import OnlineAgent, OllamaChat
import ollama

class LLMClient:
    _HOST_URL = 'host.docker.internal:11434'
    _MODEL = 'gemma3:1b'

    def __init__(self):
        self._client = ollama.Client(host=LLMClient._HOST_URL)
        # self._client = OnlineAgent(OllamaChat(host=LLMClient._HOST_URL, model=LLMClient._MODEL))

    def ask(self, messages):
        # return self._client.generate(model=LLMClient._MODEL, prompt=prompt)['response']
        return self._client.chat(model=LLMClient._MODEL, messages=messages)['message']['content']
        # return self._client.search(messages[-1]['content'])