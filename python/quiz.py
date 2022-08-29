import getpass, sys

def question_with_response(prompt):
    print("Question: " + prompt)
    return input()

# create a dictionary (key value) of questions and answers
# this way I can add as many questions as I want without duplicating the code
quesstionsAndAsnwers = {
  "What command is used to include other functions that were previously developed?": "import",
  "What command is used to evaluate correct or incorrect response in this example?": "if",
  "Each 'if' command contains an '_________' to determine a true or false condition?": "expression"
}

# since the number of questions can change, the questions variable is populated with the length of the dictionary
questions = len(quesstionsAndAsnwers)
correct = 0

print('Hello, ' + getpass.getuser() + " running " + sys.executable)
print("You will be asked " + str(questions) + " questions.")
print("Are you ready to take a test! Hit Enter to begin.")
input()

# iterate over the keys from the dictionary
for key in quesstionsAndAsnwers:
    # pass the question (key) to the function
    rsp = question_with_response(key)
    # compare the user response with value from the dictionary (the answer)
    if rsp == quesstionsAndAsnwers[key]:
        print(rsp + " is correct! Wohoo!")
        correct += 1
    else:
        print(rsp + " is incorrect! Better luck next time :(")

print(getpass.getuser() + " you scored " + str(correct) + "/" + str(questions))
#print the percentage
print("Total Percentage: " + str (format(correct/questions * 100,".2f")) + "%")

