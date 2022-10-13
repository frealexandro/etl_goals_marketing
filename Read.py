from ast import pattern
import csv
import re
import pandas as pd 


class Read:

    def __init__(self,file_p):
        
      self.file_p = file_p

    def read_fle(self):

      #pattern = re.compile(r'(\w.*\/\/\/)((?:\w+\d+\w+))(\s+)')

      df = pd.read_csv(self.file_p)
      df = df[df['campaign_name'].str.match('(\w.*\/\/\/)((?:\w+\d+\w+))(\s+)')== True]
      s = df.replace(to_replace=r"\s{3,3}", value=r"\\\\\\", regex=True)
      s.to_csv('C:\\Users\\Santiago\\Documents\\GitHub\\Web_site_goal_final_version\\input\\sumadre.csv')
      print(s)
      #with open( self.file_p , 'r') as file:
        
        #for line in file:
          #res = re.findall(pattern, line)
          #for i in res:
            #print(i)
            #re.sub("\s{3,3}" , "\\\\\\\\\\\\" , i)

          #if res:
            #f = (str(f"{res.group(3)}\n"))
            #re.sub("\s{3,3}" , "\\\\\\\\\\\\" , res)
            #print (res)

        
        
        #return csvreader
        #for row in csvreader:
          #print(row)