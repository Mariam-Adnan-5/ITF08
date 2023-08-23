import datetime
clients=[]
class Transaction:
   def __init__(self,amount,type):
      self.amount=amount
      self.date=str(datetime.datetime.now())
      self.type=type
   def get_transaction(self):
      print(f"{self.amount}\t|{self.date}\t|{self.type}")


class BankAccount:
   count=0
   def __init__(self,national_id,client_name):
      self.national_id=national_id
      self.client_name=client_name
      self.balance=0
      self.transaction=[]
      self.id=BankAccount.count
      BankAccount.count+=1
   def wihtdraw(self,amount):
     if amount>self.balance or amount<=0:
       print("Invailed Amount")
     else:
      self.balance-=amount
      transaction=Transaction(amount,"wihtdraw")
      self.transaction.append(transaction)
      print("wihtdraw Done Succesful")
   def deposit(self,amount):
      if amount<=0:
         print("Invailed Amount")
      else:
       self.balance += amount
       transaction = Transaction(amount, "deposit")
       self.transaction.append(transaction)
       print("Deposit Done Succesful")
   def print_transaction_history(self):
      print("Amount\t|Date\t|Type")
      for i in self.transaction:
        i.get_transaction()
        print("----------------------------------")
      print(f"Total balance={self.balance}")
while True:
 choice=int(input("""1-Open new account\n2-Deposit of your account \n3-Wihtdraw of your account
 4-print transaction history\n5-Exit\n Enter your choice"""))
 while True:

  if choice==1:
    name=input("Enter your account name")
    national_id=int(input("Enter your national_id"))
    bankAccount=BankAccount(national_id,name)
    clients.append(bankAccount)
    break
  elif choice==2:
    cheak_national_id=int(input("Enter your national_id"))
    for i in clients:
        if cheak_national_id == i.national_id:
            depo=int(input("Enter your amount"))
            i.deposit(depo)
        else:
          print("Invalid national_id")
    break


  elif choice==3:
    cheak_national_id =int( input("Enter your national_id"))
    for i in clients:
        if cheak_national_id==i.national_id:
            with_draw=int(input("Enter your amount"))
            i.wihtdraw(with_draw)
        else:
          print("Invalid national_id")
    break



  elif choice==4 :
    cheak_national_id =int( input("Enter your national_id"))
    for i in clients:
        if cheak_national_id == i.national_id:
           i.print_transaction_history()
        else:
          print("Invalid national_id")
    break



  elif choice == 5:
      exit()
  else:
      print("Invalid input")
      break

