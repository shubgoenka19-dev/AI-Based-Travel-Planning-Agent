from langchain.tools import tool
from services.hotel_service import search_hotels
from services.itinerary_service import generate_itinerary

@tool
def hotel_search_tool(destination: str):
    """Search hotels for a destination (MakeMyTrip-style)"""
    return search_hotels(destination)


@tool
def itinerary_tool(input_text: str):
    """
    Generate itinerary.
    Input format: '<destination>, <days>'
    Example: 'Goa, 4'
    """
    try:
        destination, days = input_text.split(",")
        destination = destination.strip()
        days = int(days.strip())
        return generate_itinerary(destination, days)
    except Exception:
        return "Invalid input format. Use: 'Destination, Days'"
