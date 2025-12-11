# AI Web Assistant

A Flask-based web application powered by Google Gemini API that allows users to interact with AI through a beautiful, modern interface.

## Features

- 🤖 **Real AI Responses** - Powered by Google Gemini API
- 📚 **Custom Python Library** - `my_ai_lib` for AI operations
- 🎨 **Modern UI** - Beautiful gradient design with Bootstrap 5
- 💬 **Chat History** - Track your conversation
- 🔧 **Easy Configuration** - Web-based API key setup
- 🔒 **Secure** - Environment variable support with `.env` file

## Quick Start

### 1. Install Dependencies

```bash
# Install the custom library
pip install -e ai_library_pkg

# Install required packages
pip install -r ai_library_pkg/requirements.txt
pip install -r web_app/requirements.txt
```

### 2. Set Up API Key

Create a `.env` file in the project root:

```bash
GEMINI_API_KEY=your-api-key-here
```

Get your free API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

### 3. Run the Application

```bash
cd web_app
python app.py
```

Visit: **http://127.0.0.1:5000**

## Project Structure

```
ai_web_helper/
├── ai_library_pkg/     # Custom Python library
├── web_app/           # Flask application
├── .env              # API key (create this)
└── .env.example      # Template
```

## Usage

1. **Ask Questions**: Type any question in the textarea
2. **Get AI Responses**: Click "Get Answer" to receive AI-generated responses
3. **View History**: See all your previous conversations
4. **Configure API**: Click the gear icon to set up your API key

## Mock Mode

If no API key is provided, the app runs in **mock mode** with simulated responses for testing.

## Technologies Used

- **Backend**: Flask, Python
- **AI**: Google Gemini API
- **Frontend**: Bootstrap 5, HTML5, CSS3
- **Libraries**: python-dotenv, google-generativeai

## License

MIT License

## Author

Created as part of an educational project to demonstrate:
- Custom Python library creation
- Flask web development
- AI API integration
- Modern web design

---

**Enjoy your AI Web Assistant!** 🚀
