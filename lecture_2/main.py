user_name = input("Enter your name: ")
birth_year_str = input("Enter your birth year: ")
birth_year_str = int(birth_year_str)
CURRENT_YEAR = 2025
current_age = CURRENT_YEAR - birth_year_str

hobbies = []
hobby = ''
counter = 0
while hobby != 'stop':
    hobby = input("Enter a favorite hobby or 'stop' to finish: ")
    if hobby != 'stop':
      hobbies.append(hobby)
      counter += 1


def generate_profile(age):
    if 0 <= age <= 12:
        return "Child"
    elif 13 <= age <= 19:
        return "Teenager"
    elif 20 <= age:
        return "Adult"
    return None

life_stage = generate_profile(current_age)

user_profile = {
    "Name" : user_name,
    "Age": current_age,
    "Life stage": life_stage,
    "Favorite Hobbies": hobbies
}
print(f"---\nProfile Summary: \nName: {user_profile['Name']}\nAge: {user_profile['Age']} \nLife stage: {user_profile['Life stage']}")
if not hobbies:
    print("You didn't mention any hobbies.")
else:
    print(f"My favorite hobbies ({counter}): ")
    for i in range(counter):
        print(f"- {hobbies[i]}")
print('---')

