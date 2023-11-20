from art import logo,vs;
from data import data;
import random;
import os;

print(logo);

# 이름, 설명, 나라 함수
def printData(account):
    name = account["name"];
    description = account["description"];
    country = account["country"];
    return (f"{name}, a {description}, from {country}");

# 팔로워 숫자 함수
def followerCount(accountA, accountB):
    countA = accountA["follower_count"];
    countB = accountB["follower_count"];

    if countA < countB:
        return "A"
    else:
        return "B"
    
dataRandomB = random.choice(data);
isGameChk = False;
score=0;
while not isGameChk:

    # 라운드 진행되면 b 정보를 a에 입력
    dataRandomA = dataRandomB;

    # A,B가 같으면 B에 랜덤 데이터 입력
    while dataRandomA == dataRandomB:
        dataRandomB = random.choice(data);
        
    print(f"Compare A: {printData(dataRandomA)}.");
    print(vs);
    print(f"Compare B: {printData(dataRandomB)}.");

    countChoice = followerCount(dataRandomA, dataRandomB);
    choice = input("Who has more followers? Type 'A' or 'B': ")

    os.system("cls"); # clear 처리
    print(logo);
    if countChoice.lower() != choice.lower():
        isGameChk = True;
        print(f"Sorry, that's wrong. Final score: {score}");
    else:
        score+=1;
        print(f"You're right! Current score: {score}");