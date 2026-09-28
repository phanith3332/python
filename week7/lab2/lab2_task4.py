# lab2_task4.py

def build_profile(**details):
    """Print a neatly formatted profile using keyword arguments."""
    print("\n--- Profile Card ---")
    for key, value in details.items():
        print(f"{key.capitalize()}: {value}")
    print("--------------------")
# First profile
build_profile(
    name="Phanith",
    age=19,
    city="tadepalligudem",
    hobby="Coding"
)
# Second profile with different details
build_profile(
    name="adithya",
    city="Chennai",
    hobby="Cricket"
)
# Third profile
build_profile(
    name="vamsi",
    age=18,
    course="B.Tech",
    branch="CSE",
    hobby="Reading"
)

'''output:
--- Profile Card ---
Name: Phanith
Age: 19
City: tadepalligudem
Hobby: Coding
--------------------

--- Profile Card ---
Name: adithya
City: Chennai
Hobby: Cricket
--------------------

--- Profile Card ---
Name: vamsi
Age: 18
Course: B.Tech
Branch: CSE
Hobby: Reading
--------------------'''
