#day-8
#875. Koko Eating Bananas
'''
import math    #o(n**2)
def koko_bananas(h,a):
    tot_time = 0
    k=0
    while(1):
        k+=1
        tot_time=0
        for i in range(len(a)):
            b_hr = math.ceil(a[i]/k)
            tot_time += b_hr
            if tot_time>h:
                break
            if tot_time == h:
                return k
h=8
arr=[3,6,7,11]
print(koko_bananas(h,arr))
'''



#another question
def can_place_cows_linear(positions, min_dist, cows=2):
    positions.sort()
    count = 1  
    last_pos = positions[0]

    for i in range(1, len(positions)):
        if positions[i] - last_pos >= min_dist:
            count += 1
            last_pos = positions[i]
        if count == cows:
            return True
    return False


positions = [1, 2, 5, 7, 10]
min_distance = 4


if can_place_cows_linear(positions, min_distance):
    print(" possible.")
else:
    print(" not possible.")



    