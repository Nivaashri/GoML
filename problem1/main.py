from dotenv import load_dotenv
import os
import json

load_dotenv()
api_key = os.getenv("API_KEY")

def load_flight_data():
    """Loads flight data from flights.json."""
    try:
        with open("flights.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def get_flight_info(flight_number: str) -> dict:
    """Fetches flight information from the JSON database."""
    flight_db = load_flight_data()
    return flight_db.get(flight_number, {})

def info_agent_request(flight_number: str) -> str:
    """Calls get_flight_info and returns the data as a JSON string."""
    flight_data = get_flight_info(flight_number)
    return json.dumps(flight_data) if flight_data else json.dumps({"error": "Flight not found"})

def qa_agent_respond(user_query: str) -> str:
    """Processes user query, fetches flight info, and returns a structured JSON response."""
    words = user_query.split()
    flight_number = next((word for word in words if word.startswith("AI")), None)

    if not flight_number:
        return json.dumps({"answer": "No valid flight number found in query."})

    flight_info_json = info_agent_request(flight_number)
    flight_info = json.loads(flight_info_json)

    if "error" in flight_info:
        return json.dumps({"answer": f"Flight {flight_number} not found in database."})

    if user_query.strip() == flight_number:
        return json.dumps(flight_info, indent=2)

    if "time" in user_query.lower() or "depart" in user_query.lower():
        return json.dumps({"answer": f"Flight {flight_number} departs at {flight_info['departure_time']}."})
    
    if "destination" in user_query.lower() or "where" in user_query.lower():
        return json.dumps({"answer": f"Flight {flight_number} is going to {flight_info['destination']}."})
    
    if "status" in user_query.lower():
        return json.dumps({"answer": f"Current status of Flight {flight_number}: {flight_info['status']}."})

    return json.dumps({"answer": f"Flight {flight_number} departs at {flight_info['departure_time']} to {flight_info['destination']}. Current status: {flight_info['status']}."})

if __name__ == "__main__":
    print("Welcome to the Airline AI Call Center! Type your query or 'exit' to quit.")
    while True:
        user_query = input("You: ").strip()
        if user_query.lower() == "exit":
            print("Goodbye!")
            break
        response = qa_agent_respond(user_query)
        print("AI:", response)
