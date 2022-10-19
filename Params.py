"""This code content all params in the project"""

class params:

    def __init__(self):
    
        self.regex = '(\w.*\/\/\/)((?:\w+\d+\w+))(\s+)'
        


        


        self.Website_Goals_Supermetrics_Update={
        'Applications':{
        'update':True,
        'metric' : [
            
            #['Como se llama en la API', 'Como cae el cae en la consulta', 'Como se va a llenar el campo en el export']
            
            ['goal1completions','_goal_01','1 - Cash rewards'],
            ['goal3completions','_goal_03','3 - AAdvantage Signature PR'],
            ['goal4completions','_goal_04','4 - Jetblue Mastercard'],
            ['goal7completions','_goal_07','7 - Jetblue Mastercard Eleva'],
            # ['goal12completions','Goal 12 completions','12-Completed Loan Form'],
            ['goal20completions','_goal_20','20 - Lead Negocios - Contact Form'],
        ],
        'profile':'%5B%7B%22ID%22%3A%2295557079%22%2C%22name%22%3A%22Popular.com%3A%20Popular%20-%20Portlike%20-%20MultiDomain%20-%20Applications%22%7D%5D',
        'view':'95557079',
        'viewName':'Applications'
        
        },
        'Leads':{
        'update':True,
        'metric' : [
            #['Como se llama en la API', 'Como cae el cae en la consulta', 'Como se va a llenar el campo en el export']
            ['goal5completions','_goal_05','5 - Popular Auto - New Lead Generator'],
            ['goal16completions','_goal_16','16 - Risk Service Lead'],
            ['goal8completions','_goal_08','8 - Funnel Hipotecas Refinanciar'],
        ],
        'profile':'%5B%7B%22ID%22%3A%2296577637%22%2C%22name%22%3A%22Popular.com%3A%20Popular%20-%20Portlike%20-%20MultiDomain%20-%20Leads%22%7D%5D',
        'view':'96577637',
        'viewName':'Leads'
    },
    'Leads 2':{
        'update':True,
        'metric' : [
            #['Como se llama en la API', 'Como cae el cae en la consulta', 'Como se va a llenar el campo en el export']
            ['goal2completions','_goal_02','2 - PromoTarjetasPopular'],
            ['goal8completions','_goal_08','8 - popularautoprcom'],
            ['goal9completions','_goal_09','9 - Lead Insurance Care4Cancer'],
            ['goal10completions','_goal_10','10 - Form Downloads'],
            ['goal4completions','_goal_04','4 - Sorteo AAdvantage Toscana'],
            # ['goal20completions','Goal 20 completions','20-Starting Connection - Popular Auto'],
        ],
        'profile':'%5B%7B%22ID%22%3A%22116580388%22%2C%22name%22%3A%22Popular.com%3A%20Popular%20-%20Portlike%20-%20MultiDomain%20-%20Leads%202%22%7D%5D',
        'view':'116580388',
        'viewName':'Leads 2'
    },
    'DeShow.com':{
        'update':True,
        'metric' : [
            #['Como se llama en la API', 'Como cae el cae en la consulta', 'Como se va a llenar el campo en el export']
            ['goal1completions','_goal_01','1 - Contact Us Form'],
            ['goal2completions','_goal_02','2 - Property Lead Form'],
        ],
        'profile':'%5B%7B%22ID%22%3A%22103885104%22%2C%22name%22%3A%22DeShow.com%3A%20All%20Web%20Site%20Data%22%7D%5D',
        'view':'103885104',
        'viewName':'DeShow.com'
    },
    'Popular VI':{
        'update':True,
        'metric' : [
            #['Como se llama en la API', 'Como cae el cae en la consulta', 'Como se va a llenar el campo en el export']
            ['goal7completions','_goal_07','7-Popular VI Startup'],
        ],
        'profile':'%5B%7B%22ID%22%3A%2288420841%22%2C%22name%22%3A%22Popular.com%3A%20Popular.vi%22%7D%5D',
        'view':'88420841',
        'viewName':'Popular VI'
    },
}
