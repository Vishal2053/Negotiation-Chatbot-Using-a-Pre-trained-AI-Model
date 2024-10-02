from flask import Flask, request, render_template, jsonify
from flask import Flask, request, jsonify
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import os

# Load Hugging Face models (DialoGPT for negotiation, DistilBERT for sentiment analysis)
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")
sentiment_analyzer = pipeline('sentiment-analysis')


app = Flask(__name__)

# Pricing logic
base_price = 100
min_price = 80
max_price = 120

def negotiate_price(user_price):
    if min_price <= user_price <= max_price:
        return f"We can accept your price of {user_price}."
    elif user_price < min_price:
        return f"We can't go below {min_price}. How about {min_price}?"
    elif user_price > max_price:
        return f"{user_price} is too high. Can you offer closer to {base_price}?"

def get_bot_response(user_message):
    input_ids = tokenizer.encode(user_message + tokenizer.eos_token, return_tensors='pt')
    chat_history_ids = model.generate(input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)
    return tokenizer.decode(chat_history_ids[:, input_ids.shape[-1]:][0], skip_special_tokens=True)

def analyze_sentiment(user_message):
    sentiment = sentiment_analyzer(user_message)[0]
    return sentiment['label']

# Define the routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/negotiate', methods=['POST'])
def negotiate():
    user_price = float(request.form['price'])
    user_message = request.form['message']
    
    # Analyze sentiment
    sentiment = analyze_sentiment(user_message)
    
    # Negotiate price
    negotiation_response = negotiate_price(user_price)
    
    # Get bot response
    bot_response = get_bot_response(f"Customer proposed {user_price}. Respond accordingly.")
    
    # Return the responses as JSON
    return jsonify({
        'sentiment': sentiment,
        'negotiation_response': negotiation_response,
        'bot_response': bot_response
    })

if __name__ == '__main__':
    app.run(debug=True)