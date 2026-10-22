# 🎵 Mood-Based Song Recommendation MVP

A minimal viable product that takes your mood description and recommends 5 songs with direct Spotify links using Claude AI.

## Features

✅ **Mood Input** - Describe how you're feeling in natural language  
✅ **Claude AI Analysis** - Intelligent mood understanding  
✅ **Song Recommendations** - 5 personalized songs with reasons  
✅ **Clickable Links** - Direct Spotify links for each song  
✅ **Two Interfaces** - CLI or Web-based (your choice!)

## Prerequisites

```bash
# Install required packages
pip install anthropic flask
```

## Setup - Get Your Claude API Key

1. Go to https://console.anthropic.com/
2. Sign up or log in
3. Create a new API key
4. Copy the key

## Setting the API Key

### On Mac/Linux:
```bash
export ANTHROPIC_API_KEY="your-api-key-here"
```

### On Windows (Command Prompt):
```bash
set ANTHROPIC_API_KEY=your-api-key-here
```

### On Windows (PowerShell):
```powershell
$env:ANTHROPIC_API_KEY="your-api-key-here"
```

## Option 1: CLI Version (Command Line)

**Best for:** Quick testing, learning Python, terminal lovers

```bash
# Navigate to the project folder
cd /path/to/your/project

# Run the CLI
python mood_recommendation_mvp.py
```

**Example Usage:**
```
🎵 Welcome to Mood-Based Song Recommendation System
============================================================

Describe your current mood in a few words or sentences.
Examples: 'sad and nostalgic', 'happy and energetic', 'calm and peaceful'
────────────────────────────────────────────────────────────

Your mood: sad and nostalgic, want some emotional indie music

⚙️  Analyzing mood with Claude AI...
────────────────────────────────────────────────────────────

✨ Mood Analysis:
  Emotions: sad, nostalgic, introspective
  Energy: low
  Vibe: melancholic and reflective

============================================================
🎶 Top 5 Recommendations:
============================================================

1. "Iris" by Goo Goo Dolls
   Reason: Perfectly captures nostalgic indie vibe with melancholic vocals
   🔗 Listen on Spotify: https://open.spotify.com/search/Iris%20Goo%20Goo%20Dolls

2. "Such Great Heights" by The Postal Service
   Reason: Slow tempo, emotional build-up matches introspective mood
   🔗 Listen on Spotify: https://open.spotify.com/search/Such%20Great%20Heights%20The%20Postal%20Service

... and 3 more recommendations
```

## Option 2: Web Version (Beautiful UI)

**Best for:** Nice interface, sharing with friends, screenshots

```bash
# Navigate to the project folder
cd /path/to/your/project

# Start the Flask server
python mood_recommendation_web.py
```

Then open your browser and go to:
```
http://localhost:5000
```

**Features:**
- Beautiful purple gradient UI
- Real-time mood analysis display
- Clickable Spotify links
- Mobile-friendly responsive design
- Error handling and validation

## File Structure

```
project/
├── mood_recommendation_mvp.py      # CLI version
├── mood_recommendation_web.py      # Web backend
└── templates/
    └── index.html                  # Web frontend
```

## How It Works (Under the Hood)

### UNIT 1: Python Fundamentals
- `get_user_mood()` - Functions and input validation
- Loops for retrying invalid input
- Control flow (if/else) for error handling

### UNIT 2: Data Structures
- JSON parsing of Claude's response
- Lists for song recommendations
- Dictionaries for mood analysis data

### UNIT 3: APIs
- Claude API integration using `anthropic` library
- HTTP requests to Claude (handled by SDK)
- JSON request/response handling

### Code Flow:
1. **Input** → User describes mood
2. **Processing** → Send to Claude API with prompt
3. **Parsing** → Extract JSON response
4. **Display** → Show songs with Spotify links

## Customization Ideas

### Extend with More Features:
1. Save recommendation history to a JSON file (UNIT 2)
2. Add a simple SQLite database (UNIT 4)
3. Create user profiles and preferences (UNIT 4)
4. Add data visualization with matplotlib (UNIT 4)

### Try Different Song Sources:
```python
# Current: Spotify search
# Could also add:
# - Apple Music links
# - YouTube Music links
# - YouTube links
# - Genius lyrics links
```

### Improve Recommendations:
```python
# Current: 5 songs
# Could extend to:
# - 10-15 songs
# - Full playlist creation
# - Playlist shuffling
# - Shuffle by energy level
```

## Troubleshooting

### "No module named 'anthropic'"
```bash
pip install anthropic
```

### "No module named 'flask'"
```bash
pip install flask
```

### "API key not found"
Make sure you set the environment variable and the terminal/IDE has access to it. Try restarting your terminal after setting the API key.

### "Connection error"
- Check your internet connection
- Check if Claude API is accessible (it might be down)
- Try again in a few moments

## Next Steps

Once you're comfortable with this MVP, you can:

1. **UNIT 4** - Add database storage:
   - Store recommendation history
   - Track user preferences
   - Build user profiles

2. **Advanced Features**:
   - Mood trend analysis
   - Collaborative filtering
   - Playlist generation
   - Mobile app

3. **Production Ready**:
   - Deploy to Heroku/Railway
   - Add authentication
   - Scale to handle multiple users
   - Add caching for faster responses

## Learning Resources

- Claude API Docs: https://docs.claude.com/
- Flask Docs: https://flask.palletsprojects.com/
- Python Docs: https://docs.python.org/3/

## Questions?

- Re-read the code comments (marked with UNIT 1-3)
- Try modifying the prompt to Claude
- Break things intentionally to learn how they work!

Happy coding! 🎵✨
