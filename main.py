from http.client import responses
import requests
response = requests.get('https://geek-jokes.sameerkumar.website/api?format=json')
joke = response.json()


# Answer the riddles correctly and a joke is printed out
# QUESTION 1 -------------------------------------------------------------------
print("You answer me, although I never ask you questions. What am I?")

answer = input("Enter your answer: ")
print(" ")
    # answer: Telephone
if (answer == "Telephone") :
    print("Your answer is correct! You have earned yourself a joke :)")
    print(joke['joke'])
else:
    print("Wrong answer, better luck next time :(")


# QUESTION 2 -------------------------------------------------------------------
response = requests.get('https://geek-jokes.sameerkumar.website/api?format=json')
joke = response.json()

print(" ")
print("The more you take, the more you leave behind. What am I?")

answer2 = input("Enter your answer: ")

print(" ")

    # answer: Footsteps
if (answer2 == "Footsteps"):
    print("Your answer is correct! You have earned yourself a joke :)")
    print(joke['joke'])
else:
    print("Wrong answer, better luck next time :(")

# QUESTION 3 -------------------------------------------------------------------
response = requests.get('https://geek-jokes.sameerkumar.website/api?format=json')
joke = response.json()

print(" ")
print("I am not alive, but I grow; I don't have lungs, but I need air; I don't have a mouth, but water kills me. What am I?")

answer3 = input("Enter your answer: ")

print(" ")

    # answer: Fire

if (answer3 == "Fire"):
    print("Your answer is correct! You have earned yourself a joke :)")
    print(joke['joke'])
else:
    print("Wrong answer, better luck next time :(")