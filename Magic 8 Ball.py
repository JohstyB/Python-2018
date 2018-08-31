#Johsty Bach, 8/27/18, 2nd Period

#Imported modules.
import random
import time

#Possible Responses for the output at the end.
responses = ["It is certain.", "It is decidedly so.", "Without a doubt.",
             "Yes - definitely.", "You may rely on it.", "As I see it, yes.",
             "Most Likely.", "Outlook good.", "Yes.", "Signs point to yes.",
             "Reply hazy, try agian.", "Ask agian later.",
             "Better not tell you now.", "Cannot predict now.",
             "Concentrate and ask agian.", "Don't count on it.",
             "My reply is no.", "My sources say no.", "Outlook not so good.",
             "Very Doubtful."]

#Determines if the question being asked is the first or not, changes first
#question accordingly. Will also not ask for the user's name after the 1st question.
questionAsked = 0



#Makes it to where it only asks for the user's name once, since
#it is outside of the loop.
userName = input("What is your name?: ")

while True:
    if questionAsked < 1:
        firstQuestion = input("Would you like to ask a question? Answer with Y or N: ")
        if firstQuestion == ("Y"):
            secondQuestion = input("Please ask your question: ")
            result = random.choice(list(responses))
            print("The answer to the question: ' %s ', %s , is: %s." % (secondQuestion, userName, result))
            questionAsked = 1
        elif firstQuestion == ("N"):
            print("Ok then, Goodbye!")
            break
        else:
            print("Please enter a valid response.")
    if questionAsked == 1:
        thirdQuestion = input("Would you like to ask another question? Answer with Y or N: ")
        if thirdQuestion == ("Y"):
            secondQuestion = input("Please ask your question: ")
            result = random.choice(list(responses))
            print("The answer to the question: ' %s ', %s , is: %s." % (secondQuestion, userName, result))
        elif thirdQuestion == ("N"):
            print("Ok then, Goodbye!")
            break
        else:
                print("Please enter a valid response.")
