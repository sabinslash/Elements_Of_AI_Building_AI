def bot8(pbot, p8_bot, p8_human):
    # Calculate the probability of a new follower having an 8-digit username
    p8 = p8_bot * pbot + p8_human * (1 - pbot)
    
    # Calculate the probability of the new follower being a bot given they have an 8-digit username
    pbot_8 = p8_bot * pbot / p8
    
    print(pbot_8)

# you can change these values to test your program with different values
pbot = 0.1
p8_bot = 0.8
p8_human = 0.05

bot8(pbot, p8_bot, p8_human)
