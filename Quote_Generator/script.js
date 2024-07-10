const quotes = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Life is what happens when you're busy making other plans. - John Lennon",
    "The purpose of our lives is to be happy. - Dalai Lama",
    "Get busy living or get busy dying. - Stephen King",
    "You have within you right now, everything you need to deal with whatever the world can throw at you. - Brian Tracy",
    "In the end, it's not the years in your life that count. It's the life in your years. - Abraham Lincoln",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "It does not matter how slowly you go as long as you do not stop. - Confucius",
    "The best way to predict the future is to create it. - Abraham Lincoln",
    "Your time is limited, so don't waste it living someone else's life. - Steve Jobs",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "Happiness is not something ready made. It comes from your own actions. - Dalai Lama",
    "Strive not to be a success, but rather to be of value. - Albert Einstein",
    "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
    "The journey of a thousand miles begins with one step. - Lao Tzu",
    "The mind is everything. What you think you become. - Buddha",
    "You must be the change you wish to see in the world. - Mahatma Gandhi",
    "Every moment is a fresh beginning. - T.S. Eliot",
    "To live is the rarest thing in the world. Most people exist, that is all. - Oscar Wilde",
    "It is never too late to be what you might have been. - George Eliot"
];

function generateQuote() {
    const randomIndex = Math.floor(Math.random() * quotes.length);
    const quote = quotes[randomIndex];
    document.getElementById('quote').innerText = quote;
}

function shareToWhatsApp() {
    const quote = document.getElementById('quote').innerText;
    const whatsappUrl = `https://wa.me/?text=${encodeURIComponent(quote)}`;
    window.open(whatsappUrl, '_blank');
}

function shareToFacebook() {
    const quote = document.getElementById('quote').innerText;
    const facebookUrl = `https://www.facebook.com/sharer/sharer.php?u=${encodeURIComponent(quote)}`;
    window.open(facebookUrl, '_blank');
}

function shareToTwitter() {
    const quote = document.getElementById('quote').innerText;
    const twitterUrl = `https://twitter.com/intent/tweet?text=${encodeURIComponent(quote)}`;
    window.open(twitterUrl, '_blank');
}

function shareToInstagram() {
    const quote = document.getElementById('quote').innerText;
    const instagramUrl = `https://www.instagram.com/?text=${encodeURIComponent(quote)}`;
    window.open(instagramUrl, '_blank');
}
