# garden_advice.py

def get_gardening_advice(season, plant_type):
    """
    Returns gardening advice based on the season and plant type.
    """
    # Advice data structured by season and plant type
    advice_data = {
        "summer": {
            "general": "Water your plants regularly and provide some shade.",
            "flower": "Use fertiliser to encourage blooms.",
            "vegetable": "Keep an eye out for pests!"
        },
        "winter": {
            "general": "Protect your plants from frost with covers.",
            "flower": "Move flowers indoors if possible.",
            "vegetable": "Use mulch to protect root vegetables."
        }
    }

    # Default responses
    default_season_advice = "No advice for this season."
    default_plant_advice = "No advice for this type of plant."

    # Get season-specific advice or fallback
    season_advice = advice_data.get(season, {})
    advice = season_advice.get("general", default_season_advice) + "\n"

    # Get plant-type-specific advice or fallback
    advice += season_advice.get(plant_type, default_plant_advice)

    return advice


def recommend_plants_by_season(season):
    """
    Suggests plant types that thrive in a given season.
    """
    season_plants = {
        "summer": ["Sunflowers", "Tomatoes", "Lavender"],
        "winter": ["Kale", "Broccoli", "Pansies"]
    }
    return season_plants.get(season, ["No recommendations available."])


# === Main Program ===

# Get user input for season and plant type
season = input("Enter the season (e.g., summer, winter): ").lower()
plant_type = input("Enter the plant type (e.g., flower, vegetable): ").lower()

# Get and print gardening advice
advice = get_gardening_advice(season, plant_type)
print("\nGardening Advice:")
print(advice)

# Recommend plants for the season
recommendations = recommend_plants_by_season(season)
print("\nRecommended Plants for", season.capitalize() + ":")
for plant in recommendations:
    print("- " + plant)
