import sys 
from pathlib import Path


class Leaderboard: 
    def __init__(self):
        
        # file path for the data storage 
        self.datafolder = Path("../data/")
        self.file_to_open = self.datafolder / ""

    def displayElement(elementType, element):

        # element type is a string 