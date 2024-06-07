# variables def ----------------------------------------

liquidity = 0
reward_per_week = 0
my_liquidity = 0
reward_per_dollar_day = 0
my_reward_per_day = 0
increase_of_reward = 0
my_first_reward = 0
quotient = 0
a = 0
b = 0
length = 0


# lists def -----------------------------------------------

list_quotient = []
list_my_liquidity = []
list_my_reward_per_day = []

# input ---------------------------------------------------

liquidity = input("\nliquidity_(excluding_my_planned_position)_in_USD: ")
reward_per_week = input("\nrewards_per_week_in_USD: ")
liquidity = int(liquidity)
reward_per_week = int(reward_per_week)


# confirmation input ---------------------------------------

print("\nliquidity_(excluding_my_planned_position): " + str(liquidity) + " USD")
print("\nrewards_per_week : " + str(reward_per_week) + " USD")


# workaround ----------------------------------------------

my_first_reward = (((reward_per_week)/7)/(liquidity+10))*10


# loop reward increase -----------------------------------

for i in range (1, 51):  
    my_liquidity = i*10    
    list_my_liquidity.append(my_liquidity)  
    reward_per_dollar_day = (reward_per_week/7)/(liquidity+my_liquidity)    
    my_reward_per_day = (reward_per_dollar_day*my_liquidity)    
    list_my_reward_per_day.append(my_reward_per_day)
    if i == 1:
        increase_of_reward = my_reward_per_day
    else:
        increase_of_reward = (my_reward_per_day - my_first_reward)    
    
    quotient = (increase_of_reward/i)    
    list_quotient.append(quotient)
    
    

# loop for positionsize decision---------------------------

length = len(list_quotient)
for i in range(length):
    if i > 1 and i <= 48:
        a = list_quotient[i]
        b = list_quotient[i+1]
        if a > b:
            break    

# output positionsize--------------------------------------

print ("\npositionsize: " + str(list_my_liquidity[i]) + " USD\n")        
print ("\nROI per day: " + str(list_my_reward_per_day[i]) + " USD\n") 
print ("\nROI per week: " + str(list_my_reward_per_day[i]*7) + " USD\n")       
print ("\nROI per month: " + str(list_my_reward_per_day[i]*30) + " USD\n")  