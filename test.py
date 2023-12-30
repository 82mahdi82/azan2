# A simple example of using EdgeGPT library
from edgegpt import EdgeGPT

# Create an instance of EdgeGPT class
gpt = EdgeGPT()

# Set the chat mode to creative
gpt.set_chat_mode("creative")

# Ask Bing to write a poem about love
gpt.send_message("Hey Bing, write a poem about love")

# Get the response from Bing
response = gpt.get_response()

# Print the response
print(response)
