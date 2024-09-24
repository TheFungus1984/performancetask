def quiz():
    for i in questions:
        print(i)
        response = input("\n")
        answers.append(response)
def results(playername):
    score = 0
    if int(answers[0]) >= 8: 
        score = score+1
    if answers[1] == "y":
        score = score + 1
    if (float(answers[3])/(float(answers[2]))**2*703 <= 25.00 
        and float(answers[3])/(float(answers[2]))**2*703 >= 5.00):
        score = score + 1
    if int(answers[4]) <= 2300:
        score = score+1
    if int(answers[5]) >= 20:
        score = score + 1
    if answers[6] == 'n':
        score = score + 1
    if int(answers[7]) >= 6:
        score = score + 1
    if int(answers[8]) <= 6:
        score = score + 1
    if int(answers[9]) >= 5:
        score = score + 1
    print(playername+", your result is: " + str(score) + "/10")
    if score >= 8:
        print("Your health is fairly good, continue living this way.")
    if score >= 6 and score < 8:
        print("Think about living a bit healthier")
    if score >= 4 and score < 6: 
        print("Your health is average, but improvement is possible")
    if score >= 2 and score < 4:
        print("Your health is below average and action should be taken to remedy this")
    if score < 2:
        print("You should improve your health immediately")
answers = []
questions = ["1. How many hours of sleep do you get per night?", 
             "2. Do you regularly brush and floss your teeth?(y or n)",
             "3. What is your height?(inches)", 
             "4. What is your weight?(pounds)", 
             "5. About how many calories do you eat per day?",
             "6. On average, how many minutes do you spend performing physical activity a day?", 
             "7. Do you often feel lethargic or struggle to do basic tasks(y or n)",
             "8. How many cups of water do you drink per day?", 
             "9. How long ago have you gone to the dentist(months)", 
             "10. On a scale from 1-10, how do you feel right now?"]
print("Welcome to Yin's health quiz!")
print("You will be asked a series of questions pertaining to your health, and will be graded at the end by your answers")
name = input("To start, please input your name:\n")
quiz()
results(name)

