AI-Based Travel Planning Agent
Overview

This project is an AI-powered travel planning agent that generates personalized travel itineraries for any destination using natural language input.
It combines agentic reasoning with tool-based logic to help users plan trips while considering constraints such as time, budget, and preferences, all through an interactive Streamlit interface.

The system is designed to be scalable, ethical, and user-centric, avoiding web scraping and unsafe parsing while still delivering realistic travel recommendations.

Key Features

Works for any destination
Agentic reasoning using LangChain
Structured day-wise travel itinerary
Automatic Veg / Non-Veg restaurant & café recommendations
City-aware hotel suggestions with estimated pricing
15% VIT student discount (optional user preference)
Google Maps links for easy location discovery

Interactive Streamlit UI
System Architecture & Design

The project follows a clean separation of concerns:

1️⃣ LLM (Groq + LangChain)

Generates:

Day-wise travel itinerary

Food & café recommendations

Handles creative reasoning and narrative generation

2️⃣ Tools / Services (Python)

Hotel Service

Estimates hotel prices dynamically based on city demand

Discount Service

Applies user-specific discounts (e.g., VIT student)

3️⃣ UI Layer (Streamlit)

Collects user input

Displays structured outputs clearly

Design Principle:
LLM for reasoning and creativity, tools for deterministic logic.

  Tech Stack

Python 3.11

LangChain

Groq LLM (LLaMA-3.1-8B-Instant)
  How the System Works

User enters destination and trip duration

LLM generates:

Structured day-wise itinerary

Veg / Non-Veg food recommendations

Hotel service estimates city-based prices

Discount service applies user preference (if applicable)

Results are displayed interactively in Streamlit

Conclusion

This project demonstrates agent-based AI design, tool integration, and user-centric system thinking, fulfilling all mandatory requirements and multiple brownie points for the task.

Author

Shubham Goenka
AI / ML Project — Travel Planning Agent

Streamlit

python-dotenv
