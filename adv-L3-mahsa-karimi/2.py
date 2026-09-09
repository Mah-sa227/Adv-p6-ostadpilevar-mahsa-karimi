zoj_list = []
count = 0


print('fard beyne 30_50 =')

for i in range(30,51):
   
    if i%2 == 1:
         print(i , end=',')
   
        
for i in range(30,7001):
        
        if i%2 == 1 :
            count +=1
print('\ncount even between 30-7000 is :', count)           


for i in range(60,121):
        
        if i%2 == 0:
           zoj_list.append(i)
          
             
print('\nzoj_list = ',zoj_list)            