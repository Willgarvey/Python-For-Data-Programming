#!/usr/bin/env python3

# db.py contains the functions to load and save player data in a dictionary to and from a bin file
import db

from datetime import datetime, date

POSITIONS = ("P", "C", "1B", "2B", "3B", "SS", "LF", "CF", "RF")

def show_dates():
    while True:
        game_date_str = input("Enter date of next game (YYYY-MM-DD) or x to skip: ")
        if game_date_str == "x":
            print()
            print("================================================================")
            print("                     Baseball Team Manager                      ")
            print()
            break
        else:
            try:
                game_date = datetime.strptime(game_date_str, "%Y-%m-%d")
            except ValueError:
                print("Invalid date format. Please try again.")
                continue
            today = date.today()
            game_date = game_date.date()
            days_until = (game_date - today).days
            print()
            print("================================================================")
            print("                     Baseball Team Manager                      ")
            print()
            if days_until < 0:
                break
            else:
                print(f"CURRENT DATE: {today}")
                print(f"GAME DATE: {game_date}")
                print(f"DAYS UNTIL NEXT GAME: {days_until}")
                print()
                break
            
def main_menu():
    """displays the menu options available in the program"""
    
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
    print("================================================================")
    
def display_lineup(players_dictionary):
    """iterates through the players_dictionary to display the player lineup with 64-character width formatting"""
    print(f"{' ':<6}{'Player':<30} {'POS':<5} {'AB':<7} {'H':<7} {'AVG':<5}")
    print("----------------------------------------------------------------")  
    i=1
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
                print(f"{lineup_position:<5} {player:<30} {position:<5} {at_bats:<7} {hits:<7} {average:<5}")
                i=i+1
                lineup = lineup + 1
    print("")
    
def add_player(players_dictionary):
    """add a new player to the database inluding player name, position, AB, and H"""
    
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
        
    # input from the user is formatted into a list called new_player to be added to the players list
    new_player_dict = {"position" : player_position, "at_bats" : at_bats, "hits" : hits, "lineup_position" : len(players_dictionary) + 1}
    players_dictionary[name] = new_player_dict
    print(f"{name} was added to the lineup!")
    return players_dictionary
    
def remove_player(players_dictionary):
    """removes a player from the list by confirming their number in the lineup"""
    display_lineup(players_dictionary)
    
    # first checks if there is anyone in the list
    while True:
        if len(players_dictionary) == 0:
            print ("There are no players to remove!")
            break
        # input from the user is checked to see if it is a number in the lineup
        else:
            try: 
                option = int(input("Which player do you want to delete?: "))
            except TypeError:
                print("Invalid option number.")
                continue
            except ValueError:
                print("Invalid option number.")
                continue   
            except IndexError:
                print("Invalid option number.")
                continue
            
            #prevent negative number index selections
            if option <= 0:
                print("Invalid option number.")
                continue
            
            # removes player and saves the lineup
            else:
                for player in players_dictionary:
                    lineup_position = players_dictionary[player]["lineup_position"]
                    if option == lineup_position:
                        del players_dictionary[player]
                        break
                db.save_lineup(players_dictionary)
                print(f"{player} has been removed from the player lineup")
                break
    
def move_player(players_dictionary):
    """move a player to a different location in the list"""
    display_lineup(players_dictionary)
    
    while True:
        # check if the players list is empty
        if len(players_dictionary) == 0:
            print("There are no players to move.")
            break
        # input from the user to select a player from the list to change their list position
        else:
            try: 
                old_lineup_position = int(input("Which player do you want to move?: "))
            except TypeError:
                print("Invalid option number.")
                continue
            except ValueError:
                print("Invalid option number.")
                continue    
            except IndexError:
                print("Invalid option number.")
                continue
            if old_lineup_position <= 0:
                print("Invalid option number.")
                continue
            if old_lineup_position > len(players_dictionary):
                print("Invalid option number")
                continue
            else:
                break
    # input from the user to select a position in the list to move the player to
    while True:
        try:
            new_lineup_position = int(input("Where do you want to place the player in the lineup?"))
        except TypeError:
            print("Invalid option number.")
            continue
        except ValueError:
            print("Invalid option number.")
            continue    
        except IndexError:
            print("Invalid option number.")
            continue
        if new_lineup_position <= 0:
            print("Invalid option number.")
            continue
        if new_lineup_position > len(players_dictionary):
            print("Invalid option number")
            continue
        #Get the name of the player you are moving
        else:
            for player in players_dictionary:
                lineup_position = players_dictionary[player]["lineup_position"]
                if lineup_position == old_lineup_position:
                    players_dictionary[player]["lineup_position"] = new_lineup_position
                    moved_player = f"{player}"
                    break
                
            #Iterate through players and change their lineup position accordingly
            for player in players_dictionary:
                lineup_position = players_dictionary[player]["lineup_position"]
                if lineup_position < new_lineup_position and lineup_position < old_lineup_position:
                    continue
                elif lineup_position > new_lineup_position and lineup_position > old_lineup_position:
                    continue
                elif lineup_position == new_lineup_position and player == moved_player:
                    continue
                elif lineup_position == new_lineup_position and player != moved_player and lineup_position == len(players_dictionary):
                    players_dictionary[player]["lineup_position"] = players_dictionary[player]["lineup_position"] - 1
                    continue
                elif lineup_position == new_lineup_position and lineup_position > old_lineup_position and player != moved_player and lineup_position != len(players_dictionary):
                    players_dictionary[player]["lineup_position"] = players_dictionary[player]["lineup_position"] - 1
                    continue
                elif lineup_position == new_lineup_position and lineup_position < old_lineup_position and player != moved_player and lineup_position != len(players_dictionary):
                    players_dictionary[player]["lineup_position"] = players_dictionary[player]["lineup_position"] + 1
                    continue
                elif lineup_position < old_lineup_position and lineup_position > new_lineup_position:
                    players_dictionary[player]["lineup_position"] = players_dictionary[player]["lineup_position"] +1
                    continue
                elif lineup_position > old_lineup_position and lineup_position < new_lineup_position:
                    players_dictionary[player]["lineup_position"] = players_dictionary[player]["lineup_position"] - 1
                    continue  
                else:
                    players_dictionary[player]["lineup_position"] = players_dictionary[player]["lineup_position"] - 1
                    continue
                
            #save the player_dictionary to players.bin
            db.save_lineup(players_dictionary)
            print(f"{moved_player} has been moved to position {new_lineup_position} in the lineup")
            break          
                
def edit_player_position(players_dictionary):
    """select a player from the list to modify their statistics entries"""
    
    display_lineup(players_dictionary)
    
    while True:
        # first checks if there is anyone in the list
        if len(players_dictionary) == 0:
            print ("There are no players to edit!")
            break
        # User input selects lineup position of player they want to edit stats for and errors are handled
        else:
            try: 
                option = int(input("Which player do you want to change positions?: "))
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
    # User input selects the new position for the selected player
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
        
        #check if position is in the POSITIONS tuple of valid positions
        if baseball_position in POSITIONS:
            
            # find the player with the corresponding lineup position and checnges their position
            for player in players_dictionary:
                lineup_position = players_dictionary[player]["lineup_position"]
                if option == lineup_position:
                    players_dictionary[player]["position"] = baseball_position
                    break
            # save players_dictionary to players.bin
            db.save_lineup(players_dictionary)
            print(f"{player} has changed their position to {baseball_position}.")
            break
        else:
            print("Invalid position. Please enter a new position and try again.")
            continue
        
def edit_player_stat(players_dictionary):
    """select a player from the list to modify their statistics entries"""
    display_lineup(players_dictionary)
    while True:
        # check if there are any player in the list
        if len(players_dictionary) == 0:
            print("There are no players to change statics for.")
            break
        # input from the user to select a player from the list to change their statistics
        else:
            try: 
                option = int(input("Which player do you want to change statistics for?: "))
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
    # input from the user to set a new At Bats (AB) statistic
    while True:
        try:
            at_bats = int(input("Enter new At Bats (AB) statistic:"))
        except TypeError:
            print("Invalid option number.")
            continue
        except ValueError:
            print("Invalid option number.")
            continue    
        except IndexError:
            print("Invalid option number.")
            continue
        if at_bats <= 0:
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
        if hits > at_bats:
            print("Hits must be less than or equal to at-bats.")
            continue
        else:
            # updates the (AB) and (H) stat for the selected player
            for player in players_dictionary:
                lineup_position = players_dictionary[player]["lineup_position"]
                if option == lineup_position:
                    players_dictionary[player]["at_bats"] = at_bats
                    players_dictionary[player]["hits"] = hits
                    db.save_lineup(players_dictionary)
                    print(f"Statistics for {player} updated successfully!")
                    return players_dictionary
            
def main():
    """start a loop of user input options that manipulate the data until exit is triggered"""
    
    players_dictionary = {}
    players_dictionary = db.load_lineup(players_dictionary)
    
    show_dates()
    
    main_menu()
    
    option = 1
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