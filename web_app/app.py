from flask import Flask, render_template, request, session, redirect, url_for
from my_ai_lib import AIHelper
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.secret_key = os.urandom(24)  # For session management

def get_ai_helper():
    """Get AIHelper instance with session API key if available"""
    api_key = session.get('api_key') or os.environ.get('GEMINI_API_KEY')
    return AIHelper(api_key=api_key)

@app.route('/config', methods=['GET', 'POST'])
def config():
    if request.method == 'POST':
        api_key = request.form.get('api_key')
        if api_key:
            session['api_key'] = api_key
            return redirect(url_for('index'))
    return render_template('config.html', current_key=session.get('api_key', ''))

@app.route('/', methods=['GET', 'POST'])
def index():
    ai_helper = get_ai_helper()
    response = None
    
    if 'chat_history' not in session:
        session['chat_history'] = []
    
    if request.method == 'POST':
        user_input = request.form.get('user_input')
        if user_input:
            raw_response = ai_helper.get_response(user_input)
            response = ai_helper.format_response(raw_response)
            
            # Store in session
            chat_history = session['chat_history']
            chat_history.append({'query': user_input, 'response': response})
            session['chat_history'] = chat_history
            session.modified = True
    
    has_api_key = bool(session.get('api_key') or os.environ.get('GEMINI_API_KEY'))
    return render_template('index.html', 
                         response=response, 
                         history=session.get('chat_history', []),
                         has_api_key=has_api_key)

if __name__ == '__main__':
    app.run(debug=True)
