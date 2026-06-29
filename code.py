import random
def spin_row():
    symbols = ["🍉","🍇","🍊","🍋"]

    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print(" | ".join(row))
def get_payout(row,bet):
    if row[0] == row[1]==row[2]:
       if row[0]=="🍉":
          return bet*3
       elif row[0]=="🍇":
          return bet*4
       elif row[0]=="🍊":
          return bet*5
       elif row[0]=="🍋":
          return bet*6
    return 0 
       
def main():
    balance = 1000
    print("welcome to python slot🤗")

    while balance > 0:
       print(f"Current balance {balance}")

       bet = input("Place ur bet amount: ")

       if not bet.isdigit():
        print("please enter valid no.")
        continue

       bet = int(bet)

       if bet > balance:
          print("invalid")
          continue
       
       if bet <=0:
          print("bet must be >0")
          continue
       
       balance -= bet

       row = spin_row()
       print("spinning...")
       print_row(row)

       payout = get_payout(row,bet)

       if payout > 0:
          print(f"uh won {payout}")
       else:
            print("uh lost")
            balance += payout
       playagain = input("want to play again (Y/N)?? ").upper()

    
       if playagain != "Y":
         break
if __name__ == "__main__":
  main()  