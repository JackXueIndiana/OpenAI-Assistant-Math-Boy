import os
import time
import json
import requests
from openai import AzureOpenAI
  
client = AzureOpenAI(
    azure_endpoint = "https://xjxopenai.openai.azure.com/",
    api_key= "104a5aa356014d599d960a45c08d6847",
    api_version="2024-05-01-preview"
)

assistant = client.beta.assistants.create(
    model="gpt-35-turbo-16k", # replace with model deployment name.
    instructions="You are an AI assistant that can write code to help answer math question.",
    tools=[{"type":"code_interpreter"}],
    tool_resources={"code_interpreter":{"file_ids":[]}},
    temperature=1,
    top_p=1
)

# Create a thread
thread = client.beta.threads.create()

# Add a user question to the thread
message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="I need to solve the equation 3x + 11 = 14. Can you help me?" # Replace this with your prompt
)

      
  
# Run the thread
run = client.beta.threads.runs.create(
  thread_id=thread.id,
  assistant_id=assistant.id
)

# Looping until the run completes or fails
while run.status in ['queued', 'in_progress', 'cancelling']:
    time.sleep(1)
    run = client.beta.threads.runs.retrieve(
        thread_id=thread.id,
        run_id=run.id
    )

if run.status == 'completed':
  messages = client.beta.threads.messages.list(
    thread_id=thread.id
  )
  print(messages)
elif run.status == 'requires_action':
  # the assistant requires calling some functions
  # and submit the tool outputs back to the run
  pass
else:
  print(run.status)
