from pickle import TRUE
from re import A
from types import new_class
import pandas as pd
import numpy as np


class read_clasify:
    def __init__(self, file_p):

        self.Update = file_p

    def read_clsify(self, opt):
        new_list_2 = []
        for brand in self.Update:
            if self.Update[brand]["update"]:
                goalsNum = len(self.Update[brand]["metric"])
                new_list_1 = []
                for i in range(goalsNum):

                    valueField = self.Update[brand]["metric"][i][1]
                    view = self.Update[brand]["view"]
                    file = f"{view}{valueField}000000000000"
                    df = pd.read_csv(
                        f"C:\\Users\\Santiago\\Documents\\GitHub\\Web_site_goal_final_version\\input\\{file}.csv"
                    )
                    a = int(len(df))

                    if a != 0 and opt == "viewName":
                        for i in range(a):
                            new_list_1.append(self.Update[brand][opt])
                        new_list_2.append(new_list_1)
                    #

                    elif a != 0 and opt == "view":
                        for i in range(a):
                            new_list_1.append(self.Update[brand][opt])
                        new_list_2.append(new_list_1)

                    elif a != 0 and opt == "goalname":
                        s = 0
                        for s in range(a):
                            new_list_2.append(self.Update[brand]["metric"][i][2])

        return new_list_2

    def clean(self, hola):
        # initializing the data and an empty list
        data = hola
        flat_list = []

        # iterating over the data
        for item in data:
            # appending elements to the flat_list
            flat_list += item

        # printing the resultantn flat_list
        return flat_list

        # for i  in range (int(len(df))):
        # df1 = np.where(df.empty == False , self.Update[brand]['viewName'], 'vacio')
        # if df1 == 'vacio'
        # print (df1)
        # df2 = df['ViewID'] = self.Update[brand]['view']
        # df3 = df['GoalName'] = goalName
        # print(df1)
