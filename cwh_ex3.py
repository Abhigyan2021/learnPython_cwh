name = input("Enter your name:")

print("Hello", name, "Good Morning!")
agree = input("Are you ready to become Crorepati?")

if agree == "Yes":
    print("Let's start the game...")
else:
    print("Let's play some other time.")

ques = [ "Which day is observed as World Standards Day.\nA Nov 15  B Oct 14 C Dec 2 D June 26 ",
          "The theme of the World Red Cross and Red Crescent Day was?\nA Dignity for all focus on Children B Nourishment for all-focus on children  C Focus on health for all D Dignity for all focus on women ",
          "What is celebrated on September 27 every year.\nA National Integration Day B Teachers' Day C  International Literacy Day D World Tourism Day",        
          "What day is observed as Sports Day every year.\nA 29th August B 2nd October C 26th July D 22nd April ",        
          "What day is observed as World Health Day?\nA Mat 15 B Apr 28 C Apr 7 D Mar 6 ",        
          "Which Year was celebrated as the World Communication Year.\nA 1983 B 1981 C 1987 D 1985 ",        
          "The abbreviation 'fob' stands for\nA Fellow of Britain B  Free of Bargain C Free on Board. D None of these ",        
          "According to a proverb, what is the mother of invention\nA Science B Necessity C Problem D Society ",        
          "Vault, uneven bars, and floor exercise are events in which sport?\nA Wrestling B  Synchronized Swimming C Skating D Gymnastics ",        
          "Which of the following is an Island country?\nA Maldives B Yemen C Peru D Oman ",        
          "Muslims lives in?\nA Pakistan B USA C India D Canada",        
          "The Sun is approximately how many miles away from the Earth?\nA 93 million B 9.3 million C 193 million D 39 million ",        
          "Since 2002, what is the currency of Greece?\nA Drachma B peso C Euro D Lira ",        
       ]
prize_money = [5000, 10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000,30000000]

ans = ['B','A','D','A','C','A','C','B','D','A','A','A','C']

prz = 0

for i in range(13):
    # if i != 0:
    #     q = input("Do you want to quit? Y or N")
    #     if q == "Y":
    #         print("Your prize money is:", prize_money[i-1])
    #         break

    print("question",i+1)
    print(ques[i])
    say = input("Which Option would you like to choose? (kindly ans in UpperCase)")
    if say == ans[i]:
        print("Correct Ans")
        prz = prize_money[i]
    else:
        print("Incorrect Ans. You are disqualified!")
        break
    

print(name,"you have won",prz,"rupees Congratulations!!")





