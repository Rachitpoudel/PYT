def get_weekend_average_temp(weekly_temps):
    weekend_temps = []
    for day, temp in weekly_temps.items():
        if day.lower() in ['saturday', 'sunday']:
            weekend_temps.append(temp)
    if len(weekend_temps) == 0:
        return None
    return sum(weekend_temps) / len(weekend_temps)
weekly_temps = {
    'monday': 20,
    'tuesday': 21,
    'wednesday': 22,
    'thursday': 23,
    'friday': 24,
    'saturday': 25,
    'sunday': 26
}
avg_temp = get_weekend_average_temp(weekly_temps)
print(avg_temp) 
