def generate_itinerary(destination, budget, days, interests):

    days = int(days)
    daily_budget = int(budget) // days

    itinerary = f"\n🎓 AI Travel Plan for {destination}\n"
    itinerary += f"Total Budget: ₹{budget}\n"
    itinerary += f"Interests: {interests}\n\n"

    for day in range(1, days + 1):
        itinerary += f"Day {day}:\n"
        itinerary += f"- Visit top attractions in {destination}\n"
        itinerary += f"- Explore {interests.lower()} related places\n"
        itinerary += f"- Try affordable local food options\n"
        itinerary += f"- Estimated daily spending: ₹{daily_budget}\n\n"

    itinerary += "💡 Travel Tips:\n"
    itinerary += "- Use public transport\n"
    itinerary += "- Book hostels instead of hotels\n"
    itinerary += "- Use student discounts wherever possible\n"

    return itinerary
