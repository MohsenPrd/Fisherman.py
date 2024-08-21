## Mohsen Pourdehghan

import datetime
import random



randFish= random.randint(300, 1000)

print('\n(You): Hello fisherman, how many fish did you catch?')

print(f'\n(Fisherman): Not bad, just {randFish} pound. Do you wanna buy?')


buy= input('\nSay somthing! ("yes" or "no"): ')


while buy !='yes' and buy !='no':
    
    buy= input('\nJUST "yes" or "no": ')




if buy =='yes':

    pound_to_kilo= round(randFish * 0.45,2)
    
    print('\n(You): yes!')

    print(f'\n(Fisherman): $5 per pound, how many pound do you want?')
    
    poundNeed= int(input(f'\nSay somthing! (from 1 and {randFish}): '))


    # When the input is invalid 

    while poundNeed > randFish or poundNeed < 1 :
        
        poundNeed= int(input(f'\nBETWEEN 1 AND {randFish} !: '))
    
    money = poundNeed * 5
    is_doubled = False;

    
    #if over $1000: money 2x      

    if money >= 1000:

        money = money * 2
        is_doubled = True

        print(f'\n(You): I need {poundNeed}.')
    
        print(f'\n(Fisherman): its {pound_to_kilo} kilos and ${money} (doubled!).')

        print(f'\n(You): here is your money ${money}.')

        print('\n(Fisherman): Oh, Wow. Thanks!\n')

    else:
        
        print(f'\n(You): I need {poundNeed}.')
    
        print(f'\n(Fisherman): its {pound_to_kilo} kilos and ${money}.')

        print(f'\n(You): here is your money ${money}.')

        print('\n(Fisherman): Thanks, enjoy it!\n')


elif buy =='no' :
    
    print('\n(You): No thanks.')
    
    print('\n(Fisherman): Ok.')




# Save results to file
file = open('Fisherman.py/results.txt', 'a')

file.write(f'''

=== Results at {datetime.datetime.now()} ===

fisherman total pound = {randFish}

user pound need: {poundNeed}

total pay : ${money}

is_doubled : {is_doubled}

---------------------------------------

           ''')