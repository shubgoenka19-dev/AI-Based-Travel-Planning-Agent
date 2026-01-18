import random

CITY_MULTIPLIER = {
    "delhi": 1.3,
    "mumbai": 1.4,
    "bangalore": 1.25,
    "kolkata": 1.1,
    "chennai": 1.15,
    "pune": 1.2,
    "goa": 1.5,
    "jaipur": 1.2,
    "amritsar": 1.1,
    "default": 1.0
}

def search_hotels(destination):
    city = destination.lower()
    multiplier = CITY_MULTIPLIER.get(city, CITY_MULTIPLIER["default"])

    budget_base = random.randint(1500, 2200)
    mid_base = random.randint(3000, 4500)
    premium_base = random.randint(6500, 9000)

    return [
        {
            "name": f"{destination} Budget Stay",
            "category": "Budget",
            "rating": round(random.uniform(3.8, 4.5), 1),
            "price": int(budget_base * multiplier),
            "deal": "Best available deal (estimated)",
            "area": "Near city center",
            "map_query": f"{destination} budget hotel"
        },
        {
            "name": f"{destination} Mid-range Stay",
            "category": "Mid-range",
            "rating": round(random.uniform(4.0, 4.7), 1),
            "price": int(mid_base * multiplier),
            "deal": "Best available deal (estimated)",
            "area": "Near main market area",
            "map_query": f"{destination} mid range hotel"
        },
        {
            "name": f"{destination} Premium Stay",
            "category": "Premium",
            "rating": round(random.uniform(4.2, 4.9), 1),
            "price": int(premium_base * multiplier),
            "deal": "Best available deal (estimated)",
            "area": "Prime / luxury locality",
            "map_query": f"{destination} luxury hotel"
        }
    ]
