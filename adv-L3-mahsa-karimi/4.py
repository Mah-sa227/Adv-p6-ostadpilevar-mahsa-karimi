print("Salam be foroshgah fanavari khosh amadid")
product=['atr','skin product','rozh lab','morq sokhari']

while True:
        
        print(product)
        answer=input("aya mahsoli mikhahid?\n")
        answerrr = answer.lower().strip()
    
        if answerrr=='yes' :
                p = input('befarmaeeid  :')
                product.append(p)
                print('ezafe shod :',product)

        elif answerrr=='no':
             print('besiar awli khoda negahdar ... ')
             break
        else:
             print('shoma faqat bayad ba yes/no javab bedi')
            