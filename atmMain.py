import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Green2!73!7B27',database='bank_management')
import random

def openAcc():
    n=input("Enter your Name: ")
    def generateAccountNumber():
        return random.randrange(1111111111,9999999999)
    ac=generateAccountNumber()
    db=input("Enter your date of birthh: ")
    add=input("Enter your address: ")
    cn=input("Enter the contact number: ")
    ob=int(input("Enter your opening balance: "))
    data1=(n,ac,db,add,cn,ob)
    data2=(n,ac,ob)
    sql1=('insert into account va2lues (%s,%s,%s,%s,%s,%s)')
    sql2=('insert into amount values (%s,%s,%s)')
    x=mydb.cursor()
    x.execute(sql1,data1)
    x.execute(sql2,data2)
    mydb.commit()
    print("Your account has been created.")
    print("== === ===== ===== ===")
    print("Your account number is: %d" % ac)
    print("make sure you keep it safe")
    print("== === ===== ===== ===")
    restart=input('Do you want to return to the main menu?')
    if restart=='yes':
        main()
    else:
        print('Thank you for banking with Bank PHP. Have a blessed day.')
        exit()
    

def deposAmo():
    amount=int(input("Enter the amount you want to deposit:  "))
    ac=input("Enter the Account number:  ")
    a="select Balance from amount where AccNo=%s"
    data=(ac,)
    x=mydb.cursor()
    x.execute(a,data)
    result=x.fetchone()
    t=result[0]+amount
    sql=("update amount set Balance=%s where AccNo=%s")
    d=(t,ac)
    x.execute(sql,d)
    mydb.commit()
    print('Your new balance is %d.'  %t)
    restart=input('Do you want to return to the main menu?')
    if restart=='yes':
        main()
    else:
        print('Thank you for banking with Bank PHP.  Have a blessed day.')
        exit()

def wdrawAmo():
    amount=int(input("Enter the amount you want to withdraw:  "))
    ac=input("Enter the Account number:  ")
    a="select Balance from amount where AccNo=%s"
    data=(ac,)
    x=mydb.cursor()
    x.execute(a,data)
    result=x.fetchone()
    t=result[0]-amount
    sql=("update amount set Balance=%s where AccNo=%s")
    d=(t,ac)
    x.execute(sql,d)
    mydb.commit()
    print('Your new balance is %d.' %t)
    restart=input('Do you want to return to the main menu?')
    if restart=='yes':
        main()
    else:
        print('''Thank you for banking with Bank PHP.
                 Have a blessed day.''')
        exit()

def balanceInq():
    ac=input("Enter the account number:  ")
    a='select * from amount where AccNo=%s'
    data=(ac,)
    x=mydb.cursor()
    x.execute(a,data)
    result=x.fetchone()
    print("Your balance for account:",ac,"is",result[-1])
    restart=input('Do you want to return to the main menu?')
    if restart=='yes':
        main()
    else:
        print('Thank you for banking with Bank PHP.  Have a blessed day.')
        exit()

def custDet():
    ac=input("Enter the account number:  ")
    a='select * from amount where AccNo=%s'
    data=(ac,)
    x=mydb.cursor()
    x.execute(a,data)
    result=x.fetchone()
    for i in result:
        print(i)
    restart=input('Do you want to return to the main menu?')
    if restart=='yes':
        main()
    else:
        print('Thank you for banking with Bank PHP.  Have a blessed day.')
        exit()

def closeAcc():
    ac=input("Enter the account number:  ")
    sql1='delete from account where AccNo=%s'
    sql2='delete from account where AccNo=%s'
    data(ac,)
    x=mydb.cursor()
    x.execute(sql1,data)
    x.execute(sql2,data)
    mydb.commit()
    restart=input('Do you want to return to the main menu?')
    if restart=='yes':
        main()
    else:
        print('Thank you for banking with Bank PHP.  Have a blessed day.')
        exit()



def main():
    print('''
                1. OPEN NEW ACCOUNT
                2. DEPOSIT AMOUNT
                3. WITHDRAW AMOUNT
                4. BALANCE INQUIRY
                5. DISPLAY CUSTOMER DETAILS
                6. CLOSE THE ACCOUNT''')
    choice =input("Enter your task:")
    if(choice=='1'):
        openAcc()
    elif(choice=='2'):
        deposAmo()
    elif(choice=='3'):
        wdrawAmo()
    elif(choice=='4'):
        balanceInq()
    elif(choice=='5'):
        custDet()
    elif(choice=='6'):
        closeAcc()
    else:
        print("Invalid Choice")
    
main()
