def calculate_budget(budget, days):
    try:
        budget = float(budget)
        days = int(days)

        daily_budget = budget / days
        food = daily_budget * 0.3
        stay = daily_budget * 0.4
        transport = daily_budget * 0.2
        activities = daily_budget * 0.1

        return {
            "daily_budget": round(daily_budget, 2),
            "food": round(food, 2),
            "stay": round(stay, 2),
            "transport": round(transport, 2),
            "activities": round(activities, 2)
        }

    except:
        return None
