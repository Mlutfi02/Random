import random
print("***SELAMAT DATANG DAN DI GAME SUIT GUNTING, BATU, KERTAS!!!")
print("PERINGATAN!!!!")
print("ANDA HANYA PUNYA 1X KESEMPATAN!!!")
name = input("your name: ")
choice = input("rock , papper or scissor ? : ")
choices = ["rock","papper","scissor"]
computer = random.choice(choices) 

def choice_checking():
    global choice
    if choice not in choices:
        choice = input("Enter the correct choice : ")

class Player(object):
    def __init__(self, name):
        self.name = name

    def getnama(self):
        return self.name

class RPS(Player):
    def __init__(self, name):
        # Inisialisasi kelas induk."Pewarisan Berorientasi Objek"
        super(self).__init__(name)
        self.p1Input = None  
        self.compInput = None


    def computerChoice(self):self.compInput = print("computer memilih : ", random.choice())  


def play_game():
    choice_checking()
    print("You selected",choice,"and computer selected",computer)
    if choice == computer:
        print("Draw , try again")
    elif choice == "rock" and computer == "scissor":
        print("You Won the match") 
    elif choice == "scissor" and computer == "papper":
        print("You Won the match")
    elif choice == "papper" and computer == "rock":
        print("You Won the match")
        return True
    else:
        print("You Lose and computer won the match , Try again ")
        return False
    

if __name__ == '__main__':
    play_game()