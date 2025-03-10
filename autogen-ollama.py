from autogen_ext.models.ollama import OllamaChatCompletionClient
from autogen_core.models import UserMessage
from autogen_core.clients import ChatCompletionClient  # Updated import

ollama_client = ChatCompletionClient(
    model="llama3.2",
)

result = ollama_client.create([UserMessage(content="What is the capital of France?", source="user")])  # type: ignore
print(result)