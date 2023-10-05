wall = input('')
wall_list = [int(x) for x in wall.split(',')]
water = 0
i=0
n=len(wall_list)
wall_list.append(0)
while i<n:
    temp_water=0
    a=i
    b=i+1
    #从a开始往后探索临界柱子，同时添水
    while wall_list[a]>wall_list[b]:
        #比a低的柱子可以存水
        temp_water+=(wall_list[a]-wall_list[b])
        b+=1
        #如果溢出了还没找到比a高的柱子，除去流出的水
        if b>=len(wall_list):
            temp_water-=((wall_list[a]-wall_list[b-1])*(b-1-a))
            break
    water+=temp_water
    i=b
print(water)