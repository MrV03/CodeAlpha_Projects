from flask import Flask, request, jsonify, render_template
import spacy

app = Flask(__name__)
nlp = spacy.load('en_core_web_sm')

# Sample FAQs
faqs = {
    "hi": "Hi! How can I help you today?",
    "hello": "Hello There! How can I help you today?",
    "hey": "Hey there! How can I help you today?",
    "how are you ?": "I'm good, thank you. I'm doing well. How about you?",
    "what can you do ?": "I can answer questions, provide information, or just chat with you.",
    "who created you ?": "I was created by a developer using Python and NLTK.",
    "how does this chatbot work ?": "I use natural language processing (NLP) techniques to understand and respond to your messages.",
    "how do I reset my password ?": "To reset your password, please visit our website and follow the 'Forgot Password' link.",
    "how do I contact customer support ?": "You can contact our customer support team by phone at +27 815 382 785 or via email at vivekmaharaj41@gmail.com.",
    "what are your hours of operation ?": "We are available 24/7 to assist you.",
    "what payment methods do you accept ?": "We accept Visa, Mastercard, American Express, and PayPal.",
    "how can I track my order ?": "You can track your order status by entering your tracking number on our website.",
    "how do I return an item ?": "To return an item, please log in to your account and initiate a return request.",
    "what is your privacy policy ?": "You can view our privacy policy on our website. We take your privacy seriously.",
    "can I change my delivery address after placing an order ?": "Please contact our customer support team as soon as possible to request a delivery address change.",
    "can I cancel my order ?": "You can cancel your order within 24 hours of placing it. After that, please contact customer support for assistance.",
    "where can I find your store locations ?": "You can find our store locations on our website's store locator page.",
    "what is your return policy ?": "Our return policy allows returns within 30 days of purchase. Please ensure the item is in its original condition.",
    "what are your shipping options ?": "We offer standard and expedited shipping options. Delivery times may vary based on your location.",
    "do you offer discounts or promotions ?": "Yes, we regularly offer discounts and promotions. Please check our website or subscribe to our newsletter for updates.",
    "do you have a mobile app ?": "Yes, you can download our mobile app from the App Store or Google Play.",
    "can I change my account password ?": "Yes, you can change your account password in the settings section of your account.",
    "how can I update my billing information ?": "You can update your billing information by logging in to your account and navigating to the billing section.",
    "where can I find product manuals or guides ?": "Product manuals and guides are available for download on our website under the support section.",
    "(.*) (location|city) ?": "I'm a virtual assistant. My location is in the cloud!",
    "(.*) thank you (.*)": "You're welcome! No problem!",
    "bye|goodbye": "Goodbye! Have a great day. See you later!",
    "quit": "Bye! Take care. Goodbye. Have a great day!"
}



@app.route('/')
def home():
    return render_template('index.html')


@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_input = request.json['message']
    doc = nlp(user_input.lower())

    # Normalize and tokenize user input
    user_input_tokens = set([token.lemma_ for token in doc])

    response = "Sorry, I didn't understand that."
    max_similarity = 0.0

    for question, answer in faqs.items():
        faq_tokens = set([token.lemma_ for token in nlp(question.lower())])
        similarity = len(user_input_tokens & faq_tokens) / len(faq_tokens)
        if similarity > max_similarity:
            max_similarity = similarity
            response = answer

    return jsonify({'response': response})


if __name__ == '__main__':
    app.run(debug=True)
