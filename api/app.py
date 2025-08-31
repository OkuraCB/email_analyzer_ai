from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import json
from openai import OpenAI

app = Flask(__name__)
CORS(app)  # pyright: ignore[reportUnusedCallResult]

OPENROUTER_API_KEY = os.environ.get('OPENROUTER_API_KEY')
OPENROUTER_API_URL = os.environ.get('OPENROUTER_API_URL', 'https://openrouter.ai/api/v1')
AI_MODEL = os.environ.get("AI_MODEL", "deepseek/deepseek-r1-0528:free")
PORT = os.environ.get("PORT")

def analyze_email_content(text: str):
    prompt = f"""
    Analyze the following email content and provide a JSON response with these exact fields:
    Please note that "meaningfulness", in this context, refers to what is considered meaningful in a corporate sense. Urgent actions, important meetings and emails from managers are normally meaningful, while system notifications, spam and messages such as "Happy new year!" are generally not. 
    - "score": integer between 0-100 representing how meaningful the email is
    - "meaningful_label": string classification ("Highly Meaningful", "Meaningful", "Moderately Meaningful", "Not Meaningful")
    - "topics": integer count of distinct topics discussed
    - "actions": integer count of action items or requests
    - "sentiment": string sentiment classification ("Positive", "Neutral", "Negative")
    - "length": string classification of email length ("Very Short", "Short", "Medium", "Long", "Very Long")
    - "accuracy": integer that represents the percentage of confidence you have in this response
    
    Email content: {text}
    
    Respond with ONLY the JSON object in raw text form, without markdown notation and no additional text.
    """

    try:
        client = OpenAI(base_url=OPENROUTER_API_URL,api_key=OPENROUTER_API_KEY)
        completion=client.chat.completions.create(model=AI_MODEL, messages=[
                {"role": "system", "content": "You are an AI assistant that analyzes emails for meaningfulness. Always respond with valid JSON only."},
                {"role": "user", "content": prompt}
            ])
        
        ai_response = completion.choices[0].message.content
        print(ai_response)
        
        analysis = json.loads(ai_response)
        
        required_fields = ["score", "meaningful_label", "topics", "actions", "sentiment", "length", "accuracy"]
        if all(field in analysis for field in required_fields):
            return analysis
        else:
            raise ValueError("DeepSeek response missing required fields")
            
    except Exception as e:
        print(f"DeepSeek API error: {e}")
        raise ValueError("Something gone wrong")

@app.route('/api/analyze', methods=['POST'])
def analyze_email():
    try:
        data = request.get_json()
        
        if not data or 'text' not in data:
            return jsonify({"error": "No text provided"}), 400
        
        text = data['text']
        
        if not text.strip():
            return jsonify({"error": "Empty text provided"}), 400

        if OPENROUTER_API_KEY:
            analysis = analyze_email_content(text)
        else:
            raise ValueError("Invalid API KEY")
        
        return jsonify(analysis)
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500