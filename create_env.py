#!/usr/bin/env python3

# Create .env file with proper UTF-8 encoding
env_content = """# LiveKit Configuration
LIVEKIT_API_KEY=APIHKZQUWmcYHG5
LIVEKIT_API_SECRET=your_livekit_api_secret_here

# OpenAI Configuration
OPENAI_API_KEY=your_openai_api_key_here

# Agent Configuration
LIVEKIT_URL=wss://aiadvisor-hdtqljyi.livekit.cloud
"""

# Remove the old .env file and create a new one
import os
if os.path.exists('.env'):
    os.remove('.env')

with open('.env', 'w', encoding='utf-8') as f:
    f.write(env_content)

print("✅ .env file created successfully!")
print("Please edit the .env file to add your actual API keys:")
print("1. Replace 'your_livekit_api_secret_here' with your LiveKit API secret")
print("2. Replace 'your_openai_api_key_here' with your OpenAI API key")
print("\nCurrent .env content:")
with open('.env', 'r', encoding='utf-8') as f:
    print(f.read()) 