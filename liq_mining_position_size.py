# variables def ----------------------------------------

liquidity = 0
reward_woche = 0
meine_liqu = 0
pos_size = 0
reward_pro_dollar_tag = 0
mein_rew_tag = 0
zunahme_rew = 0
mein_erster_rew = 0
quotient = 0
a = 0
b = 0
laenge = 0


# lists def -----------------------------------------------

list_quotient = []
list_meine_liqu = []


# input ---------------------------------------------------

liquidity = input("\nliquidity_(excluding_my_planned_position)_in_USD: ")
reward_woche = input("\nrewards_per_week_in_USD: ")
liquidity = int(liquidity)
reward_woche = int(reward_woche)


# confirmation input ---------------------------------------

print("\nliquidity_(excluding_my_planned_position): " + str(liquidity) + " USD")
print("\nrewards_per_week : " + str(reward_woche) + " USD")


# workaround ----------------------------------------------

mein_erster_rew = (((reward_woche)/7)/(liquidity+10))*10


# loop reward increase ------------------------------------

for i in range (1, 51):  
    meine_liqu = i*10    
    list_meine_liqu.append(meine_liqu)  
    reward_pro_dollar_tag = (reward_woche/7)/(liquidity+meine_liqu)    
    mein_rew_tag = (reward_pro_dollar_tag*meine_liqu)    
    
    if i == 1:
        zunahme_rew = mein_rew_tag
    else:
        zunahme_rew = (mein_rew_tag - mein_erster_rew)    
    
    quotient = (zunahme_rew/i)    
    list_quotient.append(quotient)
    
    

# loop for positionsize decision---------------------------

laenge = len(list_quotient)
for i in range(laenge):
    if i > 1 and i <= 48:
        a = list_quotient[i]
        b = list_quotient[i+1]
        if a > b:
            break    

# output positionsize--------------------------------------

print ("\npositionsize: " + str(list_meine_liqu[i]) + " USD\n")               