import streamlit as st
from agent.agent import llm
from services.discount_service import apply_vit_discount
from services.hotel_service import search_hotels

st.set_page_config(page_title="AI Travel Planner", layout="wide")

st.title("✈️ AI-Based Travel Planning Agent")

destination = st.text_input("Where do you want to travel?")
days = st.number_input("Number of days", 1, 15, 3)
vit_student = st.checkbox("Are you a VIT student? (15% discount)")

if st.button("Generate Travel Plan") and destination:

   
    st.subheader("🧠 Travel Plan & Itinerary")

    agent_prompt = f"""
    You are an expert travel planner.

    Create a detailed {days}-day travel itinerary for {destination}.
    Each day MUST include:
    - Morning activity (specific place)
    - Afternoon activity (specific place or food experience)
    - Evening activity (specific attraction or experience)

    Use REAL, WELL-KNOWN places and restaurants in {destination}.
    Do NOT be generic.
    Do NOT repeat places across days.

    After the itinerary, add a short paragraph explaining
    why this trip plan is well-balanced.

    Format strictly as:
    Day 1:
    - Morning: ...
    - Afternoon: ...
    - Evening: ...

    Day 2:
    ...
    """

    agent_response = llm.invoke(agent_prompt).content
    st.write(agent_response)
    #FOOD & CAFE RECOMMENDATIONS (AUTO, LLM-DRIVEN)
    st.subheader("🍽️ Food & Cafe Recommendations")

    food_prompt = f"""
    You are a local food expert.

    List famous and trusted food places in {destination}.
    Divide them strictly into:
    Vegetarian and Non-Vegetarian.

    Rules:
    - Use REAL, POPULAR restaurant or cafe names.
    - Avoid generic names.
    - 4 to 6 items per category.
    - No explanations, only names.

    Format EXACTLY like this:

    Vegetarian:
    - Place 1
    - Place 2
    - Place 3

    Non-Vegetarian:
    - Place 1
    - Place 2
    - Place 3
    """

    food_response = llm.invoke(food_prompt).content

    veg_places = []
    nonveg_places = []

    current = None
    for line in food_response.splitlines():
        line = line.strip()
        if line.lower().startswith("vegetarian"):
            current = "veg"
        elif line.lower().startswith("non-vegetarian"):
            current = "nonveg"
        elif line.startswith("-") and current:
            if current == "veg":
                veg_places.append(line[1:].strip())
            else:
                nonveg_places.append(line[1:].strip())

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🟢 Vegetarian")
        for place in veg_places:
            map_link = f"https://www.google.com/maps/search/{place.replace(' ', '+')}+{destination}"
            st.markdown(f"- **{place}**  \n  📍 [View on Maps]({map_link})")

    with col2:
        st.markdown("### 🔴 Non-Vegetarian")
        for place in nonveg_places:
            map_link = f"https://www.google.com/maps/search/{place.replace(' ', '+')}+{destination}"
            st.markdown(f"- **{place}**  \n  📍 [View on Maps]({map_link})")


    # HOTEL DEALS (ONLY ONCE, BOTTOM)
    st.subheader("🏨 Hotel Deals")

    hotels = search_hotels(destination)

    for h in hotels:
        final_price = apply_vit_discount(h["price"], vit_student)
        map_link = f"https://www.google.com/maps/search/{h['map_query'].replace(' ', '+')}"

        st.markdown(f"""
        **🏨 {h['name']}**
        - Category: {h['category']}
        - Area: {h['area']}
        - Rating: ⭐ {h['rating']}
        - Price per night: ₹{final_price}
        - Deal: {h['deal']}
        - 📍 [View nearby hotels on Google Maps]({map_link})
        """)

