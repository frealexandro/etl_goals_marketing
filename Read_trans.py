from ast import pattern
import csv
import re
import pandas as pd
import numpy as np


class read_trans:
    def __init__(self, file_p):

        self.Update = file_p

    def read_transf(self):

        df_final = pd.DataFrame()
        for brand in self.Update:
            if self.Update[brand]["update"]:
                goalsNum = len(self.Update[brand]["metric"])
                for i in range(goalsNum):
                    valueField = self.Update[brand]["metric"][i][1]
                    view = self.Update[brand]["view"]
                    file = f"{view}{valueField}000000000000"
                    df = pd.read_csv(
                        f"C:\\Users\\Santiago\\Documents\\GitHub\\Web_site_goal_final_version\\input\\{file}.csv"
                    )
                    a = int(len(df))
                    if a != 0:
                        df = df.set_axis(
                            [*df.columns[:-1], "Value"], axis=1, inplace=False
                        )
                        df_regex = df[
                            df["campaign_name"].str.match(
                                "(\w.*\/\/\/)((?:\w+\d+\w+))(\s+)"
                            )
                            == True
                        ]
                        df_unregex = df[
                            df["campaign_name"].str.match(
                                "(\w.*\/\/\/)((?:\w+\d+\w+))(\s+)"
                            )
                            == False
                        ]
                        fixed_df = df_regex.replace(
                            to_replace=r"\s{3,3}", value=r"\\\\\\", regex=True
                        )
                        df_final_1 = pd.concat([df_final, fixed_df], ignore_index=True)
                        df_final = pd.concat(
                            [df_final_1, df_unregex], ignore_index=True
                        )
                        df_final = df_final.drop(["view_id"], axis=1)

        return df_final
        # 88420841_Events_01000000000000

        # pattern = re.compile(r'(\w.*\/\/\/)((?:\w+\d+\w+))(\s+)')
        # s.to_csv('C:\\Users\\Santiago\\Documents\\GitHub\\Web_site_goal_final_version\\input\\sumadre.csv')
        # print(s
