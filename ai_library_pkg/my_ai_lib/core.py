import random
import os

class AIHelper:
    """
    A helper library to interface with Google Gemini API.
    Falls back to mock mode if no API key is provided.
    """
    
    def __init__(self, api_key=None):
        self.api_key = api_key or os.environ.get('GEMINI_API_KEY')
        self.mock_responses = [
            "That's a very interesting question! As an AI, I think...",
            "Based on my analysis, the answer is 42.",
            "I'm not entirely sure, but here is what I found...",
            "Could you elaborate on that?",
            "The sky is blue because of Rayleigh scattering."
        ]
        
        # Try to import google.generativeai if API key is available
        self.genai = None
        self.model = None
        if self.api_key:
            try:
                import google.generativeai as genai
                self.genai = genai
                genai.configure(api_key=self.api_key)
                self.model = genai.GenerativeModel('gemini-flash-latest')
            except ImportError:
                print("Warning: google-generativeai not installed. Install with: pip install google-generativeai")
            except Exception as e:
                print(f"Warning: Could not initialize Gemini API: {e}")

    def get_response(self, prompt):
        """
        Gets a response from Gemini AI or returns a mock response.
        
        Args:
            prompt (str): The user's question or prompt
            
        Returns:
            str: AI-generated response
        """
        if self.model:
            try:
                response = self.model.generate_content(prompt)
                return response.text
            except Exception as e:
                return f"Error calling Gemini API: {str(e)}. Using mock mode."
        
        # Mock logic (fallback)
        return f"{random.choice(self.mock_responses)} (Mock mode - set GEMINI_API_KEY to use real AI)"

    def summarize_text(self, text):
        """
        Summarizes the given text using Gemini AI or a simple algorithm.
        
        Args:
            text (str): Text to summarize
            
        Returns:
            str: Summarized text
        """
        if self.model:
            try:
                prompt = f"Please provide a concise summary of the following text:\n\n{text}"
                response = self.model.generate_content(prompt)
                return response.text
            except Exception as e:
                # Fallback to simple summarization
                pass
        
        # Simple summarization (fallback)
        sentences = text.split('.')
        if len(sentences) > 2:
            return f"Summary: {sentences[0]}. {sentences[1]}."
        return f"Summary: {text}"

    def format_response(self, text):
        """
        Cleans and formats the text (e.g., stripping whitespace, capitalizing).
        
        Args:
            text (str): Text to format
            
        Returns:
            str: Formatted text
        """
        if not text:
            return ""
        return text.strip()

