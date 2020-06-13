import random

print("H A N G M A N\n")

def ask_the_player():
    mode = input('Type "play" to play the game, "exit" to quit: ')
    if mode == "play":
        word_list = ('герб', 'подсолнух', 'ружье', 'берлога', 'плюшка', 'одноклассник',
                     'веревка', 'забор', 'яблоко', 'портфель', 'корзина', 'рация',
                     'паутина', 'фейерверк', 'велосипед', 'весы', 'лестница', 'терминатор',
                     'кондиционер', 'монета', 'икота', 'лопух', 'чебурашка', 'транспорт',
                     'зубочистка', 'перчатки', 'домохозяйка', 'именинница', 'мёд', 'мангал',
                     'буратино', 'креветка', 'наушники', 'будильник', 'кенгуру', 'будильник',
                     'светофор', 'зоопарк', 'огонь', 'спички', 'капуста', 'камень',
                     'кроссовки', 'ягода', 'электричество', 'аспирин', 'танк', 'хлопушка')
        answer = random.choice(word_list)
        hidden_ans = len(answer) * '-'
        temp = list(hidden_ans)
        chances = 0

        check = set()
        while chances < 8:
            i = 0
            print()
            print(hidden_ans)
            guess = (input("Input a letter:"))
            if len(guess) != 1:
                print("You should input a single letter")
                continue
            if not guess.islower():
                print("It is not an ASCII lowercase letter")
                continue
            if guess in check:
                print("You already typed this letter")
                continue
            check.add(guess)
            if guess not in answer:
                print("No such letter in the word")
                chances += 1
                print(f"осталось {8 - chances} жизней")
            else:
                for letters in answer:
                    if guess == letters:
                        temp[i] = guess
                    i = i + 1
                hidden_ans = "".join(temp)
                if hidden_ans == answer:
                    print("You guessed the word!")
                    print("You survived!")
                    break
        else:
            print(answer)
            print("You are hanged!")
        ask_the_player()
    if mode == "exit":
        return
ask_the_player()