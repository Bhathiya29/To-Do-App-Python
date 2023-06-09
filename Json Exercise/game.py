import json

with open('questions.json', 'r') as file:
    content = file.read()

print(type(content))
print(content)
data = json.loads(content)
print(type(data))
print(data)

for question in data:
    print(question['question_text'])
    for index, alternative in enumerate(question['alternatives']):
        print(index + 1, "-", alternative)
    choice = int(input("Please Enter Your Answer: "))
    question["choice"] = choice


score = 0
for index,question in enumerate(data):
    if question['choice'] == question['correct_answer']:
        score += 1
        result='Correct Answer'
    else:
        result='Wrong Answer'

    message=f"{result} {index+1} Your answer: {question['choice']}, Correct answer: {question['correct_answer']}"
    print(message)

print(score, "/", len(data))