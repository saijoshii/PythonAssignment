import random
import json
import logging

# Load responses from a JSON file
def load_responses():
    return {
        "coffee": "The campus coffee bar is open from 7 AM to 8 PM.",
        "parking": "Parking is unavailable.",
        "library": "The library is open from 9 AM to 9 PM on weekdays.",
        "admissions": "Admissions can be contacted via email at admissions@poppleton.ac.uk.",
        "course": "You can find information about courses on our website under the 'Programs' section."
    }

# Random responses for unrecognized input
random_responses = [
    "Could you clarify your question?",
    "could you repeat that again?",
    "Hmm, i did not get that."
]

# Generate a random agent name
def generate_agent_name():
    names = ["Sai", "Dipsan", "Kohli", "starc", "ram bam yadav"]
    return random.choice(names)

# Initialize logging
logging.basicConfig(
    filename="chat_session.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

def chat():
    # Load responses
    responses = load_responses()

    # Prompt for user's name
    user_name = input("Welcome to Poppleton University's chat system! May I know your name please ? ")
    print(f"Hello, {user_name}! how are you? .")

    # Generate agent's name
    agent_name = generate_agent_name()
    print(f"You are now chatting with {agent_name}. How can I help you today?")

    while True:
        # Get user input
        user_input = input(f"{user_name}: ").strip().lower()
        
        # Log the user input
        logging.info(f"User: {user_input}")

        # Exit conditions
        if user_input in ["bye", "quit", "exit"]:
            print(f"{agent_name}: babye, {user_name}! Have a great day.")
            logging.info(f"{agent_name}: Goodbye, {user_name}!")
            break

        # Check for keywords
        response = None
        for keyword, reply in responses.items():
            if keyword in user_input:
                response = reply
                break

        # Random disconnection simulation
        if random.random() < 0.1:  
            print(f"{agent_name}: Oops, it seems we've been disconnected. Please refresh and try again.")
            logging.info(f"{agent_name}: Random disconnection occurred.")
            break

        # Respond
        if response:
            print(f"{agent_name}: {response}")
            logging.info(f"{agent_name}: {response}")
        else:
            random_reply = random.choice(random_responses)
            print(f"{agent_name}: {random_reply}")
            logging.info(f"{agent_name}: {random_reply}")

if __name__ == "__main__":
    chat()
