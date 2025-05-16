with open("story.txt","r") as f:
    story = f.read()

words = set()
start_of_word = -1

target_start = "<"
target_end = ">"

for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i

    if char == target_end and start_of_word != -1:
        word = story[start_of_word: i+1]
        words.add(word)
        start_of_word = -1

answers = {}

for word in words:
    answer = input("Enter a word for "+ word.strip("}").strip("{")+": ")
    answers[word] = answer

for word in words:
    story = story.replace(word, answers[word])

print(story)

'''I found a gross creature in my school.  
It was gross, pink, and could run!  
It loved eating pants and running.  
Then it gave me a gross calendar and vanished.  
Best sunday ever.'''