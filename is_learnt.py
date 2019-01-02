learning_file = open("learning.txt", "r")
learnt_file = open("learnt.txt", "a+")
keep_list = []

learning_list = learning_file.readlines()
for word in learning_list:
    print(word, end="")
    answer = input("did you learn it? y/n")
    if answer == "y":
        learnt_file.write(word)
        print(word, "is written in learnt_file")
        keep_list.append(word)
# deleting learnt_word from learning_list 
for word in keep_list: 
    learning_list.remove(word)
learning_file.close()

# over_writing learning_file
learning_file = open("learning.txt", "w")
for word in learning_list:
    learning_file.write(word)
    
learning_file.close()
learnt_file.close()    
