password = input('enter password : \n')

if len(password)>=8:
    
          if any(i.isdigit() for i in password ):
              if not password.isalpha():
                  if not password.islower():
                      if not password.isupper():
                             print('با موفقیت ثبت شد...')
                      else:
                          print('upper nadare ')
                  else:
                      print('lower nadare ')
              else:
                  print('alphabet nadare')
          else:
              print('number nadare')

else:
    raise TypeError('کوچکتر از 8 کاراکتز مجاز نیست')
