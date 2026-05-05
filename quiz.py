
questions = ["Who painted the Mona Lisa?",
             "Which planet is known as the Blue Planet?",
             "What is the chemical symbol for Water?",
             "Which is the largest continent on Earth?",
             "How many colors are in a rainbow?"]
options = [["A. Vincent van Gogh","B. Pablo Picasso","C. Leonardo da Vinci","D. Claude Monet"],
           ["A. Mars","B. Earth", "C. Neptune", "D. Venus"],
           ["A. CO2", "B. O2", "C. H2O", "D. NaCl"],
           ["A. Africa", "B. Asia", "C. Europe", "D. North America"],
           ["A. 5", "B. 6", "C. 7", "D. 8"]]
answers = ["C", "B", "C", "B", "C"]

def ask_questions(question,opt,ans,qno):
    print("\nQuestion",qno)
    print(question)
    for option in opt:
        print(option)

#input validation
    while True:
        user=input("Enter your answer(A/B/C/D):").upper()
        if user in ["A","B","C","D"]:
            break
        else:
            print("Invalid input! Please enter A,B,C,D.")

    if user==ans:
        print("Correct")
        return 1
    else:
        print("Incorrect! correct answer is:",ans)
        return 0

def run_quiz():
    score=0
    for i in range (len(questions)):
        score+=ask_questions(questions[i],options[i],answers[i],i+1)
    print("Final score is:",score,"/",len(questions))
        
#menu system
while True:
        print("\n Quiz Menu ")
        print("1.start quiz")
        print("2.Exit")
        choice=input("Enter your choice:")
        if choice=="1":
            run_quiz()
            again=input("\n Do you want to play again?(Y/N):").upper()
            if again !="Y":
                print("Thank you")
                break

        elif choice=="2":
            print("Good Bye!")
            break
        else:
            print("Invalid choice! please select 1 or 2:")




    



    
