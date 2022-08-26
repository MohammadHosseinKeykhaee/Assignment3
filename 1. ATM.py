#password_card
password_card = 1994
#reverse_code
reverse_code= 4991
#ATM code
ATM = int(input("please enter your password:"))
if ATM == password_card:
   print("welcome ** Banking operations: 1.cash withdrawal 2. money transfer  3. account balance  4. Changing the password " ) 
elif ATM == reverse_code:
    print(" Warning !!!! Alarm !!!!!!! Phone number : 110/// A report was sent to the police ")
### part2 ####
for i in range(3):
    ATM = int(input("please enter your password:"))
    if ATM == password_card:
        print("welcome ** Banking operations: 1.cash withdrawal 2. money transfer  3. account balance  4. Changing the password " ) 
        break
    elif  9999<= password_card<= 10000 :    # test 4 digit
        print ("the password must be 4 digits...try again please")
    elif ATM == reverse_code:
         print(" Warning !!!! Alarm !!!!!!! Phone number : 110/// A report was sent to the police ")
    else:
        print("wrong password...try again")
    continue
else:
       print('the card locked')