import getpass, sys

def question_with_response(prompt):
    print("Question: " + prompt)
    msg = input()
    return msg

questionsDict = {"What command is used to include other functions that were previously developed?": "import",
    "What command in this example is used to evaluate a response?": "if", 
    "Each 'if' command contains an '_________' to determine a true or false condition?": "expression",
    "What does Jupyter Notebooks use": "python",
    "What is the end of the file name of Mark Down Post": ".md",
    "What kernel does one need to use to use python": "ipykernel",
    "What command in terminal allows one to switch directort": "cd"
}
questions = len(questionsDict)
correct = 0


print('Hello, ' + getpass.getuser() + " running " + sys.executable)
print("You will be asked " + str(questions) + " questions.")
print("Are you ready to take a test! Press Enter key to begin. Best of luck :)")
input()

for key in questionsDict:
    rsp = question_with_response(key)
    if rsp.lower() == questionsDict[key].lower():
        print(rsp + " is correct! Good Job!")
        correct += 1
    else:
        print(rsp + " is incorrect! Better Luck next time.")
    
print(getpass.getuser() + " you scored " + str(correct) +"/" + str(questions))
page = correct/questions * 100
print("Total Percentage: " + str (format(page,".2f")) + "%")