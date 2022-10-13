from Params import *
from Read import *
from Fix_goals import *




def run():
    #call params 
    params_m = params()
    
    ######read the file 
    
    #read_m = Read(params_m.pth_fl)
    
    #file_m = read_m.read_fle()
    
    Update = params_m.Website_Goals_Supermetrics_Update
    
    for brand in Update:
        if Update[brand]['update']:
            goalsNum = len(Update[brand]['metric'])
            for i in range(goalsNum):
                print(f"{brand}")
                metric = Update[brand]['metric'][i][0]
                valueField = Update[brand]['metric'][i][1]
                goalName = Update[brand]['metric'][i][2]
                view = Update [brand]['view']
                print(f'{view}')                
                print(f"{goalName}")
                print(f'{valueField}')
                
                print(f'{metric}')

                profile = Update[brand]['profile']
                #print(profile)
    
    
    #extract and fix goals with problems

    #fix_maingl = Fix_Goals(file_m, params_m.regex)
    
    #match_m = fix_maingl.match_goals()
    





if __name__=="__main__":
    run()