# Negotiation-Chatbot-Using-a-Pre-trained-AI-Model
Negotiation Chatbot is a web-based application designed to simulate price negotiation between a customer and a supplier. It takes user input in the form of a proposed price and a message and uses sentiment analysis to interpret the tone of the message. Based on the sentiment and negotiation model, the chatbot provides a response

# Negotiation Chatbot

This project is a **Negotiation Chatbot** that simulates the process of negotiating a price between a customer and a supplier. The chatbot uses sentiment analysis and negotiation response models to provide real-time feedback based on the user's input.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Overview

The Negotiation Chatbot allows users to:
- Enter a proposed price.
- Send a message to simulate negotiation with a supplier.
- Get a response from the bot based on the message and proposed price.

The project incorporates **sentiment analysis** to understand the tone of the message and provides negotiation feedback accordingly. This chatbot can be useful for platforms that deal with real-time pricing negotiations.

## Features

- Real-time negotiation feedback.
- Sentiment analysis based on the user’s message.
- Integration with pre-trained AI models (like ChatGPT or Gemini).
- Simple and intuitive UI.
  
## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/negotiation-chatbot.git


cd negotiation-chatbot
Create a virtual environment (optional but recommended):

bash
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
Install the required dependencies:

bash
pip install -r requirements.txt
Run the app:

bash
streamlit run app.py
Usage
Open your web browser and navigate to http://localhost:8501.
Enter your proposed price and message into the input fields.
Click Submit to see the bot's response based on sentiment analysis and negotiation logic.
Project Structure
negotiation-chatbot/
│
├── app.py               # Main application file for Streamlit
├── requirements.txt      # List of dependencies
├── README.md             # Project documentation
└── assets/               # Folder for images and other static assets
Contributing
Contributions are welcome! If you find any issues or have suggestions for improvement, feel free to submit a pull request.


