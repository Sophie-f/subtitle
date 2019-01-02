subtitle_file = open("subtitle.txt", "r")
learning_file = open("learning.txt", "a+")
all_words_file = open("all_words.txt", "a+")


def is_valid(word):
    if len(word) < 3:
        return False
    num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for char in word:
        if char in num_list:
            return False
    return True        
            

def is_not_in_all_words(word):
    all_words_file.seek(0)
    all_word_list = all_words_file.readlines()
    for words in all_word_list:
        if word+"\n" == words:
            return False
    return True      


sub_list_word = []
sub_list_line = subtitle_file.readlines()
for line in sub_list_line:
    sub_list_word += line.split()
for word in sub_list_word:
    word = word.strip().strip('?').strip('!').strip("...").strip(",").strip(".").lower()
    if is_valid(word):
        if is_not_in_all_words(word):
            all_words_file.write(word+"\n")
            print(word)
            answer = input("Do you want this word is written in lerning_file? y/n")
            if answer == "y":
                print(word, "is written in learning_file")
                learning_file.write(word+"\n")
subtitle_file.close()
learning_file.close()
all_words_file.close()
