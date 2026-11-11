phoneboook = []
print("Welcome to the 67 phonebook")
while True:
   
    inpuut = int(input("Enter 1 if u want to add a number \n Enter 2 if u want to delete a currently stored number \n Enter 3 if u want to edit a currently stored number \n Enter 4 if u want to view an already stored number\n Enter 5 if u want to exit the phonebook :\t"))
    if (inpuut == 1):
       
        name = input("Enter the name u want to store : ")
        number = int(input("Enter the number u want to save : "))
        record = {
            'Name'  :  name,
            'Number' : number
        }
        phoneboook.append(record)
        print(phoneboook)
        print('\n--------------------------------')
    elif (inpuut == 2):
        if (len(phoneboook) == 0):
           print('You need to add a number before deleting it')
        else:     
            # print(record.items())
            print (phoneboook)
            index = int(input("enter the index of the number u want to delete"))
            del phoneboook[index]
            print (phoneboook)
    elif( inpuut == 3):
        yo = int(input('Enter 1 if u want to change a name\n Enter 2 if u want to change the number : \t '))
        if (yo == 1):
            print(phoneboook)
            index2 = int(input('Enter the index of the name u want to change'))
            name2 = input(' Enter the new name u want to add\t :')
            record.update({'name':name2[index2]})
            print(phoneboook)
           
        elif (yo == 2):
            index3 = int(input('Enter the index of number you want to change:\t'))
            num = int("Enter the new number u want to store\t :")
            record.update({'Number':num[index3]})
            print(phoneboook)
        



    elif (inpuut == 4):
         if (len(phoneboook) == 0):
            print('You need to add a number before viewing it')
         else:
          print('Here is the list of all the numbers u have stored')
          print(phoneboook)
       

  

    elif (inpuut == 5):
         print('Goodbye')
         break
    else:
        print('Invalid input, please try again')
        




        





