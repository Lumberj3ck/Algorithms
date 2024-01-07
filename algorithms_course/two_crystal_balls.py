import math 

def two_crystal_balls(breaks: list[bool]) -> int:
    '''
    The problem: we have the list of breaks 
    
    We have two balls need to determine first 
    floor at which it will break using only two balls
    '''
    jump_amount = math.floor(math.sqrt(len(breaks)))

    i = 0

    # using first ball two define area for scaning
    while i < len(breaks):
        i += jump_amount
        if breaks[i]:
            break

    # reset low point to determine are for scaning
    i -= jump_amount

    # scaning this area using second ball
    for i in range(i, i + jump_amount + 1):
        print(i)
        if breaks[i]:
            return i
    return -1





    

