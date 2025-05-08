This Python script fetches and displays interesting science facts from the Numbers API. After showing a fact, it interactively asks the user if they want to learn another one.

## How to Run

1.  Make sure you have Python 3 or higher installed on your system.
2.  Download or copy the `api_agent.py` file.
3.  Open your terminal or command prompt and navigate to the directory where `api_agent.py` is located.
4.  Run the script using the following command:

    ```bash
    python api_agent.py
    ```

## How to Use

When you run the script, the Agent will greet you and present a random science fact. It will then ask if you want to know another fact.

* Type `yes` or `y` and press Enter to get another random science fact.
* Type `no` or `n` and press Enter to exit the Agent.
* If you enter an invalid response, the Agent will prompt you again for a valid answer.

## Code Explanation

The script uses the following libraries:

* `requests`: To make HTTP requests to the Numbers API.
* `json`: To handle JSON responses from the API (although in this case, the API returns plain text within a JSON object).
* `random`: To select a random greeting message for the user.

The `get_random_science_fact_from_api()` function sends a GET request to the Numbers API endpoint for a random trivia fact and returns the text of the fact.

The `main()` function handles the interaction with the user. It fetches a fact, displays it, and then enters a loop to ask the user if they want another fact until the user chooses to exit.
