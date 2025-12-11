# My AI Library

A Python library for interfacing with Google Gemini API to build AI-powered applications.

## Features

- **get_response(prompt)**: Get AI responses from Google Gemini
- **summarize_text(text)**: Summarize long text using AI
- **format_response(text)**: Clean and format AI output

## Installation

### Local Installation (Development)

```bash
pip install -e .
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Setup

### Get a Gemini API Key

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Click "Create API Key"
3. Copy your API key

### Set the API Key

**Option 1: Environment Variable (Recommended)**

```bash
# Windows (PowerShell)
$env:GEMINI_API_KEY="your-api-key-here"

# Windows (Command Prompt)
set GEMINI_API_KEY=your-api-key-here

# Linux/Mac
export GEMINI_API_KEY="your-api-key-here"
```

**Option 2: Pass to Constructor**

```python
from my_ai_lib import AIHelper

helper = AIHelper(api_key="your-api-key-here")
```

## Usage

```python
from my_ai_lib import AIHelper

# Initialize (uses GEMINI_API_KEY environment variable)
ai = AIHelper()

# Or pass API key directly
ai = AIHelper(api_key="your-key-here")

# Get a response
response = ai.get_response("What is Python?")
print(response)

# Summarize text
summary = ai.summarize_text("Long text here...")
print(summary)

# Format response
formatted = ai.format_response("  some text  ")
print(formatted)
```

## Mock Mode

If no API key is provided, the library runs in **mock mode** with simulated responses. This is useful for testing without API costs.

## License

MIT
