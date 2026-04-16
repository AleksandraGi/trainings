import random

def generate_quote():
    quote_list = ["To be or not to be",
                  "TGIF",
                  "No i klawo"]
    quote = random.choice(quote_list)

    return quote