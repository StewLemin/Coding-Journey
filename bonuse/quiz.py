import json

with open("files/questions.json", 'r') as file:
    content = file.read()

data = json.loads(content)


for question in data:
    print(question["question_text"])
    for index, alternative in enumerate(question["alternatives"]):
        print(index+1, "-", alternative)
    answer = int(input("Enter the correct answer: "))
    question["answer"] = answer

score = 0
for index, question in enumerate(data):
    if question["answer"] == question["correct_answer"]:
        score = score + 1
        result = "Correct Answer"
    else:
        result = "Wrong Answer"
    message = f"{index + 1} {result} - You chose {question['answer']} and the correct answer was {question['correct_answer']}"
    print(message)
print("Final score",score, "/", len(data))
