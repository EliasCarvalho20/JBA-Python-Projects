def select_dates(potential_dates):
    return ", ".join([n['name'] for n in potential_dates if n["age"] > 30 and "art" in n["hobbies"] and n["city"] == "Berlin"])
