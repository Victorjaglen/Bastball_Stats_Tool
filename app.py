import constants   # Importing external constants (PLAYERS and TEAMS data)
import copy   # For deep copying the original data structures to prevent mutations
import random   # For randomly selecting players for teams

if __name__ == "__main__":

    # Creating deep copies of players and teams from constants to avoid modifying the original data
    players_copy = copy.deepcopy(constants.PLAYERS)
    teams_copy = copy.deepcopy(constants.TEAMS)

    # Function to clean and process players data
    def clean_data():

        updated_list = []  # This list will store cleaned player data

        # Iterate over the player dictionaries in players_copy
        for dictionary in players_copy:
            name = dictionary["name"]
            guardians = dictionary["guardians"].split(" and ")
            experience = dictionary["experience"]
            experience_bool = experience == "YES"
            height = int(dictionary["height"].split()[0])

            # Created a new dictionary with the cleaned data
            updated_player = {
                "name": name,
                "guardians": guardians,
                "experience": experience_bool,
                "height": height}

            updated_list.append(updated_player)

        # Return the cleaned player list
        return updated_list

    # Got the cleaned player data
    players_cleaned_list = (clean_data())

    # Function to balance the teams by dividing players equally
    def balance_teams():

        # Filtering the experienced players from the cleaned list
        experienced_players = [player for player in players_cleaned_list if player["experience"]]

        # Determining the number of experienced players per team
        num_exp_per_team = len(experienced_players) // len(teams_copy)

        # Randomly assigned experienced players to the Panthers team and remove them from the pool
        Panthers = random.sample(experienced_players, num_exp_per_team)
        for player in Panthers:
            experienced_players.remove(player)

        # Randomly assign experienced players to the Bandits team and remove them from the pool
        Bandits = random.sample(experienced_players, num_exp_per_team)
        for player in Bandits:
            experienced_players.remove(player)

        # The remaining experienced players are assigned to the Warriors team
        Warriors = experienced_players

        # Combine all assigned players into one list
        all_players = Panthers + Bandits + Warriors

        # Identify any players who have not been assigned to a team
        unassigned_players = [player for player in players_cleaned_list if player not in all_players]

        # Create a list of all teams
        all_teams = Panthers, Bandits, Warriors

        # Distribute unassigned players evenly across the teams
        while unassigned_players:
            for team in all_teams:
                if unassigned_players:
                    team.append(unassigned_players.pop())

        # Return the final balanced teams
        return Panthers, Bandits, Warriors

    # Got the balanced teams
    Panthers, Bandits, Warriors = balance_teams()

    # Display title and menu
    print("\n BASKETBALL TEAM STATS TOOL \n")
    print("-----------Menu----------- \n")

    # Function to display the lists of player names for each team
    def display_lists():

        Panthers_display_dict = [player["name"] for player in Panthers]
        Bandits_display_dict = [player["name"] for player in Bandits]
        Warriors_display_dict = [player["name"] for player in Warriors]

        # Return the lists of player names for each team
        return Panthers_display_dict, Bandits_display_dict, Warriors_display_dict

    # Got the lists of player names
    Panthers_display_dict, Bandits_display_dict, Warriors_display_dict = display_lists()

    # Function to create lists of guardians for each team
    def guardian_lists():

        Panthers_guardian_dict = [player["guardians"] for player in Panthers]
        Bandits_guardian_dict = [player["guardians"] for player in Bandits]
        Warriors_guardian_dict = [player["guardians"] for player in Warriors]

        # Return the lists of guardians for each team
        return Panthers_guardian_dict, Bandits_guardian_dict, Warriors_guardian_dict

    # Got the lists of guardians for each team
    Panthers_guardian_dict, Bandits_guardian_dict, Warriors_guardian_dict = guardian_lists()

    # Function to format guardians names into a comma-separated string
    def formatted_guardians(given_dict):
        guardians = [", ".join(guardians) for guardians in given_dict]
        return guardians

    # Function to count the number of experienced players on a team
    def count_exp_pl(any_list):
        return sum(1 for player in any_list if player["experience"])

    # Function to count the number of inexperienced players on a team
    def count_in_exp_pl(any_list):
        return sum(1 for player in any_list if not player["experience"])

    # Function to create lists of player heights for each team
    def heights():
        Panthers_height_dict = [player["height"] for player in Panthers]
        Bandits_height_dict = [player["height"] for player in Bandits]
        Warriors_height_dict = [player["height"] for player in Warriors]

        return Panthers_height_dict, Bandits_height_dict, Warriors_height_dict

    Panthers_height_dict, Bandits_height_dict, Warriors_height_dict = heights()

    # Function to calculate the average height of players on a team
    def average_height(given_dict):
        average_height = round(sum(given_dict) / len(given_dict), 1)
        return average_height


    def stats_display():
        # Infinite loop to display the menu repeatedly until the user chooses to quit
        while True:

            # Displaying the main menu options and prompting the user for input
            choice_made = input(f"Here are your choices: \n    \033[92m1\033[0m) Display Team stats \n    \033[92m2\033[0m) Quit \n \n ENTER an option: ")

            # If the user selects '1' (to display team stats)
            if choice_made.lower() == '1':
                team_choice = input("\n    \033[92m1\033[0m) Panthers \n    \033[92m2\033[0m) Bandits \n    \033[92m3\033[0m) Warriors \n \n ENTER an option : ")

                # If the user selects '1' (Panthers team)
                if team_choice.lower() == '1':
                    # Print the stats for the Panthers team
                    print(f"\n Team: Panthers Stats \n --------------- \n Total Players: \033[92m{len(Panthers)}\033[0m \n \n Total Experienced Players: \033[92m{count_exp_pl(Panthers)}\033[0m \n \n Total Inexperienced Players: \033[92m{count_in_exp_pl(Panthers)}\033[0m \n \n Average Height : \033[94m{average_height(Panthers_height_dict)}\033[0m\n \n Players on team: \n    {', '.join(Panthers_display_dict)} \n \n Guardians: \n    {', '.join(formatted_guardians(Panthers_guardian_dict))} \n ")
                    # Pause and wait for the user to press ENTER before continuing
                    input('Press ENTER to \033[94mcontinue...\033[0m\n')

                # If the user selects '2' (Bandits team)
                elif team_choice.lower() == '2':
                    # Print the stats for the Bandits team
                    print(f"\n Team: Bandits Stats \n --------------- \n Total Players: \033[92m{len(Bandits)}\033[0m \n \n Total Experienced Players: \033[92m{count_exp_pl(Bandits)} \033[0m\n \n Total Inexperienced Players: \033[92m{count_in_exp_pl(Bandits)}\033[0m \n \n Average Height : \033[94m{average_height(Bandits_height_dict)}\033[0m\n \n Players on team: \n    {', '.join(Bandits_display_dict)} \n \n Guardians: \n    {', '.join(formatted_guardians(Bandits_guardian_dict))}\n ")
                    # Pause and wait for the user to press ENTER before continuing
                    input('Press ENTER to \033[94mcontinue...\033[0m\n')

                # If the user selects '3' (Warriors team)
                elif team_choice.lower() == '3':
                    # Print the stats for the Warriors team
                    print(f"\n Team: Warriors Stats \n --------------- \n Total Players: \033[92m{len(Warriors)}\033[0m \n \n Total Experienced Players: \033[92m{count_exp_pl(Bandits)}\033[0m \n \n Total Inexperienced Players: \033[92m{count_in_exp_pl(Warriors)}\033[0m \n \n Average Height : \033[94m{average_height(Warriors_height_dict)}\033[0m\n \n  Players on team: \n    {', '.join(Warriors_display_dict)} \n \n Guardians: \n    {', '.join(formatted_guardians(Warriors_guardian_dict))}\n ")
                    # Pause and wait for the user to press ENTER before continuing
                    input('Press ENTER to \033[94mcontinue...\033[0m\n')

                # If the user enters an invalid choice for team selection
                else:
                    print('\nThat is not a valid choice please choose from the Options given below \n')

            # If the user selects '2' (to quit the program)
            elif choice_made.lower() == '2':
                print("\nHave a good day! \n")
                break  # Exit the loop and end the program

            # If the user enters an invalid choice for the main menu
            else:
                print('\nThat is not a valid input, Please make a choice from the options given \n')


    stats_display()   #Function call to run Display Options & Stats
