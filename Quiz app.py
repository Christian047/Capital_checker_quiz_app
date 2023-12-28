
# Show the result when quiz is completed

# Create a dictionary that stores questions and answers
# {question:{question|answer}}
def quiz_questions():
    
  while True:
    quiz = {
        'question1':{
            'question': 'What is the Capital of France? ',
            'answer':'Paris'
        },
        
        'question2':{
            'question': 'What is the Capital of Germany? ',
            'answer':'Berlin'
        },
        
        'question3':{
            'question': 'What is the Capital of Italy? ',
            'answer':'Rome'
        },
        'question4':{
            'question': 'What is the Capital of Spain? ',
            'answer':'Madrid'
        },
        
        'question5':{
            'question': 'What is the Capital of Portugal? ',
            'answer':'Lisbon'
        },
        
        'question6':{
            'question': 'What is the Capital of Switzerland? ',
            'answer':'Bern'
        },
        
        'question7':{
            'question': 'What is the Capital of Austria? ',
            'answer':'Vienna'
        },
    }

    # Have a variable that tracks the scores of the players 
    score = 0

    # loop through the dictionary using key value pairs
    for key,value in quiz.items():
        correct_answer =value['answer']
        
        
        # display each question to the user and allow them to answer
        print(value['question'])
        answer = input('Answer? ')
        if answer.lower() == correct_answer.lower():
            print('')
            print('Correct')
            score+=1
            print(f'Your Score is {score}')
            
        else:
            print('')
            print('Wrong Answer!')
            print(f'The correct answer is {correct_answer}')
            print(f'Your Score is {score}')
            print('')
            
            
    print(f'Your final score is {score} out of  questions')
    print(f'Your percentage is {score/7 * 100}%')
    
    
# Ask if the user wants to play again
    while True:
        play_again = input('Do you want to play again, Y or N?: ')
        
        if play_again.upper() == 'Y':
            continue
        
        if play_again.upper() == 'N':
            break
        else:
            print('Incorrect input')
    
    
quiz_questions()
