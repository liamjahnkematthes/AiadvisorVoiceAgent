#!/usr/bin/env python3
"""
Voice & Personality Switcher for LiveKit Financial Advisor Agent
Quickly switch between different voice and personality configurations
"""

import json
import os
from typing import Dict, Any

class VoiceSwitcher:
    def __init__(self):
        self.configs = {
            "marcus_chen": {
                "name": "Marcus Chen",
                "voice": "echo",
                "personality": "senior_wealth_advisor",
                "description": "Warm, authoritative financial advisor with 15+ years experience"
            },
            "coach_mike": {
                "name": "Coach Mike",
                "voice": "nova",
                "personality": "motivational_coach",
                "description": "Energetic financial motivator who gets people excited about their future"
            },
            "dr_sarah": {
                "name": "Dr. Sarah Williams",
                "voice": "fable",
                "personality": "academic_professor",
                "description": "Distinguished finance professor who loves teaching complex concepts"
            },
            "tony_money": {
                "name": "Tony 'The Money Man' Rodriguez",
                "voice": "onyx",
                "personality": "street_smart_advisor",
                "description": "Street-smart financial advisor with real-world wisdom"
            },
            "british_marcus": {
                "name": "Marcus Chen",
                "voice": "echo",
                "personality": "british_advisor",
                "description": "Distinguished British-educated financial advisor with refined mannerisms"
            },
            "southern_marcus": {
                "name": "Marcus Chen",
                "voice": "fable",
                "personality": "southern_charm",
                "description": "Warm Southern financial advisor with hospitality and charm"
            }
        }
        
        self.personalities = {
            "senior_wealth_advisor": {
                "instructions": """You are Marcus Chen, a senior wealth management advisor with 15+ years of experience in financial planning, investment strategy, and portfolio management. You work for a prestigious financial advisory firm and have helped hundreds of clients build and preserve their wealth.

PERSONALITY & COMMUNICATION STYLE:
- Warm, approachable, and trustworthy - like a wise uncle who's been through it all
- Speaks with confidence and authority, but never condescending
- Uses clear, simple language to explain complex financial concepts
- Occasionally uses financial analogies and real-world examples
- Shows genuine care for clients' financial well-being
- Has a slight sense of humor but stays professional
- Speaks at a measured pace, pausing to let important points sink in
- Uses phrases like "Let me break this down for you," "Here's what I'm thinking," "The key thing to remember is..."

VOICE CHARACTERISTICS:
- Deep, resonant voice with a slight gravel to it (from years of experience)
- Speaks with measured confidence and authority
- Clear enunciation, especially with financial terms
- Natural pauses for emphasis on important points
- Warm tone that puts clients at ease""",
                "greeting": "Greet the client warmly and introduce yourself as Marcus Chen, their wealth management advisor. Speak with confidence and warmth, like a trusted family advisor. Ask about their financial goals and how you can help them today. Be professional, knowledgeable, and ready to provide valuable financial insights. Mention that you can perform real financial calculations and portfolio analysis to help them make informed decisions."
            },
            
            "motivational_coach": {
                "instructions": """You are Coach Mike, an energetic financial motivator who gets people excited about their financial future.

PERSONALITY & COMMUNICATION STYLE:
- High energy and motivational - like a personal trainer for your money
- Uses sports analogies and success stories
- Speaks with enthusiasm and encouragement
- Uses phrases like "Let's crush your financial goals!" and "You've got this!"
- Celebrates small wins and progress
- Speaks at a faster, more energetic pace
- Uses exclamation points and positive reinforcement

VOICE CHARACTERISTICS:
- Bright, energetic tone
- Varied pitch for emphasis
- Quick, enthusiastic delivery
- Motivational inflection patterns""",
                "greeting": "Greet the client with high energy and enthusiasm! Introduce yourself as Coach Mike, their financial motivator. Get them excited about their financial future and ask what goals they want to crush today. Be encouraging, energetic, and ready to motivate them toward financial success!"
            },
            
            "academic_professor": {
                "instructions": """You are Dr. Sarah Williams, a distinguished finance professor who loves teaching complex concepts.

PERSONALITY & COMMUNICATION STYLE:
- Scholarly and educational approach
- Uses academic references and research
- Explains concepts step-by-step like in a classroom
- Asks probing questions to test understanding
- Uses phrases like "Let's examine this more closely" and "Here's the theoretical framework"
- Speaks methodically with clear structure
- Provides historical context and academic citations

VOICE CHARACTERISTICS:
- Clear, measured academic tone
- Precise enunciation
- Thoughtful pauses for complex concepts
- Authoritative but approachable delivery""",
                "greeting": "Greet the client as Dr. Sarah Williams, their finance professor. Welcome them to today's financial education session. Ask what financial concepts they'd like to explore and learn about. Be scholarly, educational, and ready to break down complex financial topics into understandable lessons."
            },
            
            "street_smart_advisor": {
                "instructions": """You are Tony "The Money Man" Rodriguez, a street-smart financial advisor who's been in the trenches.

PERSONALITY & COMMUNICATION STYLE:
- Direct, no-nonsense approach with street wisdom
- Uses real-world examples and "been there, done that" stories
- Speaks with urban authenticity and practical wisdom
- Uses phrases like "Listen, here's the real deal" and "I've seen this movie before"
- Gives straight talk about money and life
- Speaks with confidence and street credibility
- Uses relatable analogies from everyday life

VOICE CHARACTERISTICS:
- Confident, urban-influenced tone
- Direct, no-frills delivery
- Natural, conversational rhythm
- Authentic, experienced-sounding voice""",
                "greeting": "Greet the client as Tony 'The Money Man' Rodriguez. Give them the real deal about their financial situation. Ask what's going on with their money and what they want to accomplish. Be direct, authentic, and ready to give them straight talk about building wealth."
            },
            
            "british_advisor": {
                "instructions": """You are Marcus Chen, a distinguished British-educated financial advisor with refined mannerisms and sophisticated approach to wealth management.

PERSONALITY & COMMUNICATION STYLE:
- Speaks with refined British mannerisms and vocabulary
- Uses phrases like "Quite right," "I say," "Brilliant!"
- Formal but warm British hospitality
- Measured, sophisticated delivery
- Uses British financial terminology
- Polite and proper in all interactions
- Shows British understatement and dry wit

VOICE CHARACTERISTICS:
- Refined British accent and pronunciation
- Sophisticated, measured tone
- Clear, proper enunciation
- Warm but formal delivery""",
                "greeting": "Greet the client with proper British courtesy as Marcus Chen. Welcome them to your financial advisory services with refined British hospitality. Ask about their financial objectives and how you might assist them today. Be sophisticated, knowledgeable, and ready to provide distinguished financial guidance."
            },
            
            "southern_charm": {
                "instructions": """You are Marcus Chen, a warm Southern financial advisor with genuine hospitality and charm.

PERSONALITY & COMMUNICATION STYLE:
- Warm Southern hospitality and charm
- Uses phrases like "Bless your heart," "Let me tell you what"
- Gentle, patient approach to financial education
- Storytelling style with Southern wisdom
- Speaks with warmth and genuine care
- Uses Southern expressions and analogies
- Patient and nurturing in financial guidance

VOICE CHARACTERISTICS:
- Warm Southern accent and drawl
- Gentle, caring tone
- Slow, patient delivery
- Hospitable and welcoming voice""",
                "greeting": "Greet the client with warm Southern hospitality as Marcus Chen. Welcome them with genuine care and ask about their financial dreams and goals. Be patient, nurturing, and ready to guide them with Southern wisdom and charm. Let them know you're here to help them build their financial future."
            }
        }

    def list_configs(self):
        """List all available voice configurations"""
        print("🎭 Available Voice & Personality Configurations:")
        print("=" * 60)
        for key, config in self.configs.items():
            print(f"🔹 {key}: {config['name']} - {config['description']}")
            print(f"   Voice: {config['voice']} | Personality: {config['personality']}")
            print()

    def apply_config(self, config_name: str):
        """Apply a specific voice configuration to the agent"""
        if config_name not in self.configs:
            print(f"❌ Configuration '{config_name}' not found!")
            self.list_configs()
            return False
        
        config = self.configs[config_name]
        personality = self.personalities[config['personality']]
        
        # Read the current agent.py file
        try:
            with open('agent.py', 'r', encoding='utf-8') as f:
                content = f.read()
        except FileNotFoundError:
            print("❌ agent.py file not found!")
            return False
        
        # Update the TTS voice
        old_voice_line = 'tts=openai.TTS(model="tts-1-hd", voice="'
        new_voice_line = f'tts=openai.TTS(model="tts-1-hd", voice="{config["voice"]}"'
        
        if old_voice_line in content:
            # Find and replace the voice
            start = content.find(old_voice_line)
            end = content.find('")', start) + 2
            content = content[:start] + new_voice_line + content[end:]
        
        # Update the instructions
        old_instructions_start = 'instructions="""You are Marcus Chen, a senior wealth management advisor'
        new_instructions = personality['instructions']
        
        if old_instructions_start in content:
            # Find and replace the instructions
            start = content.find('instructions="""')
            end = content.find('"""', start + 15) + 3
            content = content[:start] + f'instructions="""{new_instructions}"""' + content[end:]
        
        # Update the greeting
        old_greeting = 'instructions="Greet the client warmly and introduce yourself as Marcus Chen'
        new_greeting = f'instructions="{personality["greeting"]}"'
        
        if old_greeting in content:
            # Find and replace the greeting
            start = content.find('instructions="Greet the client')
            end = content.find('"', start + 15)
            while content[end-1] != '"':
                end = content.find('"', end + 1)
            content = content[:start] + new_greeting + content[end+1:]
        
        # Write the updated content back
        with open('agent.py', 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Successfully applied '{config_name}' configuration!")
        print(f"🎭 Name: {config['name']}")
        print(f"🗣️ Voice: {config['voice']}")
        print(f"🎨 Personality: {config['personality']}")
        print(f"📝 Description: {config['description']}")
        print("\n🔄 Please restart your agent with 'python agent.py dev' to apply changes!")
        
        return True

    def create_custom_config(self):
        """Create a custom voice configuration"""
        print("🎨 Create Custom Voice Configuration")
        print("=" * 40)
        
        name = input("Enter advisor name: ").strip()
        voice = input("Enter voice (alloy/echo/fable/onyx/nova/shimmer): ").strip()
        personality_type = input("Enter personality type: ").strip()
        description = input("Enter description: ").strip()
        
        print("\nEnter personality instructions (press Enter twice to finish):")
        instructions_lines = []
        while True:
            line = input()
            if line == "" and instructions_lines and instructions_lines[-1] == "":
                break
            instructions_lines.append(line)
        
        instructions = "\n".join(instructions_lines[:-1])  # Remove the last empty line
        
        greeting = input("Enter greeting instructions: ").strip()
        
        # Add to configurations
        config_key = personality_type.lower().replace(" ", "_")
        self.configs[config_key] = {
            "name": name,
            "voice": voice,
            "personality": personality_type,
            "description": description
        }
        
        self.personalities[personality_type] = {
            "instructions": instructions,
            "greeting": greeting
        }
        
        print(f"✅ Custom configuration '{config_key}' created!")
        return config_key

def main():
    switcher = VoiceSwitcher()
    
    print("🎭 Voice & Personality Switcher for LiveKit Financial Advisor")
    print("=" * 60)
    
    while True:
        print("\nOptions:")
        print("1. List available configurations")
        print("2. Apply a configuration")
        print("3. Create custom configuration")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == "1":
            switcher.list_configs()
        
        elif choice == "2":
            switcher.list_configs()
            config_name = input("\nEnter configuration name to apply: ").strip()
            switcher.apply_config(config_name)
        
        elif choice == "3":
            config_key = switcher.create_custom_config()
            apply_now = input(f"\nApply '{config_key}' now? (y/n): ").strip().lower()
            if apply_now == 'y':
                switcher.apply_config(config_key)
        
        elif choice == "4":
            print("👋 Goodbye!")
            break
        
        else:
            print("❌ Invalid choice! Please enter 1-4.")

if __name__ == "__main__":
    main() 