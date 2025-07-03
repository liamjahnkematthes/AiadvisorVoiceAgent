from flask import Flask, request, jsonify
from flask_cors import CORS
from livekit import api
import os
from dotenv import load_dotenv
from datetime import timedelta

load_dotenv()

app = Flask(__name__)
CORS(app)

@app.route('/token', methods=['GET'])
def get_token():
    room = request.args.get('room', 'demo-room')
    identity = request.args.get('identity', 'user')
    
    # Get LiveKit credentials from environment
    api_key = os.getenv('LIVEKIT_API_KEY')
    api_secret = os.getenv('LIVEKIT_API_SECRET')
    
    if not api_key or not api_secret:
        return jsonify({'error': 'LiveKit credentials not found'}), 500
    
    try:
        # Generate token
        token = (
            api.AccessToken(api_key, api_secret)
            .with_identity(identity)
            .with_grants(
                api.VideoGrants(
                    can_publish=True,
                    can_subscribe=True,
                    room_join=True,
                    room=room
                )
            )
            .with_ttl(timedelta(hours=1))  # 1 hour
            .to_jwt()
        )
        
        return jsonify({'token': token})
    except Exception as e:
        return jsonify({'error': f'Token generation failed: {str(e)}'}), 500

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    print("Starting token server on port 5001...")
    print(f"LiveKit URL: {os.getenv('LIVEKIT_URL')}")
    print(f"API Key: {os.getenv('LIVEKIT_API_KEY', 'Not set')[:10]}...")
    app.run(host='0.0.0.0', port=5001, debug=True) 