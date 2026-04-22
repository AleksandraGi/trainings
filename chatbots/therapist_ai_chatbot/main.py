# source: https://programiz.pro/ide/python/RSBJCZ9RQT

from openai import OpenAI

llm = OpenAI()

# OPENAI_API_KEY

# Print statement at the start of the program

print("\nWarning: This is not a real therapist. This is an AI example\n")
print("\nWelcome to AI THERAPIST\n")
print("\nType 'quit' to exit\n")

# A dictionary to store the youtube links, this will be used to access the data, when users type /help <topic>.

resources = {
    "anxiety": "https://www.youtube.com/watch?v=WWloIAQpMcQ",
    "sleep": "https://www.youtube.com/shorts/zK5BfFvmTao", 
    "stress": "https://www.youtube.com/watch?v=8jPQjjsBbic", 
    "motivation": "https://www.youtube.com/watch?v=QkCa--fyGJA"
    }

# Create a variable "quit_message" to store the message of program have ended after user decided to end.
quit_message = "\n--- Session Ended ---\nThank you for using AI Therapist \n" + "-" * 60

#The main logic and loop of the AI chatbot

# The while true loop allow the program to keep running until the user decided to quit or end it.

while True:
    # Allow user to choose the type of responses
    Prompt = input("\nChoose type of response: [1] relaxed [2] neutral | Type 'quit' to exit' \n")
      
    # Check that if the Prompt variable that is given by the user if it is quit.
    # Then initialize and print quit_message and break.
    # Notice that lower() is used so no matter if user types in capital or small letter, it will recognize it.

    if Prompt.strip().lower() == "quit":
        print(quit_message)
        break

    # This will check if prompt is 1 or 2 and keeps asking until the input is valid.

    if Prompt != "1" and Prompt != "2":
        print("Please enter 1 or 2 only.") 
        continue

    user = input("Ask Anything (or type /help topic): ")

    if user.strip().lower() == "quit":
        print(quit_message)
        break

    # This check if user word start with /help, then it will check if the topic exist in the dictionary.
    # If exist, print and show the link, otherwise suggest avaiable topics.

    if user.strip().lower().startswith("/help"):
        topic = user.replace("/help", "").strip().lower()
        if topic in resources:
            print(f"\nHere is a helpful resource regarding {topic}: {resources[topic]}\n")
        else:
            print("\nTry something like: /help anxiety, /help sleep, /help stress, or / help motivation.\n")
            continue

    # Allow user to choose 1 or 2, after each message by the AI.
    if Prompt == "1":
        print("\nYou selected: Relaxed mode\n")
    elif Prompt == "2":
        print("\nYou selected: Neutral mode\n")

    # Create a line to make the program look nicer.
    print("-" * 60)
       
    # Check if prompt is 1, then uses the responses of Relaxed Mode
    if Prompt == "1":
        response = llm.chat.completions.create(
            model="gpt-40",
            messages=[
                {"role": "system", "content": "You are a therapist who comforts and offers responses and advice to the user."},
                {"role": "user", "content": user}])
        
    # Otherwise check if prompt is 2, then uses the responses of Neutral Mode
    elif Prompt == "2":
        response = llm.chat.completions.create(
            model="gpt-40",
            messages=[
                {"role": "system", "content": "You are a therapist who offers logical and neutral stances with no emotional bias to the user."}, 
                {"role": "user", "content": user}])
    
    reply = response.choices[0].message.content
    print("\n--- Therapist Response ---\n") 
    print(reply)
    print("-" * 60 + "\n")