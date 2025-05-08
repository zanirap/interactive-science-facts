import requests
import json
import random

def get_random_science_fact_from_api():
    """Fetches a random science fact from the Numbers API."""
    try:
        response = requests.get("http://numbersapi.com/random/trivia?json")
        response.raise_for_status()  # Raise an exception for bad status codes
        data = response.json()
        return data.get("text")
    except requests.exceptions.RequestException as e:
        print(f"Agent: Oops! There was an issue connecting to the server.")
        print(f"Agent: Error details: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Agent: Hmm, I couldn't understand the server's response.")
        print(f"Agent: Error details: {e}")
        return None

def main():
    """Fetches and displays a science fact, then asks the user if they want another one."""
    greetings = [
        "Agent: Hello! Here's a fun science fact for you:",
        "Agent: Time to learn something cool! Here's a fact:",
        "Agent: Look what I found:",
        "Agent: Did you know that:",
        "Agent: Today I'm going to tell you that:"
    ]

    while True:
        fact = get_random_science_fact_from_api()
        if fact:
            greeting = random.choice(greetings)
            print(greeting)
            print(fact)

            while True:
                another_fact = input("Agent: Want to know another interesting fact? (yes/no): ").lower()
                if another_fact in ["yes", "y"]:
                    break
                elif another_fact in ["no", "n"]:
                    print("Agent: Alright! Have a great day!")
                    return
                else:
                    print("Agent: Hmm, I didn't understand that. Please answer 'yes' or 'no'.")
        else:
            print("Agent: Sorry, I couldn't find a science fact right now. Maybe try again later!")
            return

if __name__ == "__main__":
    main()