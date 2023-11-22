# def runners_data():
#     with open("Runners.txt") as input:
#         lines = input.readlines()
#     runners_name = []
#     runners_id = []
#     for line in lines:
#         split_line = line.split(",")
#         runners_name.append(split_line[0])
#         id = split_line[1].strip("\n")
#         runners_id.append(id)
#     return runners_name, runners_id


def read_integer(prompt):
    while True:
        try:
            users_input = int(input(prompt))
            if users_input >= 0:
                return users_input
        except ValueError:
            print("Sorry -numbor olny please")


def read_nonempty_string(prompt):
    while True:
        users_input = input(prompt)
        if len(users_input) > 0 and users_input.isalpha():
            break
    return users_input



def race_venues():
    with open("Races.txt") as input:
        lines = input.readlines()
    races_location = []
    for line in lines:
        races_location.append(line.strip("\n"))
    return races_location



def users_venue(races_location, runners_id):
    while True:
        user_location = read_nonempty_string("Where will the new race take place? ").capitalize()
        if user_location not in races_location:
            break
    connection = open(f"{user_location}.txt", "a")
    races_location.append(user_location)
    time_taken = []
    updated_runners = []
    for i in range(len(runners_id)):
        time_taken_for_runner = read_integer(f"Time for {runners_id[i]} >> ")
        if time_taken_for_runner == 0:
            time_taken.append(time_taken_for_runner)
            updated_runners.append(runners_id[i])
            print(f"{runners_id[i]},{time_taken_for_runner},", file=connection)
    connection.close()


def read_integer_between_numbers(prompt, mini, maximum):
    while True:
        try:
            users_input = int(input(prompt))
            if maximum <= users_input >= mini:
                return users_input
            else:
                print(f"Numbers from {mini} to {maximum} only.")
        except ValueError:
            print("Sorry -numbor olny please")



def competitors_by_county(name, id):
    print("Cork runners")
    print("=" * 20)
    for i in range(len(name)):
        if id[i].startswith("CK"):
            print(f"{name[i]} ({id[i]})")
    print("Kerry runners")
    print("=" * 20)
    for i in range(len(name)):
        if id[i].startswith("KY"):
            print(f"{name[i]} ({id[i]})")


def reading_race_results_of_relevant_runner(location, runner_id):
    with open(f"{location}.txt") as input_type:
        lines = input_type.readlines()
    id = []
    time_taken = []
    for line in lines:
        if line != "\n":
            split_line = line.split(",".strip("\n"))
            id.append(split_line[0])
            time_taken.append(int(split_line[1]))
    for i in range(len(id)):
        if runner_id == id[i]:
            time_relevant_runner = time_taken[i]
            return time_relevant_runner
    return None

def displaying_race_times_one_competitor(races_location, runner, id):
    print(f"{runner} ({id})")
    print(f"-"*35)
    for i in range(len(races_location)):
        time_taken = 1000#eading_race_results_of_relevant_runner(races_location[i], id)
        if time_taken is not None:
            minutes, seconds = 10, 30#convert_time_to_minutes_and_seconds(time_taken)
            came_in_race, number_in_race = "3rd", 3#sorting_where_runner_came_in_race(races_location[i], time_taken)
            print(f"{races_location[i]} {minutes} mins {seconds} secs ({came_in_race} of {number_in_race})")


def displaying_runners_who_have_won_at_least_one_race(races_location, runners_name, runners_id):
    print(f"The following runners have all won at least one race:")
    print(f"-" * 55)
    winners = []
    runners = []
    for i, location in enumerate(races_location):
        id, time_taken = "ck_23", 1000#reading_race_results(location)
        fastest_runner = "ck_23" #winner_of_race(id, time_taken)
        name_of_runner = "John" #finding_name_of_winner(fastest_runner, runners_id, runners_name)
        if fastest_runner not in winners:
            winners.append(fastest_runner)
            runners.append(name_of_runner)
    for i, fastest_runner in enumerate(winners):
        print(f"{runners[i]} ({fastest_runner})")


def relevant_runner_info(runners_name, runners_id):
    for i in range(len(runners_name)):
        print(f"{i + 1}: {runners_name[i]}")
    user_input = read_integer_between_numbers("Which Runner > ", 1, len(runners_name))
    runner = runners_name[user_input - 1]
    id = runners_id[user_input -1]
    return runner, id


def runners_data():
    with open("./Runners-1.txt") as input:
        lines = input.readlines()
    runners_name = []
    runners_id = []
    for line in lines:
        split_line = line.split(",")
        runners_name.append(split_line[0])
        id = split_line[1].strip("\n")
        runners_id.append(id)
    return runners_name, runners_id


def test():
    runners, id = runners_data()
    print(relevant_runner_info(runners, id))
test()