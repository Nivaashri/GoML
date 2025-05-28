This project provides a simple AI-powered flight information query system using Python and JSON. Users can input queries regarding flight details, and the system will respond accordingly.

Installation:
    Ensure you have Python installed (Python 3.x recommended).
    Install necessary dependencies
        pip install -r requirements.txt
        json (built-in, no installation needed)
        python-dotenv (for environment variable management)

Running the Code
    Ensure flights.json contains the necessary flight details.
    Run the script using:
         python main.py
    Type your queries about flight details, such as:
        "AI123"
        "What time does AI123 depart?"
        "Where is AI456 going?"
        "What is the status of AI456?"
        Type exit to quit the program.

Approach for Multi-Agent Function Calling 
    This system simulates a multi-agent approach:
        Information Agent (info_agent_request)
            Loads and retrieves flight data from flights.json.
            Returns structured flight details in JSON format.
        QA Agent (qa_agent_respond)
            Processes user queries and extracts the flight number.
            Calls info_agent_request to fetch flight details.
            Interprets user intent and formats responses accordingly.
            Handles cases such as flight status, departure time, and destination.

This modular approach allows easy expansion, such as integrating APIs for real-time flight tracking or adding a Natural Language Processing (NLP) layer for better query interpretation.

Example Interaction
    Welcome to the Airline AI Call Center! Type your query or 'exit' to quit.
    You: What time does AI123 depart?
    AI: {"answer": "Flight AI123 departs at 08:00 AM."}
    You: What is the status of AI456?
    AI: {"answer": "Current status of Flight AI456: On Time."}
    You: exit
    Goodbye!