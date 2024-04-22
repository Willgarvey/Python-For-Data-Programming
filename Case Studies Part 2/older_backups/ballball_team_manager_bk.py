#!/usr/bin/env python3

# db.py contains the functions to load and save player data
import db

POSITIONS = ("P", "C", "1B", "2B", "3B", "SS", "LR", "CF", "RF")

def main_menu():
    #displays the menu options available in the program
    print("====================================================================")
    print("\t\t\tBaseball Team Manager")
    print("MENU OPTIONS")
    print("1 - Display lineup")
    print("2 - Add player")
    print("3 - Remove player")
    print("4 - Move player")
    print("5 - Edit player position")
    print("6 - Edit player stats")
    print("7 - Exit program")
    print()
    print("POSITIONS")
    positions_str = ""
    for position in POSITIONS:
        positions_str = (positions_str + position + ", ")
    print(positions_str[0:-2])
    print("====================================================================")
    
def display_lineup(players_dictionary):
    print(" Player POS AB H AVG")
    print("--------------------------------------------------------------------")
    # iterates through the players_dictionary and adds padding after the name
    # if the name is less than 14 characters long so the table is
    # formatted correctly
    
#     dict_names = {
#     'd1': {
#         'name': 'bob',
#         'place': 'lawn',
#         'animal': 'man'
#     },
#     'd2': {
#         'name': 'spot',
#         'place': 'bed',
#         'animal': 'dog'
#     }
# }
    
#    dict_names['d1']['name'] 
#    >>> 'bob' 
    i=1
    next_player = 1
    lineup = 0
    while lineup < len(players_dictionary):
        for player in players_dictionary:
            try:
                lineup_position = players_dictionary[player]['lineup_position']
                position = players_dictionary[player]['position']
                hits = int(players_dictionary[player]['hits'])
                at_bats = int(players_dictionary[player]['at_bats'])
                average = hits / at_bats
                average = round(average, 3)
            except ZeroDivisionError:
                average = 0.0
            if lineup_position == i:
                #print the row of formatted information about the player
                print(f"{lineup_position}. {player} {position} {at_bats} {hits} {average}")
                i=i+1
                lineup = lineup + 1
        #print the row of formatted information about the player
    print("--------------------------------------------------------------------")
    
def add_player(players_dictionary):
    #add a new player to the database inluding player name, position, AB, and H
    new_player = {}
    #name is input from the user and validated
    while True:
        try:
            name = input(str("Player Name:"))
            name = str(name)
        except ValueError:
            print("Invalid input. Enter a string and try again")
            continue
        if name == "":
            print("name cannot be left blank")
            continue
        else:
            break
    # player_position is input by the user and checked to be 
    # one of the valid entry listed in the tuple POSITIONS
    while True:
        try:
            player_position = input(str("Player Position:"))
            player_position = str(player_position)
        except ValueError:
            print("Invalid input. Enter a string and try again")
            continue
        if player_position in POSITIONS:
            break
        else:
            print("Invalid position. Please try again")
            continue
    # player enters number for at bats and is validated    
    while True:
        try:     
            at_bats = input(str("At Bats (AB):"))
            at_bats = int(at_bats)
            if at_bats < 0:
                print("Hits must greater or equal to zero.")
                continue
        except ValueError:
            print("Invalid integer. Please try again")
            continue
        break
    # player enters hits and input is validated to not be more that total at bats 
    while True:
        try:     
            hits = input(("Hits:"))
            hits = int(hits)
            if hits < 0:
                print("Hits must greater or equal to zero.")
                continue
        except ValueError:
            print("Invalid integer. Please try again")
            continue
        if hits > at_bats:
            print("Hits must be less than or equal to At Bats (AB)")
            continue
        else:
            break
    # input from the user is formatted into a list called new_player
    # to be added to the players list
    new_player = [name, player_position, at_bats, hits]
    new_player_dict = {"position" : player_position, "at_bats" : at_bats, "hits" : hits, "lineup_position" : len(players_dictionary) + 1}
    players_dictionary[name] = new_player_dict
    print(f"{name} was added to the lineup!")
    return players_dictionary
    
def remove_player(players_dictionary):
    # removes a player from the list by confirming their number in the lineup
    display_lineup(players_dictionary)
    # first checks if there is anyone in the list
    while True:
        if len(players_dictionary) == 0:
            print ("There are no players to remove!")
            break
        else:
            try: 
                # input from the user is checked to see if it is a number in the lineup
                option = int(input("Which player do you want to delete?: "))
            except TypeError:
                print("Invalid option number.")
                continue
            except ValueError:
                print("Invalid option number.")
                continue  
            #error for if the user enters a number greater than zero that is out of range  
            except IndexError:
                print("Invalid option number.")
                continue
            #prevent negative number index selections
            if option <= 0:
                print("Invalid option number.")
                continue
            else:
                # removes player and saves the lineup
                for player in players_dictionary:
                    lineup_position = players_dictionary[player]["lineup_position"]
                    if option == lineup_position:
                        del players_dictionary[player]
                        break
                # db.save_lineup(players)
                print(f"{player} has been removed from the player lineup")
                break
    
def move_player(players_dictionary):
    # move a player to a different location in the list
    display_lineup(players_dictionary)
    
    while True:
        # check if the players list is empty
        if len(players_dictionary) == 0:
            print("There are no players to move.")
            break
        # input from the user to select a player from the list to change their list position
        else:
            try: 
                player_to_move = int(input("Which player do you want to move?: "))
            except TypeError:
                print("Invalid option number.")
                continue
            except ValueError:
                print("Invalid option number.")
                continue    
            except IndexError:
                print("Invalid option number.")
                continue
            if player_to_move <= 0:
                print("Invalid option number.")
                continue
            if player_to_move > len(players_dictionary):
                print("Invalid option number")
                continue
            else:
                break
    # input from the user to select a position in the list to move the player to
    while True:
        try:
            new_player_position = int(input("Where do you want to place the player in the lineup?"))
        except TypeError:
            print("Invalid option number.")
            continue
        except ValueError:
            print("Invalid option number.")
            continue    
        except IndexError:
            print("Invalid option number.")
            continue
        # prevents negative index inputs
        if new_player_position <= 0:
            print("Invalid option number.")
            continue
        if new_player_position > len(players_dictionary):
            print("Invalid option number")
            continue
        else:
            #Get the name of the player you are moving
            for player in players_dictionary:
                lineup_position = players_dictionary[player]["lineup_position"]
                if lineup_position == player_to_move:
                    players_dictionary[player]["lineup_position"] = new_player_position
                    moved_player = f"{player}"
                    break
            #Iterate through players and change their lineup posoition accordingly
            for player in players_dictionary:
                lineup_position = players_dictionary[player]["lineup_position"]
                if lineup_position < player_to_move and player != moved_player:
                    players_dictionary[player]["lineup_position"] = players_dictionary[player]["lineup_position"] + 1
                    print("Item was increased")
                    continue
                elif lineup_position > player_to_move and player != moved_player:
                    players_dictionary[player]["lineup_position"] = players_dictionary[player]["lineup_position"] - 1
                    print("item was decreased")
                    continue
            print(f"{moved_player} has been moved to position {new_player_position} in the lineup")
            break
            
            # move the player list to the new position in the players list and delete the original player list
            # players.insert((player_position-1), players[option-1])
            # players.pop(option)
            # print()
            # print("Batting position lineup move complete!")
            # db.save_lineup(players)
            break            
                
def edit_player_position(players_dictionary):
    # select a player from the list to modify their statistics entries
    display_lineup(players)
    while True:
        if len(players) == 0:
            break
        else:
            try: 
                option = int(input("Which player do you want to change positions?: "))
                player = players[option-1]
            except TypeError:
                print("Invalid option number.")
                continue
            except ValueError:
                print("Invalid option number.")
                continue    
            except IndexError:
                print("Invalid option number.")
                continue
            if option <= 0:
                print("Invalid option number.")
                continue
            else:
                break
    while True:
        try:
            baseball_position = str(input("Which position should this player play?"))
        except TypeError:
            print("Invalid option number.")
            continue
        except ValueError:
            print("Invalid option number.")
            continue    
        except IndexError:
            print("Invalid option number.")
            continue
        if baseball_position in POSITIONS:
            players[option-1][1] = baseball_position
            print()
            print("Baseball position change complete!")
            db.save_lineup(players)
            break
        else:
            print("Invalid position.Please enter a new position and try again.")
            continue
        
def edit_player_stat(players_dictionary):
    # select a player from the list to modify their statistics entries
    display_lineup(players)
    while True:
        # check if there are any player in the list
        if len(players) == 0:
            print("There are no players to change statics for.")
            break
        # input from the user to select a player from the list to change their statistics
        else:
            try: 
                option = int(input("Which player do you want to change statistics for?: "))
                player = players[option-1]
            except TypeError:
                print("Invalid option number.")
                continue
            except ValueError:
                print("Invalid option number.")
                continue    
            except IndexError:
                print("Invalid option number.")
                continue
            if option <= 0:
                print("Invalid option number.")
                continue
            else:
                break
    # input from the user to set a new At Bat (AB) statistic
    while True:
        try:
            at_bat = int(input("Enter new At Bat (AB) statistic:"))
        except TypeError:
            print("Invalid option number.")
            continue
        except ValueError:
            print("Invalid option number.")
            continue    
        except IndexError:
            print("Invalid option number.")
            continue
        if at_bat <= 0:
            print("Statistic must be greater than or equal to zero.")
        else:
            break 
    # input from the user to set a new Hit (H) statistic
    while True:
        try:
            hits = int(input("Enter new Hits (H) statistic:"))
        except TypeError:
            print("Invalid option number.")
            continue
        except ValueError:
            print("Invalid option number.")
            continue    
        except IndexError:
            print("Invalid option number.")
            continue
        # checks if the input is at least zero.
        if hits < 0:
            print("Statistic must be greater or equal to zero.")
            continue
        if hits > at_bat:
            print("Hits must be less than or equal to at-bats.")
            continue
        else:
            # updates the (AB) and (H) stat for the selected player
            players[option-1][2] = at_bat
            players[option-1][3] = hits
            # saves the players list to the deginated csv file
            db.save_lineup(players)
            print()
            print("Statistics updated successfully!") 
            break

def main():
    # load players from designated csv file
    
    players = db.load_lineup(players)
    players = [{"name": "Tommy La Stella", "position": "3B", "at_bats" : "1316", "hits" : "360", "lineup_position" : 1}, 
                    {"name": "Mike Yastrzemski", "position": "3B", "at_bats" : "1316", "hits" : "360", "lineup_position" : 1}, 
                    {"name": "Buster Posey", "position": "C", "at_bats" : "4575", "hits" : "1380", "lineup_position" : 4}, 
                    {"name": "Brandon Crawford", "position": "SS", "at_bats" : "4402", "hits" : "1099", "lineup_position" : 5}, 
                    {"name": "Alex Dickerson", "position": "LF", "at_bats" : "586", "hits" : "160", "lineup_position" : 6}, 
                    {"name": "Austin Slater", "position": "CF", "at_bats" : "569", "hits" : "147", "lineup_position" : 7}, 
                    {"name": "Kevin Gausman", "position": "P", "at_bats" : "56", "hits" : "2", "lineup_position" : 8},]
    
    players_dictionary = {
        "Tommy La Stella":
            {"position": "3B", "at_bats" : "1316", "hits" : "360", "lineup_position" : 1}, 
        "Mike Yastrzemski":
            {"position": "RF", "at_bats" : "563", "hits" : "168", "lineup_position" : 2},
        "Donovan Solano":
            {"position": "2B", "at_bats" : "1473", "hits" : "407", "lineup_position" : 3},
        "Buster Posey":
            {"position": "C", "at_bats" : "4575", "hits" : "1380", "lineup_position" : 4},
        "Brandon Crawford":
            {"position": "SS", "at_bats" : "4402", "hits" : "1099", "lineup_position" : 5},
        "Alex Dickerson":
            {"position": "LF", "at_bats" : "586", "hits" : "160", "lineup_position" : 6},
        "Austin Slater":
            {"position": "CF", "at_bats" : "569", "hits" : "147", "lineup_position" : 7},
        "Kevin Gausman":
            {"position": "P", "at_bats" : "56", "hits" : "2", "lineup_position" : 8}
    }
    
    option = 1
    #display the meny options 
    main_menu()
    
    # start a loop of user input options that manipulate the data until exit is triggered
    # exiting the program is the only way to save the player data to the csv file
     
    while option != "7":
        try: 
            option = input(str("Menu option:"))
        except IndexError:
            print("Please enter a valid Menu option")
            main_menu(players_dictionary)           
        if option == "1":
            display_lineup(players_dictionary)
        elif option == "2":
            add_player(players_dictionary)  
        elif option == "3":
            remove_player(players_dictionary)
        elif option == "4":
            move_player(players_dictionary)
        elif option == "5":
            edit_player_position(players_dictionary)
        elif option == "6":
            edit_player_stat(players_dictionary)
        elif option == "7":
            db.save_lineup(players_dictionary)
            print("Bye!") 
        # Any option that is not exactly correct will trigger this else statement
        # and prompt the user for another menu option
        else:
            main_menu()
            print()
            print("Please enter a valid Menu option")
            print()
            
if __name__ == "__main__":
    main()