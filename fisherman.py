## Mohsen Pourdehghan

import random

randFish= random.randint(250, 800)

print('\n(You): Hello fisherman, how many fish did you catch?')

print(f'\n(Fisherman): Not bad, just {randFish} pound. Do you wanna buy?')

buy= input('\nSay somthing! ("yes" or "no"): ')

while buy !='yes' and buy !='no':
    
    buy= input('\nJUST "yes" or "no": ')


if buy =='yes':

    pound_to_kilo= round(randFish * 0.45,2)
    
    print('\n(You): yes! i want to buy in kilograms.')

    print(f'\n(Fisherman): It can be {pound_to_kilo} kilos. $2 per kilo, how many kilos do you want?')
    
    kilosNeed= int(input(f'\nSay somthing! (from 1 and {pound_to_kilo}): '))

    # When the input is invalid 
    while kilosNeed > pound_to_kilo or kilosNeed < 1 :
        
        kilosNeed= int(input(f'\nBETWEEN 1 AND {pound_to_kilo} !: '))
    
    money= kilosNeed * 2

    #if over $300: gift one rod      
    if money >= 300:
        
        print(f'\n(You): I need {kilosNeed}. here is your money ${money}. and this is your gift! a new fishing rod!!!')
    
        print('\n(Fisherman): Oh, Wow. Thanks!')

    else:
        
        print(f'\n(You): I need {kilosNeed}. here is your money ${money}.')
    
        print('\n(Fisherman): Thanks, enjoy it!')

elif buy =='no' :
    
    print('\n(You): No thanks.')
    
    print('\n(Fisherman): Ok.')


