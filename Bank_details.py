
from Validate import *

class Bank:
    def __init__(self, name, mobile_num, bank_name, acc_type, acc_num, ifsc, pan_num, adhar_num, gender, dob, state, city, balance):
        self.name = name
        self.mobile_num = mobile_num
        self.bank_name = bank_name
        self.acc_type = acc_type
        self.acc_num = acc_num
        self.ifsc = ifsc
        self.pan_num = pan_num
        self.adhar_num = adhar_num
        self.gender = gender
        self.dob = dob
        self.state = state
        self.city = city
        #self.area = area
        self.balance = balance
        self.transactions = []

    def display(self):
        print(f"------------------\nAccount Number: ",self.acc_num, f"\nIFSC: ",self.ifsc, f"\nName: ", self.name, f"\nAccount Type: ",self.acc_type, f"\nBalance: ",self.balance)

s1= Bank('Rutika Vasant Harpude', '9021081392', 'ICICI','salary', '1234567890', 'ICIC012345', 'BOFPH2398N', '327813050470', 'female', '28-09-2000', 'Maharashtra', 'Pune', 1000)
s2= Bank('Nupur Vasant Harpude', '1234081392', 'ICICI','saving', '1234567891', 'ICIC012345', 'BOFPH2398A', '327813050471', 'male', '28-09-2005', 'Maharashtra', 'Pune', 0)
s3= Bank('Sakshi Subhash Harpude', '1234081311', 'ICICI','current', '1234567231', 'ICIC012345', 'BOFPH2398A', '327813050471', 'male', '28-09-1999', 'Maharashtra', 'Pune', 0)


cust= []
cust.append(s1)
cust.append(s2)
cust.append(s3)

IFSC_codes = {'Pune': {'Katraj': 'ICIC012345', 'Swargate': 'ICIC012346', 'Hadapsar': 'ICIC012347'}, 'Mumbai': {'Bandra': 'ICIC056780', 'Andheri': 'ICIC056781'}, 'Nashik': 'ICIC054321', 'Nagpur': {'Manewada': 'ICIC001234', 'Wardha Road': 'ICIC001235'}, 'Indore': {'Indore City': 'ICIC013579'}, 'Ujjain': {'Ujjain City': 'ICIC097531'}, 'Gurugram': {'MG Road': 'ICIC086420', 'Palam Vihar': 'ICIC086421'}, 'Panipat': {'Faridpur': 'ICIC024680', 'Model Town': 'ICIC024681'}}
while True:
    print(f"\n----------WELCOME TO ICICI BANK!!------------------------")
    print("\nPress 1: Customer")
    print("Press 2: Administrator")
    print("Press 3. To exit\n")

    ch = int(input("Enter your Choice : "))
    if ch == 1:

        while True:
            print(f"\n----------WELCOME TO ICICI BANK!!------------------------")
            print("What can we do for you : ")
            print("1. Create an Account")
            print("2. Delete Account")
            print("3. Update account Details")
            #print("4. Search for Bank Account")
            print("5. Deposit ")
            print("6. Withdraw ")
            print("7. Display Account Details")
            print("8. Check Balance")
            print("9. Fund Transfer")
            print("10. Bank Statement ")
            print(f"11. Exit\n-------------------------------------------")
            ch = int(input("Enter your choice : "))

            if ch == 1:
                while True:
                    name = input(f"\nEnter your Name[FirstName MiddleName LastName]: ")
                    if(validName(name)):
                        print("Name inserted")
                        break
                    else:
                        print("Enter name in valid format")

                while True:
                    num = input(f"\nEnter your Mobile number: ")
                    if(validNumber(num)):
                        print("Mobile Number Inserted")
                        break
                    else:
                        print("Enter valid Number")

                while True:
                    adhar = input(f"\nEnter your Adhar Number : ")
                    if(validAdhar(adhar)):
                        print("Adhar Number Inserted")
                        break
                    else:
                        print("Enter valid Adhar Number")

                while True:
                    pan = input(f"\nEnter your PAN Number : ")
                    if(validPan(pan)):
                        print("PAN Number Inserted")
                        break
                    else:
                        print("Enter valid PAN Number")

                while True:
                    state = input(f"\nEnter your state: ")
                    if(validState(state)):
                        print("Sate Inserted")
                        break
                    else:
                        print("Enter valid state")

                while True:
                    city = input(f"\nEnter your city: ")
                    if(validCity(state, city)):
                        print("City Inserted")
                        break
                    else:
                        print("Enter valid city")


                while True:
                    dob = input(f"\nEnter Your Date Of Birth[dd-mm-yyyy] :")
                    if(validDOB(dob)):
                        print("DOB inserted")
                        break
                    else:
                        print("Enter valid birth date")

                while True:
                    gender= input(f"\nGender : ")
                    if(validGender(gender)):
                        print("Gender Inserted")
                        break
                    else:
                        print("Enter valid Gender")

                while True:
                    acc_type = input(f"\nEnter account type you want to create :")
                    if(validAccountType(acc_type)):
                        print("Account type Inserted")
                        break
                    else:
                        print("Enter valid Account type")

                import random
                random_number = random.randint(1000000000, 9999999999)
                random_number = str(random_number)
                if(validAccountNumber(random_number)):
                    acc_num = random_number

                balance =0
                age1 = age(dob)
                b_name = 'ICICI'

                #IFSC_codes = {'Pune': {'Katraj': 'ICIC012345', 'Swargate': 'ICIC012346', 'Hadapsar': 'ICIC012347'}, 'Mumbai': {'Bandra': 'ICIC056780', 'Andheri': 'ICIC056781'}, 'Nashik': 'ICIC054321', 'Nagpur': {'Manewada': 'ICIC001234', 'Wardha Road': 'ICIC001235'}, 'Indore': {'Indore City': 'ICIC013579'}, 'Ujjain': {'Ujjain City': 'ICIC097531'}, 'Gurugram': {'MG Road': 'ICIC086420', 'Palam Vihar': 'ICIC086421'}, 'Panipat': {'Faridpur': 'ICIC024680', 'Model Town': 'ICIC024681'}}
                for k in IFSC_codes.keys():
                    if city.title() == k:
                        area = input(f"Select the branch: {IFSC_codes[k].keys()} : ")
                        ifsc = IFSC_codes[k][area.title()]


                b1 = Bank(name.title(), num, b_name, acc_type, acc_num, ifsc, pan, adhar, gender.title(), dob, state.title(), city.title(), balance)
                cust.append(b1)

                print(f"\nAccount Created Successfully !")
                print(f"----------------------\nYour Account Number : ", b1.acc_num, "\nYour IFSC code : ", b1.ifsc, "\n-----------------------")

            elif ch == 2:
                n = input(f"\nEnter the account Number to delete :")
                flag = False
                for i in cust:
                    if i.acc_num == n:
                        flag = True
                        cust.remove(i)
                        print("Account Deleted ")
                if flag == False:
                    print("Enter valid Account Number")

            elif ch == 3:
                p = input(f"\nEnter the Account Number to update :")
                flag = False

                for i in cust:
                    if i.acc_num == p:
                        flag = True
                        print(f"\nPress 1 to update name")
                        print(f"Press 2 to update mobile number\n")

                        ch = int(input("Enter your choice :"))
                        if ch == 1:
                            nm = input(f"\nEnter the updated Name :")
                            if(validName(nm)):
                                i.name = nm
                                print("Name updated")
                            else:
                                print("Invalid Name, insert in proper format")

                        if ch == 2:
                            num = input(f"\nEnter the updated Number :")
                            if (validNumber(num)):
                                i.mobile_num = num
                                print("Number updated")
                            else:
                                print("Invalid Number, insert in proper format")

                if flag == False:
                    print("Enter valid Account Number")

            elif ch == 4:
                print(f"\nPress 1 to search by account number : ")
                print(f"Press 2 to search by Name : \n")

                ch = int(input("Enter your choice: "))
                if ch == 1:
                    num = input("Enter the account Number : ")
                    flag = False
                    for i in cust:
                        if i.acc_num == num:
                            flag = True
                            print(f"Record found\n--------------------")
                            i.display()

                    if flag == False:
                        print("Record Not found")

                if ch == 2:
                    nm = input("Enter the name : ")
                    flag = False
                    for i in cust:
                        if i.name == nm:
                            flag = True
                            print(f"Record Found\n-------------------")
                            i.display()

                    if flag == False:
                        print("Record Not found")

            elif ch == 5:
                n = input(f"\nEnter your account number : ")
                flag = False
                for i in cust:
                    if i.acc_num == n:
                        flag = True
                        amt = int(input("Enter the amount you want to deposit :"))
                        i.balance +=amt
                        print("Amount Deposited Successfully!")
                        print("Your current balance :", i.balance)
                        str1 = f"{datetime.now()}    Deposit        balance: {i.balance}"
                        i.transactions.append(str1)
                if flag == False:
                    print("Invalid Account Number")


            elif ch == 6:
                n = input(f"\nEnter your account number : ")
                flag = False
                for i in cust:
                    if i.acc_num == n:
                        flag = True
                        amt = int(input("Enter the amount you want to withdraw :"))
                        if i.balance >= amt:
                            i.balance -= amt
                            print("Amount withdrawal Sucessfull !")
                            print("Your current balance :", i.balance)
                            str1 = f"{datetime.now()}    Withdraw       balance: {i.balance}"
                            i.transactions.append(str1)
                        else:
                            print("You donot have enough balance to withdraw")
                if flag == False:
                    print("Invalid Account Number")

            elif ch == 7:
                n = input(f"Enter the account Number to display details :")
                flag = False
                for i in cust:
                    if i.acc_num == n:
                        flag = True
                        i.display()
                if flag == False:
                    print("Enter valid Account Number")



            elif ch == 8:
                n = input("Enter your Account Number : ")
                flag = False
                for i in cust:
                    if i.acc_num ==n:
                        flag = True
                        print("Available Balance : ",i.balance)

                if flag == False:
                    print("Enter valid Account Number")

            elif ch == 9:
                n1 = input("Enter you account Number :")
                n2 = input("Enter the account Number you want to transact money to : ")
                amt = int(input("Enter the amount you want to transfer : "))
                flag = False
                for i in cust:
                    if i.acc_num == n1:
                        flag = True
                        if amt <= i.balance:
                            i.balance -= amt
                            print("Transaction SuccessFull")
                            print("Your current balance :", i.balance)
                            str1 = f"{datetime.now()}   Fund Transfer   balance: {i.balance}"
                            i.transactions.append(str1)

                            for j in cust:
                                if j.acc_num == n2:
                                    j.balance += amt
                                    str2 = f"{datetime.now()}   Fund Transfer   balance: {j.balance}"
                                    j.transactions.append(str2)
                                    break
                        else:
                            print("you do not enough balance to carry the transaction")

                if flag == False:
                    print("Enter valid account Number")

            elif ch == 10:
                n = input("Enter your Account Number : ")
                for i in cust:
                    if i.acc_num == n:
                        for k in i.transactions:
                            print(k, sep="\n")
                        break

            elif ch == 11:
                break

            else:
                print("Enter valid choice")

    if ch == 2:
        while True:
            print(f"\n----------WELCOME TO ICICI BANK!!------------------------")
            print("What can we do for you : \n")
            print("1. Search for Bank Account")
            print("2. Display Account Details")
            print("3. Number of Customers in Particular City")
            print("4. Number of Customers in Particular branch")
            print("5. Number of customers having a particular type of bank account: ")
            print("6. Exit\n")

            ch = int(input("Enter the choice : "))
            if ch == 1:
                print(f"\nPress 1 to search by account number : ")
                print(f"Press 2 to search by Name : \n")

                ch = int(input("Enter your choice: "))
                if ch == 1:
                    num = input("Enter the account Number : ")
                    flag = False
                    for i in cust:
                        if i.acc_num == num:
                            flag = True
                            print(f"Record found\n--------------------")
                            i.display()

                    if flag == False:
                        print("Record Not found")

                elif ch == 2:
                    nm = input("Enter the name : ")
                    flag = False
                    for i in cust:
                        if i.name == nm:
                            flag = True
                            print(f"Record Found\n-------------------")
                            i.display()

                    if flag == False:
                        print("Record Not found")

            elif ch == 2:
                n = input(f"Enter the account Number to display details :")
                flag = False
                for i in cust:
                    if i.acc_num == n:
                        flag = True
                        i.display()
                if flag == False:
                    print("Enter valid Account Number\n")


            elif ch == 3:
                city = input(("Enter the city : "))
                cnt = 0
                flag = False
                for k in IFSC_codes.keys():
                    if k == city.title():
                        flag = True
                        for i in cust:
                            if i.city == city.title():
                                cnt += 1

                if flag == False:
                    print("Enter valid City")
                else:
                    print(f"Number of customers in {city} city: {cnt}\n")

            elif ch == 4:
                area = input("Enter the IFSC: ")
                cnt = 0
                flag1 = False

                for city, branches in IFSC_codes.items():
                    if isinstance(branches, dict):
                        for branch, ifsc in branches.items():
                            if ifsc == area:
                                flag1 = True
                                for i in cust:
                                    if i.ifsc == area:
                                        cnt+= 1

                '''
                for city, branches in IFSC_codes.items():
                    if isinstance(branches, dict):
                        for branch, ifsc in branches.items():
                            if ifsc == area:
                                cnt += 1
                '''


                if flag1 == False:
                    print("Enter valid IFSC code")
                else:
                    print(f"Number of Customers in {area}: {cnt}\n")

            elif ch == 5:
                type1 = input("Enter the account type : ")
                cnt = 0
                for i in cust:
                    if i.acc_type.lower() == type1.lower():
                        cnt += 1

                print(f"\nThe total Number of Customers with {type} account : {cnt}")

            elif ch == 6:
                break

            else:
                print("Enter valid choice1")

    elif ch == 3:
        break

    else:
        print("Enter valid Choice2")













