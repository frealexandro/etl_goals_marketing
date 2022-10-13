import pandas as pd
import numpy as np 
import re

#how to merge two dataframes with python


"""This object has the capacity of convert the 
    different lines with errors in CLEAN LINE"""


class Fix_Goals:

    def __init__(self,file,regex):
        
        self.file = file

        self.regex = regex

    def match_goals(self):
        
        x = re.search( self.regex , self.file)
        
        for i in x:
            print(i)