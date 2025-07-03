#!/usr/bin/env python3

import asyncio
import os
from dotenv import load_dotenv
from livekit import api

# Load environment variables
load_dotenv()

async def test_agent_connection():
    """Test if the agent is properly connected to LiveKit"""
    
    print("🔍 Testing Agent Connection to LiveKit...")
    
    # Check environment variables
    api_key = os.getenv('LIVEKIT_API_KEY')
    api_secret = os.getenv('LIVEKIT_API_SECRET')
    livekit_url = os.getenv('LIVEKIT_URL')
    
    print(f"✅ API Key: {api_key[:10]}..." if api_key else "❌ API Key missing")
    print(f"✅ API Secret: {api_secret[:10]}..." if api_secret else "❌ API Secret missing")
    print(f"✅ LiveKit URL: {livekit_url}")
    
    if not all([api_key, api_secret, livekit_url]):
        print("❌ Missing required environment variables")
        return
    
    try:
        # Test token creation
        print("\n🧪 Testing token creation...")
        test_room_name = "test-connection-room"
        
        # Create access token for testing (using grants dict)
        at = api.AccessToken(api_key, api_secret)
        at.identity = "test-user"
        at.grants = {
            "video": {
                "roomJoin": True,
                "room": test_room_name
            }
        }
        token = at.to_jwt()
        
        print(f"✅ Test token created successfully")
        print(f"✅ Token preview: {token[:50]}...")
        
        # Test WebSocket connection
        print("\n🔌 Testing WebSocket connection...")
        import websockets
        
        # Convert wss:// to ws:// for testing
        ws_url = livekit_url.replace('wss://', 'ws://') + f"?access_token={token}"
        
        try:
            async with websockets.connect(ws_url, timeout=10) as websocket:
                print("✅ WebSocket connection established!")
                
                # Send a simple ping
                await websocket.ping()
                print("✅ WebSocket ping successful!")
                
        except Exception as ws_error:
            print(f"⚠️ WebSocket connection failed: {ws_error}")
            print("This might be normal if the agent isn't ready to accept connections yet.")
        
        print("\n🎉 Agent connection test completed!")
        print("If the agent is running properly, it should accept WebSocket connections.")
        
    except Exception as e:
        print(f"❌ Error testing agent connection: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test_agent_connection()) 