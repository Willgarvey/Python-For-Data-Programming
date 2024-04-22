#!/usr/bin/env python3

# this file serves as a db module for baseball_team_manager.py
# functions include loading a bin file into a players list
# and saving the players list to a bin file

import pickle
players_dictionary = {}

#load existing data from birds.bin
def load_lineup(players_dictionary):
    try:
        with open("players.bin", "rb") as file:
            players_dictionary = pickle.load(file)
        return players_dictionary
    except FileNotFoundError:
        print("No players data found. Creating empty players file...")
        print()
        with open("players.bin", "wb") as file:
            pickle.dump(players_dictionary, file)
        return players_dictionary
    
    
def save_lineup(players_dictionary):
    with open("players.bin", "wb") as file:
        pickle.dump(players_dictionary, file)