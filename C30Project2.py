import random

class Game:
    def __init__(self):
        self.MAX_ATTEMPTS = 10
        self.og_number = random.randint(1, 100)
        self.attempts = 0

    def play(self):
        print("Welcome to Guess the Number game!")
        print("Enter a number between 1 and 100.")

        while self.attempts < self.MAX_ATTEMPTS:
            print("Attempts left:", self.MAX_ATTEMPTS - self.attempts)
            user_input = self.get_user_input()

            if user_input == self.og_number:
                print(f"*****************Congratulations! You guessed the number ({self.og_number}) in {self.attempts + 1} attempts.**************")
                self.highScore()
                break
            elif user_input < self.og_number:
                print("Try a higher number.")
            else:
                print("Try a lower number.")

            self.attempts += 1

        if self.attempts >= self.MAX_ATTEMPTS:
            print("You have used all your attempts. The correct number was:", self.og_number)
        print("End of the game.")

    def get_user_input(self):
        while True:
            try:
                user_input = int(input("Enter your guess: "))
                if 1 <= user_input <= 100:
                    return user_input
                else:
                    print("Please enter a number between 1 and 100.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    def highScore(self):
        with open("highScoreForGuessGame.txt") as f:
            self.highScore= int(f.read())
        if self.attempts<self.highScore:
            with open("highScoreForGuessGame.txt","w") as f:
                f.write(str(self.attempts+1))
        
class RankingSystem:
    def __init__(self, attempts):
        self.attempts = attempts

    def get_grade(self):
        if self.attempts <= 2:
            return 'A'
        elif self.attempts <= 5:
            return 'B'
        elif self.attempts <= 8:
            return 'C'
        else:
            return 'D'


def main():
    game = Game()
    game.play()
    
    ranking = RankingSystem(game.attempts)
    print("Your grade:", ranking.get_grade())

# if __name__ == "__main__":
#     main()