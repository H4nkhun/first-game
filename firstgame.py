#this's Phoomjai's python learning
import random
# random a number as num
num = random.randint(1,100)
print(num)
attemps = 0
while True:
  attemps += 1
  if attemps >= 8:
    print('reach max attemps')
    break
  player=int(input("your guesses:"))
  if player != num:
    if player > num:
      print("lower")
    if player < num:
      print("higher")
    print(f"you have {7-attemps} attemps left")
  else:
    print("you guess it your total Attemp:",attemps)
    break
print("lets play anothor game")
yes_or_no = input("Do you want to play a game? (yes/no): ")
if yes_or_no == "no":
  print("ok thanks at least")
elif yes_or_no == "yes":
  print("ok lets play")
