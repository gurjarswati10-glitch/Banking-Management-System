from bank import Bank
from saving_account import SavingAccount
from current_account import CurrentAccount
from account import BankAccount

#   ===================================================
#               ||  BANKING MANAGEMENT SYSTEM ||
#   ====================================================

print("="*60)
print("            🏦 SWATI BANKING MANGEMENT SYSTEM")
print("="*60)

bank = Bank()
#-----------------------------------------------
# SAVING ACCOUNT
#-----------------------------------------------

print("\n👤 SAVING ACCOUNT")
print("-"*60)
saving_acc = SavingAccount("Swati Bankey","1736",10000,5)
print("Saving Account Created")
print(saving_acc.get_account_details())

#----------------------------------------------
# CURRENT ACCOUNT
#----------------------------------------------
print("\n👤 CURRENT ACCOUNT")
print("-"*60)
current = CurrentAccount("Om Prakash","1725",50000,5000)
print("\nCurrent Account Created")
print(current.get_account_details())

#---------------------------------------------
# ADD ACCOUNT TO BANK
#---------------------------------------------
print("\n🏦 ACCOUNT ADDED TO BANK SUCCESSFULLY")

bank.add_account(saving_acc)
bank.add_account(current)

#---------------------------------------------
# DEPOSIT
#---------------------------------------------
print("\n 💸DEPOSITE TRANSACTION")
print("-"*60)


saving_acc.deposit(5000)
print("\n ✅Deposit successful")

#------------------------------------
# UPDATE ACCOUNT DETAILS
#------------------------------------

print("\n Updated Saving Account Details:")
print('-'*60)
print(saving_acc.get_account_details())

#-------------------------------------
#WITHDRAW
#-------------------------------------

print("\nWithdraw")
print("-"*60)

saving_acc.withdraw(1000)
print("\n✅ Withdrawal Successful!")

#------------------------------------
# UPDATE ACCOUNT DETAILS
#------------------------------------
print("\n Updated Saving Account Details:")
print("-"*60)
print(saving_acc.get_account_details())


#------------------------------------
#BALANCE
#------------------------------------
print("\n 💹CURRENT Balance")
print("-"*60)
print(saving_acc.get_balance())


#------------------------------------
#INTEREST
#------------------------------------
print("\n📈 INTEREST CALCULATION")
print("-"*60)
print("💰saving account interest",saving_acc.calculate_interest())
print("💰current account interest",current.calculate_interest())

#-------------------------------------
#tRANSACTION HISTORY
#-------------------------------------
print("\n📜Transaction History")
print("-"*60)
saving_acc.show_transaction_history()

#===========================================
#FINAL ACCOUNT DETAILS
#===========================================
print("\n" + "="*60)
print("    ✅ BANKING TRANSACTION COMPLETED     ")
print("="*60)

print("Thank you for using Swati Banking Managment System. Have a great day!")
print("="*60)
#===========================================
#TOTAL ACCOUNTS
#===========================================

print("\n👥 TOTAL ACCOUNTS")
print("-"*60)
print("Total Accounts:", BankAccount.total_accounts())