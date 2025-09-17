import random
with open("russian_words.txt") as f:
    fin = f.readlines()
    mas = []
    for i in fin:
        mas.append(i[:5])
random_number = random.randint(0,len(mas))
numbers = ["0","1","2","3","4","5","6","7","8","9"]
final_word = mas[random_number]
answers = []
answers_2 = []
attempts = 6
while attempts > 0:
    mas_words = []
    player_word = str(input())
    while len(player_word) != 5:
        print("Это слово не подходит!")
        player_word = str(input())
    for i in numbers:
        while i in player_word:
            print("Это слово не подходит!")
            player_word = str(input())
            while len(player_word) != 5:
                print("Это слово не подходит!")
                player_word = str(input())
    for i in range(len(final_word)):
        if player_word[i] in final_word:
            if player_word[i] == final_word[i]:
                mas_words.append(player_word[i])
            else:
                mas_words.append("#")
        else:
            mas_words.append("0")
    answer = mas_words[0] + mas_words[1] + mas_words[2] + mas_words[3] + mas_words[4]
    answers.append(player_word)
    answers_2.append(answer)
    print("-------------")
    for i in range(len(answers)):
        print(f"{answers[i]} - {answers_2[i]}")
    print("-------------")
    if answer == final_word:
        print("Это правильное слово!")
        exit()
    attempts -= 1
print(f"У вас закончились попытки. Загаданное слово: {final_word}")