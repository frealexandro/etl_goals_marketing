import pandas as pd
import numpy as np 


#how to merge two dataframes with python


"""This object has the capacity of convert the 
    different lines with errors in CLEAN LINE"""


class merge:

    def __init__(self,df_g,views,viewname,goal_names):
        
        self.df_g = df_g

        self.viewid = views

        self.viewname = viewname
        
        self.goalname = goal_names


    def merge_data (self):
    
# initialize data of lists.

        data_df_1 = {'view_id':  self.viewid,
                    'viewname':  self.viewname,
                    'goalnames': self.goalname,}
  
# Create DataFrame
        df_1 = pd.DataFrame(data_df_1)
        df_2 = self.df_g
        df_final = pd.concat([df_1,df_2],axis=1)
        
        return df_final 

  
# Print the output.