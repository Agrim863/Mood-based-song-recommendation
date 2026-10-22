

from groq import Groq
import json
import os

def get_user_mood():
    """Get mood description from user"""
    print("\n" + "="*60)
    print("🎵 Welcome to Mood-Based Song Recommendation System")
    print("="*60)
    print("\nDescribe your current mood in a few words or sentences.")
    print("Examples: 'sad and nostalgic', 'happy and energetic', 'calm and peaceful'")
    print("-"*60)
    
    mood = input("\nYour mood: ").strip()
    
    if len(mood) < 3:
        print("❌ Please describe your mood with at least a few words.")
        return get_user_mood()
    
    return mood


def extract_mood_and_songs(mood_description):
    """Send mood to Groq and get song recommendations"""
    print("\n⚙️  Analyzing mood with Groq AI (lightning fast)...")
    print("-"*60)
    
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        print("\n❌ Error: GROQ_API_KEY environment variable not set!")
        print("\n📚 Setup Instructions:")
        print("1. Visit: https://console.groq.com/")
        return None
    
    # Initialize Groq client
    client = Groq(api_key=api_key)
    
    prompt = f"""You are a music recommendation expert. Based on the user's mood description, recommend exactly 5 songs.

User's mood: "{mood_description}"

Respond ONLY with valid JSON (no other text) in this exact format:
{{
    "mood_analysis": {{
        "primary_emotions": ["emotion1", "emotion2"],
        "energy_level": "low/medium/high",
        "vibe": "brief description"
    }},
    "recommendations": [
        {{
            "rank": 1,
            "title": "Song Title",
            "artist": "Artist Name",
            "reason": "Why this song matches the mood",
            "spotify_query": "Song Title Artist Name"
        }},
        {{
            "rank": 2,
            "title": "Song Title",
            "artist": "Artist Name",
            "reason": "Why this song matches the mood",
            "spotify_query": "Song Title Artist Name"
        }},
        {{
            "rank": 3,
            "title": "Song Title",
            "artist": "Artist Name",
            "reason": "Why this song matches the mood",
            "spotify_query": "Song Title Artist Name"
        }},
        {{
            "rank": 4,
            "title": "Song Title",
            "artist": "Artist Name",
            "reason": "Why this song matches the mood",
            "spotify_query": "Song Title Artist Name"
        }},
        {{
            "rank": 5,
            "title": "Song Title",
            "artist": "Artist Name",
            "reason": "Why this song matches the mood",
            "spotify_query": "Song Title Artist Name"
        }}
    ]
}}"""
    
    try:
        # Call Groq API (using correct chat.completions endpoint)
        message = client.chat.completions.create(
            model="llama-3.1-8b-instant",  # Fast, powerful, free
            max_tokens=1024,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        
        # Extract response
        response_text = message.choices[0].message.content
        
        # Clean up if needed
        if response_text.startswith("```"):
            response_text = response_text.split("```")[1]
            if response_text.startswith("json"):
                response_text = response_text[4:]
        
        data = json.loads(response_text)
        return data
        
    except json.JSONDecodeError as e:
        print(f"❌ Error parsing response: {str(e)}")
        return None
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return None


def display_recommendations(data):
    """Display songs with clickable Spotify links"""
    if not data:
        return
    
    # Extract mood analysis
    mood_analysis = data.get("mood_analysis", {})
    print("\n✨ Mood Analysis:")
    print(f"  Emotions: {', '.join(mood_analysis.get('primary_emotions', []))}")
    print(f"  Energy: {mood_analysis.get('energy_level', 'unknown')}")
    print(f"  Vibe: {mood_analysis.get('vibe', '')}")
    
    # Extract and display recommendations
    recommendations = data.get("recommendations", [])
    
    print("\n" + "="*60)
    print("🎶 Top 5 Recommendations:")
    print("="*60)
    
    for rec in recommendations:
        rank = rec.get("rank", 0)
        title = rec.get("title", "Unknown")
        artist = rec.get("artist", "Unknown")
        reason = rec.get("reason", "")
        spotify_query = rec.get("spotify_query", "")
        
        # Create Spotify search link
        spotify_link = f"https://open.spotify.com/search/{spotify_query.replace(' ', '%20')}"
        
        print(f"\n{rank}. \"{title}\" by {artist}")
        print(f"   Reason: {reason}")
        print(f"   🔗 Listen on Spotify: {spotify_link}")
    
    print("\n" + "="*60)
    print("✓ Open any link above in your browser to listen!")
    print("="*60 + "\n")


def main():
    """Main application flow"""
    # Get user mood input
    mood = get_user_mood()
    
    # Analyze with Groq and get recommendations
    recommendations = extract_mood_and_songs(mood)
    
    # Display results with links
    if recommendations:
        display_recommendations(recommendations)
    else:
        print("\n❌ Failed to get recommendations. Please try again.")


if __name__ == "__main__":
    main()
