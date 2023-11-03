import random

# Define a list of quotes
quotes = [
    "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
    "Keep your face always toward the sunshine—and shadows will fall behind you. - Walt Whitman",
    "Believe you can, and you're halfway there. - Theodore Roosevelt",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "The best way to predict the future is to create it. - Peter Drucker",
    "You are never too old to set another goal or to dream a new dream. - C.S. Lewis",
    "The only way to do great work is to love what you do. - Steve Jobs",
    "In the middle of every difficulty lies opportunity. - Albert Einstein",
    "Your time is limited, don't waste it living someone else's life. - Steve Jobs",
    "The future depends on what you do today. - Mahatma Gandhi",
    "You must be the change you wish to see in the world. - Mahatma Gandhi",
    "I can't change the direction of the wind, but I can adjust my sails to always reach my destination. - Jimmy Dean",
    "You miss 100% of the shots you don't take. - Wayne Gretzky",
    "The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela",
    "The secret of getting ahead is getting started. - Mark Twain",
    "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
    "The only person you are destined to become is the person you decide to be. - Ralph Waldo Emerson",
    "The harder I work, the luckier I get. - Samuel Goldwyn",
    "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle. - Christian D. Larson",
    "Success is not the key to happiness. Happiness is the key to success. If you love what you are doing, you will be successful. - Albert Schweitzer",
    "Don't be pushed around by the fears in your mind. Be led by the dreams in your heart. - Roy T. Bennett",
    "Challenges are what make life interesting and overcoming them is what makes life meaningful. - Joshua J. Marine",
    "Life is 10% what happens to us and 90% how we react to it. - Charles R. Swindoll",
    "Believe in yourself, take on your challenges, dig deep within yourself to conquer fears. Never let anyone bring you down. You got this. - Chantal Sutherland",
    "Life is short, and it's up to you to make it sweet. - Sarah Louise Delany",
    "The greatest wealth is to live content with little. - Plato",
    "To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment. - Ralph Waldo Emerson",
    "Every day may not be good, but there's something good in every day. - Alice Morse Earle",
    "Happiness is not something readymade. It comes from your own actions. - Dalai Lama",
    "You can't go back and change the beginning, but you can start where you are and change the ending. - C.S. Lewis",
    "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
    "Every morning brings new potential, but if you dwell on the misfortunes of the day before, you tend to overlook tremendous opportunities. - Harvey Mackay",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "Success is walking from failure to failure with no loss of enthusiasm. - Winston Churchill",
    "The only thing standing between you and your goal is the story you keep telling yourself as to why you can't achieve it. - Jordan Belfort",
    "Happiness is not in the mere possession of money; it lies in the joy of achievement, in the thrill of creative effort. - Franklin D. Roosevelt",
    "Do not wait for leaders; do it alone, person to person. - Mother Teresa",
    "The best preparation for tomorrow is doing your best today. - H. Jackson Brown Jr.",
    "Your work is going to fill a large part of your life, and the only way to be truly satisfied is to do what you believe is great work. And the only way to do great work is to love what you do. - Steve Jobs",
    "You have power over your mind – not outside events. Realize this, and you will find strength. - Marcus Aurelius",
    "Life is really simple, but we insist on making it complicated. - Confucius",
    "Your time is limited, so don't waste it living someone else's life. - Steve Jobs",
    "It does not matter how slowly you go as long as you do not stop. - Confucius",
    "Happiness is a butterfly, which when pursued, is always just beyond your grasp, but which, if you will sit down quietly, may alight upon you. - Nathaniel Hawthorne",
    "Change your thoughts and you change your world. - Norman Vincent Peale",
    "For everything you have lost, you have gained something else. - Unknown",
    "The biggest risk is not taking any risk. In a world that's changing quickly, the only strategy that is guaranteed to fail is not taking risks. - Mark Zuckerberg",
    "Life is either a daring adventure or nothing at all. - Helen Keller",
    "The only time to look back is when you want to see how far you've come. - Unknown",
    "You are the master of your destiny. You can influence, direct, and control your own environment. You can make your life what you want it to be. - Napoleon Hill",
    "Success is not in what you have, but who you are. - Bo Bennett",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "Don't be afraid to give up the good to go for the great. - John D. Rockefeller",
    "Your work is going to fill a large part of your life, and the only way to be truly satisfied is to do what you believe is great work. - Steve Jobs",
    "Dream big and dare to fail. - Norman Vaughan",
    "Your life does not get better by chance; it gets better by change. - Jim Rohn",
    "The only way to achieve the impossible is to believe it is possible. - Charles Kingsleigh",
    "The road to success and the road to failure are almost exactly the same. - Colin R. Davis",
    "Challenges are what make life interesting, and overcoming them is what makes life meaningful. - Joshua J. Marine",
    "The biggest risk is not taking any risk. In a world that is changing quickly, the only strategy that is guaranteed to fail is not taking risks. - Mark Zuckerberg"
]

prev_index = None

while True:
    # Generate a random index that is different from the previous one
    random_index = random.randint(0, len(quotes) - 1)
    while random_index == prev_index:
        random_index = random.randint(0, len(quotes) - 1)

    # Update the previously displayed quote's index
    prev_index = random_index

    # Select and print a random quote
    random_quote = quotes[random_index]
    print(random_quote)

    # Wait for user input, and if they press Enter, generate another random quote
    input("")
