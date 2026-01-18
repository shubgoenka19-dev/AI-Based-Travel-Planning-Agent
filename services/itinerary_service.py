def generate_itinerary(destination: str, days: int):
    base_templates = [
        "Visit the most popular historical landmark",
        "Explore a famous cultural or heritage site",
        "Relax at a well-known park / scenic viewpoint",
        "Visit a local market or shopping street",
        "Try a famous local restaurant or food street",
        "Explore a nearby attraction or day-trip spot"
    ]

    itinerary = {}

    for day in range(1, days + 1):
        morning = base_templates[(day * 2 - 2) % len(base_templates)]
        afternoon = base_templates[(day * 2 - 1) % len(base_templates)]
        evening = "Leisure walk, cafes, or local exploration"

        itinerary[f"Day {day}"] = [
            f"Morning: {morning} in {destination}",
            f"Afternoon: {afternoon} in {destination}",
            f"Evening: {evening}"
        ]

    return itinerary
