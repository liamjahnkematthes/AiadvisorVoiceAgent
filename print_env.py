import os
from dotenv import load_dotenv

load_dotenv()

print('OPENAI_API_KEY:', os.getenv('OPENAI_API_KEY'))
print('LIVEKIT_API_KEY:', os.getenv('LIVEKIT_API_KEY'))
print('LIVEKIT_API_SECRET:', os.getenv('LIVEKIT_API_SECRET'))
print('LIVEKIT_URL:', os.getenv('LIVEKIT_URL')) 