"""This code content all params in the project"""

class params:

    def __init__(self):
    
        self.regex = '(\w.*\/\/\/)((?:\w+\d+\w+))(\s+)'
        
        self.pth_fl = "C:\\Users\\Santiago\\Documents\\GitHub\\Web_site_goal_final_version\\input\\Goal_ 1 - Cash rewards.csv"

        self.Website_Goals_Supermetrics_Update={
        'Applications':{
        'update':True,
        'metric' : [
            
            #['Como se llama en la API', 'Como cae el cae en la consulta', 'Como se va a llenar el campo en el export']
            
            ['goal1completions','Goal 1 completions','1 - Cash rewards'],
            ['goal3completions','Goal 3 completions','3 - AAdvantage Signature PR'],
            ['goal4completions','Goal 4 completions','4 - Jetblue Mastercard'],
            ['goal7completions','Goal 7 completions','7 - Jetblue Mastercard Eleva'],
            # ['goal12completions','Goal 12 completions','12-Completed Loan Form'],
            ['goal20completions','Goal 20 completions','20 - Lead Negocios - Contact Form'],
        ],
        'profile':'%5B%7B%22ID%22%3A%2295557079%22%2C%22name%22%3A%22Popular.com%3A%20Popular%20-%20Portlike%20-%20MultiDomain%20-%20Applications%22%7D%5D',
        'view':'95557079',
        'viewName':'Applications'
        },
        'Leads':{
        'update':True,
        'metric' : [
            #['Como se llama en la API', 'Como cae el cae en la consulta', 'Como se va a llenar el campo en el export']
            ['goal5completions','Goal 5 completions','5 - Popular Auto - New Lead Generator'],
            ['goal16completions','Goal 16 completions','16 - Risk Service Lead'],
            ['goal8completions','Goal 8 completions','8 - Funnel Hipotecas Refinanciar'],
        ],
        'profile':'%5B%7B%22ID%22%3A%2296577637%22%2C%22name%22%3A%22Popular.com%3A%20Popular%20-%20Portlike%20-%20MultiDomain%20-%20Leads%22%7D%5D',
        'view':'96577637',
        'viewName':'Leads'
    },
    'Leads 2':{
        'update':True,
        'metric' : [
            #['Como se llama en la API', 'Como cae el cae en la consulta', 'Como se va a llenar el campo en el export']
            ['goal2completions','Goal 2 completions','2 - PromoTarjetasPopular'],
            ['goal8completions','Goal 8 completions','8 - popularautoprcom'],
            ['goal9completions','Goal 9 completions','9 - Lead Insurance Care4Cancer'],
            ['goal10completions','Goal 10 completions','10 - Form Downloads'],
            ['goal4completions','Goal 4 completions','4 - Sorteo AAdvantage Toscana'],
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
            ['goal1completions','Goal 1 completions','1 - Contact Us Form'],
            ['goal2completions','Goal 2 completions','2 - Property Lead Form'],
        ],
        'profile':'%5B%7B%22ID%22%3A%22103885104%22%2C%22name%22%3A%22DeShow.com%3A%20All%20Web%20Site%20Data%22%7D%5D',
        'view':'103885104',
        'viewName':'DeShow.com'
    },
    'Popular Auto PR':{
        'update':True,
        'metric' : [
            #['Como se llama en la API', 'Como cae el cae en la consulta', 'Como se va a llenar el campo en el export']
            ['goal1completions','Goal 1 completions','01-Popular Auto PR'],
        ],
        'profile':'%5B%7B%22ID%22%3A%22216745898%22%2C%22name%22%3A%22Popular.com%3A%20Popular%20Auto%20PR%22%7D%5D',
        'view':'216745898',
        'viewName':'Popular Auto PR'
    },
    'Popular VI':{
        'update':True,
        'metric' : [
            #['Como se llama en la API', 'Como cae el cae en la consulta', 'Como se va a llenar el campo en el export']
            ['goal7completions','Goal 7 completions','07-Popular VI Startup'],
        ],
        'profile':'%5B%7B%22ID%22%3A%2288420841%22%2C%22name%22%3A%22Popular.com%3A%20Popular.vi%22%7D%5D',
        'view':'88420841',
        'viewName':'Popular VI'
    },
}