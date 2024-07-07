import nltk
from nltk.chat.util import Chat, reflections
from tkinter import *

# Define pairs of patterns and responses for FAQs on any topic
faq_pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hey there!", "Hi! How can I help you today?"]
    ],
    [
        r"how are you ?",
        ["I'm good, thank you.", "I'm doing well. How about you?"]
    ],
    [
        r"what can you do ?",
        ["I can answer questions, provide information, or just chat with you."]
    ],
    [
        r"who created you ?",
        ["I was created by a developer using Python and NLTK."]
    ],
    [
        r"how does this chatbot work ?",
        ["I use natural language processing (NLP) techniques to understand and respond to your messages."]
    ],
    [
        r"how do I reset my password ?",
        ["To reset your password, please visit our website and follow the 'Forgot Password' link."]
    ],
    [
        r"how do I contact customer support ?",
        ["You can contact our customer support team by phone at [Phone Number] or via email at [Email Address]."]
    ],
    [
        r"what are your hours of operation ?",
        ["We are available 24/7 to assist you."]
    ],
    [
        r"what payment methods do you accept ?",
        ["We accept Visa, Mastercard, American Express, and PayPal."]
    ],
    [
        r"how can I track my order ?",
        ["You can track your order status by entering your tracking number on our website."]
    ],
    [
        r"how do I return an item ?",
        ["To return an item, please log in to your account and initiate a return request."]
    ],
    [
        r"what is your privacy policy ?",
        ["You can view our privacy policy on our website. We take your privacy seriously."]
    ],
    [
        r"can I change my delivery address after placing an order ?",
        ["Please contact our customer support team as soon as possible to request a delivery address change."]
    ],
    [
        r"can I cancel my order ?",
        ["You can cancel your order within 24 hours of placing it. After that, please contact customer support for assistance."]
    ],
    [
        r"where can I find your store locations ?",
        ["You can find our store locations on our website's store locator page."]
    ],
    [
        r"what is your return policy ?",
        ["Our return policy allows returns within 30 days of purchase. Please ensure the item is in its original condition."]
    ],
    [
        r"what are your shipping options ?",
        ["We offer standard and expedited shipping options. Delivery times may vary based on your location."]
    ],
    [
        r"do you offer discounts or promotions ?",
        ["Yes, we regularly offer discounts and promotions. Please check our website or subscribe to our newsletter for updates."]
    ],
    [
        r"do you have a mobile app ?",
        ["Yes, you can download our mobile app from the App Store or Google Play."]
    ],
    [
        r"can I change my account password ?",
        ["Yes, you can change your account password in the settings section of your account."]
    ],
    [
        r"how can I update my billing information ?",
        ["You can update your billing information by logging in to your account and navigating to the billing section."]
    ],
    [
        r"where can I find product manuals or guides ?",
        ["Product manuals and guides are available for download on our website under the support section."]
    ],
    [
        r"(.*) (location|city) ?",
        ["I'm a virtual assistant. My location is in the cloud!"]
    ],
    [
        r"(.*) thank you (.*)",
        ["You're welcome!", "No problem!"]
    ],
    [
        r"bye|goodbye",
        ["Goodbye! Have a great day.", "See you later!"]
    ],
    [
        r"quit",
        ["Bye! Take care.", "Goodbye. Have a great day!"]
    ],
]

class ChatbotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Modern FAQ Chatbot")

        # Styling variables
        self.bg_color = "#f0f0f0"
        self.text_color = "#333333"
        self.btn_color = "#4CAF50"

        self.setup_gui()

        # Initialize chatbot
        self.chatbot = Chat(faq_pairs, reflections)

    def setup_gui(self):
        self.root.configure(bg=self.bg_color)

        self.messages_frame = Frame(self.root, bg=self.bg_color)
        self.messages_frame.pack(pady=10)

        self.messages = Text(self.messages_frame, wrap=WORD, bg=self.bg_color, fg=self.text_color)
        self.messages.pack()

        self.entry_field = Entry(self.root, bd=2, relief=RIDGE, fg=self.text_color, font=("Arial", 12))
        self.entry_field.pack(fill=X, padx=10, pady=10)
        self.entry_field.bind("<Return>", self.send_message)

        self.send_button = Button(self.root, text="Send", bg=self.btn_color, fg="white", font=("Arial", 12),
                                  command=self.send_message)
        self.send_button.pack(pady=5)

    def send_message(self, event=None):
        user_input = self.entry_field.get()
        self.entry_field.delete(0, END)

        if user_input.strip():  # Check if input is not empty
            response = self.chatbot.respond(user_input)
            if not response:  # If no response found
                response = "I'm sorry, I didn't quite understand that."
        else:
            response = "Please enter something."

        self.messages.insert(END, "You: " + user_input + "\nBot: " + response + "\n\n")

def main():
    root = Tk()
    app = ChatbotGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
