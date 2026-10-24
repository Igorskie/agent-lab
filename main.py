import os

from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()
client = Anthropic()  # reads ANTHROPIC_API_KEY from the environment

resp = client.messages.create(
    model=os.getenv("MODEL", "claude-haiku-5-5"),
    max_tokens=200,
    messages=[{"role": "user", "content": "In one sentence, what is an AI agent?"}],
)

print(resp.content[0].text)
print(f"\nTokens: in={resp.usage.input_tokens} out={resp.usage.output_tokens}")
