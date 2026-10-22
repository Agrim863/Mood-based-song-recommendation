#!/usr/bin/env python3

from flask import Flask, render_template, request, jsonify
from groq import Groq
import json
import os

app = Flask(__name__)


def extract_mood_and_songs(mood):
    """Same logic as your working CLI version"""

    api_key = "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"
    if not api_key:
        return {"error": "GROQ_API_KEY not set"}

    client = Groq(api_key=api_key)

    prompt = f"""You are a music recommendation expert. Based on the user's mood description, recommend exactly 5 songs.

User's mood: "{mood}"

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
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",   
            max_tokens=1024,
            messages=[{"role": "user", "content": prompt}]
        )

        response_text = response.choices[0].message.content

        
        if response_text.startswith("```"):
            response_text = response_text.split("```")[1]
            if response_text.startswith("json"):
                response_text = response_text[4:]

        data = json.loads(response_text)
        return data

    except json.JSONDecodeError as e:
        return {"error": f"JSON parse error: {str(e)}"}
    except Exception as e:
        return {"error": str(e)}


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/api/recommend', methods=['POST'])
def get_recommendations():
    data = request.get_json()
    mood = data.get('mood', '').strip()

    if len(mood) < 3:
        return jsonify({"error": "Please enter a valid mood"}), 400

    result = extract_mood_and_songs(mood)

    if "error" in result:
        return jsonify(result), 500

    return jsonify(result), 200


if __name__ == '__main__':
    print("🎵 Starting Web App...")
    print("👉 http://localhost:5000")
    app.run(debug=True, port=5000)