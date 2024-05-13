first = 121
second = 20

def pal_num(x):
    ax = abs(x)
    num_list = [int(i) for i in str(ax)]

    num_listreverse = num_list[::-1]

    if num_listreverse == num_list:
        
        return True
    else: 
        return False

#pal_num(first)
print(pal_num(first))

