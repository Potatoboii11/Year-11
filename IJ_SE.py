import random as random
import math as math
import time

def quiz():
    stage_level =  stage()
    num_of_questions = num_questions_function()
    start()
    global start_time
    global num_correct_answers
    global question_list 
    global user_answers
    global answer_list
    question_list = []
    num_correct_answers = 0
    user_answers = []
    answer_list = []
    start_time = time.time()
    for question_num in range(num_of_questions):
        print(f"Question {question_num+1}:")
        module_stage(stage_level)
    end_time = time.time()
    total_time = round(end_time - start_time,2)
    stats(num_of_questions, total_time)
    try_again = input("Would you like to try again?: ")
    try_again = try_again.lower()
    if try_again == 'yes':
        quiz()
    else:
        print("End")

        
def stage():
    print("What stage are you in?")
    while True:
        try:
            stage_level =  int(input("(1-3) Stage: ")) 
            if 1 <= stage_level <= 3:
                return stage_level
            elif 3 < stage_level <= 6:
                print("Your education level is too high for this code, please type in a number between 1 and 6")
            else:
                print("Your year level does not exist, please try again")
        except (ValueError):        
            print("Description of code: This quiz intends to help you revise for everything you have learnt in that year by asking random questions from the syllabus. This quiz is only intended for stage 1 - stage 3. Type in 'start' to begin") #Doesn't output an error when a string is inputted instead of an integer.
            print("Please enter a number")
            stage()
    


def num_questions_function(): #For the amount of questions to be in the quiz
    try:
        input_num_questions =  int(input("How many questions would you like to do in your quiz? (1-10) "))
        if 0 < input_num_questions <= 10:
            return input_num_questions
        else:
            print("The number you have inputted is invalid. Please try again")
            num_questions_function()
    except(ValueError): #Doesn't output an error when a string is inputted instead of an integer.
        print("Please enter a number")
        return num_questions_function() #Return so that 'None' isn't returned 

def start():
    begin = input("Type in 'start' to begin: ").strip().lower() #puts the variable in lowercase too help match 'start'
    if begin == 'start': #Countdown to start
        print("Beginning in:")
        time.sleep(1) #Stops code for 1 second
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1") 
    elif begin == 'help':
        print("Description of code: This quiz intends to help you revise for everything you have learnt in that year by asking random questions from the syllabus. This quiz is only intended for stage 1 - stage 3. Type in 'start' to begin")
        start() #Call start again for a loop
    else:
        print("Please try again, they may have been a typo")
        start()

def module_stage(year_level):
    if year_level == 1:
        stage1()
    elif year_level == 2:
        stage2()
    elif year_level == 3:
        stage3()

def correct_answer(user_answer,question, actual_answer):
    global num_correct_answers
    if user_answer == actual_answer:
        num_correct_answers += 1
    user_answers.append(user_answer)
    question_list.append(question)
    answer_list.append(actual_answer)


def stage1(): 
    module = random.randint(1,4)
    if module == 1: #Number before or after
        random_number = random.randint(1,99) #it is 99 because the syllbus says that year 1 should be able to identify the number before or after any two digit number
        random_increasing_or_decreasing = random.randint(1,2)
        if random_increasing_or_decreasing == 1:
            question = f"What number comes before {random_number}"
            actual_answer = random_number - 1
        elif random_increasing_or_decreasing == 2:
            question = f"What number comes after {random_number}"
            actual_answer = random_number + 1
        print(question)
        try:
            user_answer = int(input("Enter your answer: "))
        except (ValueError):         
            print("Description of code: This quiz intends to help you revise for everything you have learnt in that year by asking random questions from the syllabus. This quiz is only intended for stage 1 - stage 3. Type in 'start' to begin")
            print("That input is not valid and will not be counted, you will be given a new question")
            return stage1()
        correct_answer(user_answer, question, actual_answer)

    elif module == 2: #Number of tens
        random_number = random.randint(1,99)
        question = f"How many tens are in this number: {random_number}"
        print(question)
        actual_answer = random_number // 10   # Floor devision rmeoves remainder when deviding
        try:
            user_answer = int(input("Enter your answer: "))    
        except (ValueError):         
            print("Description of code: This quiz intends to help you revise for everything you have learnt in that year by asking random questions from the syllabus. This quiz is only intended for stage 1 - stage 3. Type in 'start' to begin")
            print("That input is not valid and will not be counted, you will be given a new question")
            return stage1()
        correct_answer(user_answer, question, actual_answer)

    elif module == 3: #Skip counting
        random_number = random.randint(1,99)
        random_skip_count = random.randint(1,5)
        question = f"Find the next number in the number pattern:"
        print(question)
        for i in range (1,5):
            print(random_number + random_skip_count*i, end = ' ')
        print("_")
        actual_answer = random_number + random_skip_count*5
        try:
            user_answer = int(input("Enter your answer: "))
        except (ValueError):         
            print("Description of code: This quiz intends to help you revise for everything you have learnt in that year by asking random questions from the syllabus. This quiz is only intended for stage 1 - stage 3. Type in 'start' to begin")
            print("That input is not valid and will not be counted, you will be given a new question")
            return stage1()
        correct_answer(user_answer, question, actual_answer)
    
    else: #Addition and subtraction
        random_number1 = random.randint(1,20)
        random_addition_subtraction = random.randint(1,2)
        if random_addition_subtraction == 1:
            random_number2 = random.randint(1,20)
            question = f"What is {random_number1} + {random_number2}"
            actual_answer = random_number1 + random_number2
        elif random_addition_subtraction == 2:
            random_number2 = random.randint(1,random_number1) #Second number will always be smaller then first number
            question = f"What is {random_number1} - {random_number2}"
            actual_answer = random_number1 - random_number2
        print(question)
        try:
            user_answer = int(input("Enter your answer: "))
        except (ValueError):         
            print("Description of code: This quiz intends to help you revise for everything you have learnt in that year by asking random questions from the syllabus. This quiz is only intended for stage 1 - stage 3. Type in 'start' to begin")
            print("That input is not valid and will not be counted, you will be given a new question")
            return stage1()
        correct_answer(user_answer, question, actual_answer)

def stage2():
    module = random.randint(1,4)
    if module == 1: #Skip counting by 10s or 100s
        random_number = random.randint(1,1000)
        skip_count_tens_hundreds = random.randint(1,2)
        question = f"Find the next number in the number pattern:"
        print(question)
        if skip_count_tens_hundreds == 1:
            skip_count = 10
            for i in range (1,5):
                print(random_number + skip_count*i, end = ' ')
            print("_")
            actual_answer = random_number + skip_count*5
        else:
            skip_count = 100
            for i in range (1,5):
                print(random_number + skip_count*i, end = ' ')
            print("_")
            actual_answer = random_number + skip_count*5
        try:
            user_answer = int(input("Enter your answer: "))
        except (ValueError):         
            print("Description of code: This quiz intends to help you revise for everything you have learnt in that year by asking random questions from the syllabus. This quiz is only intended for stage 1 - stage 3. Type in 'start' to begin")
            print("That input is not valid and will not be counted, you will be given a new question")
            return stage2()
        correct_answer(user_answer, question, actual_answer)
    
    elif module == 2: #Addition and subtraction of 3 digit numbers
        random_number1 = random.randint(1,100)
        random_addition_subtraction = random.randint(1,2)
        if random_addition_subtraction == 1:
            random_number2 = random.randint(1,100)
            question = f"What is {random_number1} + {random_number2}"
            actual_answer = random_number1 + random_number2
        elif random_addition_subtraction == 2:
            random_number2 = random.randint(1,random_number1) #Second number will always be smaller then first number
            question = f"What is {random_number1} - {random_number2}"
            actual_answer = random_number1 - random_number2
        print(question)
        try:
            user_answer = int(input("Enter your answer: "))
        except (ValueError):         
            print("Description of code: This quiz intends to help you revise for everything you have learnt in that year by asking random questions from the syllabus. This quiz is only intended for stage 1 - stage 3. Type in 'start' to begin")
            print("That input is not valid and will not be counted, you will be given a new question")
            return stage2()
        correct_answer(user_answer, question, actual_answer)

    elif module == 3: #multiplication
        random_number1 = random.randint(2,10)
        random_number2 = random.randint(2,1)
        question = f"What is {random_number1} x {random_number2}"
        print(question)
        actual_answer = random_number1*random_number2
        try:
            user_answer = int(input("Enter your answer: "))
        except (ValueError):         
            print("Description of code: This quiz intends to help you revise for everything you have learnt in that year by asking random questions from the syllabus. This quiz is only intended for stage 1 - stage 3. Type in 'start' to begin")
            print("That input is not valid and will not be counted, you will be given a new question")
            return stage2()
        correct_answer(user_answer, question, actual_answer)
        
    
    else: #angle
        type_of_angle = random.randint(1,3)
        actual_answer = None
        if type_of_angle == 1:
            question = ("Type in an angle that is an acute angle")
            
        elif type_of_angle == 2:
            question = ("Type in an angle that is a right angle")

        elif type_of_angle == 3:
            question = ("Type in an angle that is an obtuse angle")
        print(question)
        try:
            user_answer = int(input("Enter your answer: "))
        except (ValueError):         
            print("Description of code: This quiz intends to help you revise for everything you have learnt in that year by asking random questions from the syllabus. This quiz is only intended for stage 1 - stage 3. Type in 'start' to begin")
            print("That input is not valid and will not be counted, you will be given a new question")
            return stage2()
        if type_of_angle == 1 and 1 <= user_answer < 90 or type_of_angle == 2 and user_answer == 90 or type_of_angle == 3 and 90 < user_answer < 180:
            actual_answer = user_answer
        correct_answer(user_answer, question, actual_answer)

def stage3():
    module = random.randint(1,4)
    if module == 1: #Addition and Subtraction 
        random_number1 = random.randint(1,1000)
        random_addition_subtraction = random.randint(1,2)
        if random_addition_subtraction == 1:
            random_number2 = random.randint(1,1000)
            question = f"What is {random_number1} + {random_number2}"
            actual_answer = random_number1 + random_number2
        elif random_addition_subtraction == 2:
            random_number2 = random.randint(1,random_number1) #Second number will always be smaller then first number
            question = f"What is {random_number1} - {random_number2}"
            actual_answer = random_number1 - random_number2
        print(question)
        try:
            user_answer = int(input("Enter your answer: "))
        except (ValueError):         
            print("Description of code: This quiz intends to help you revise for everything you have learnt in that year by asking random questions from the syllabus. This quiz is only intended for stage 1 - stage 3. Type in 'start' to begin")
            print("That input is not valid and will not be counted, you will be given a new question")
            return stage3()
        correct_answer(user_answer, question, actual_answer)

    elif module == 2: #Finding product 1-20
        random_number1 = random.randint(2,20)
        random_number2 = random.randint(2,10)
        random_number3 = random.randint(2,10)
        question = f"What is the product of {random_number1}, {random_number2} and {random_number3}"
        print(question)
        actual_answer = random_number1*random_number2*random_number3
        try:
            user_answer = int(input("Enter your answer: "))
        except (ValueError):         
            print("Description of code: This quiz intends to help you revise for everything you have learnt in that year by asking random questions from the syllabus. This quiz is only intended for stage 1 - stage 3. Type in 'start' to begin")
            print("That input is not valid and will not be counted, you will be given a new question")
            return stage3()
        correct_answer(user_answer, question, actual_answer)

    elif module == 3: #Convertion of length
        random_number1 = random.randint(1,1000)
        random_convertion = random.randint(1,4)
        if random_convertion == 1:
            question = f"Convert {random_number1}m to cm"
            actual_answer = random_number1*100
        elif random_convertion == 2:
            question = f"Convert {random_number1}km to m"
            actual_answer = random_number1*1000
        elif random_convertion == 3:
            question = f"Convert {random_number1}m to km"
            actual_answer = random_number1/1000
        else:
            question = f"Convert {random_number1}cm to m"
            actual_answer = random_number1/100
        print(question)
        try:
            user_answer = float(input("Enter your answer: "))
        except (ValueError):         
            print("Description of code: This quiz intends to help you revise for everything you have learnt in that year by asking random questions from the syllabus. This quiz is only intended for stage 1 - stage 3. Type in 'start' to begin")
            print("That input is not valid and will not be counted, you will be given a new question")
            return stage3()
        correct_answer(user_answer, question, actual_answer)
        

    else: #Area and perimeter of rectangles
        side1 = random.randint(1,20)
        side2 = random.randint(1,20)
        perimeter_or_area = random.randint(1,2)
        if perimeter_or_area == 1:
            question = f"Find the perimeter of a rectangle with sides {side1} and {side2}"
            actual_answer = side1*2 + side2*2
        else:
            question = f"Find the area of a rectangle with sides {side1} and {side2}"
            actual_answer = side1*side2
        print(question)
        try:
            user_answer = float(input("Enter your answer: "))
        except (ValueError):         
            print("Description of code: This quiz intends to help you revise for everything you have learnt in that year by asking random questions from the syllabus. This quiz is only intended for stage 1 - stage 3. Type in 'start' to begin")
            print("That input is not valid and will not be counted, you will be given a new question")
            return stage3()
        correct_answer(user_answer, question, actual_answer)
        

def stats(num_of_questions, total_time):
    print("\nResults: ")
    print('Questions asked:',question_list)
    print('Answers to the questions:',answer_list)
    print('Your answers:',user_answers)
    percentage = round((num_correct_answers/num_of_questions) * 100,2)
    print(f"\nYou took {total_time}s to complete {num_of_questions} and got {num_correct_answers} correct ({percentage}%)")
    
print("Welcome to the Math quiz (Stage 1-3)")
print("Type help if you need help. Note that you will not recieve help on the questions themselves.")
quiz()