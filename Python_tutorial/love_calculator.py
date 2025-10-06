name_1=input("what is your name?")
name_2=input("whta is his/her name?")
combine_string=name_1+name_2
lower_case_string=combine_string.lower()
t=lower_case_string.count("t")
r=lower_case_string.count("r")
u=lower_case_string.count("u")
e=lower_case_string.count("e")
true=t+r+u+e
l=lower_case_string.count("l")
o=lower_case_string.count("o")
v=lower_case_string.count("v")
e=lower_case_string.count("e")
love=l+o+v+e
love_score=str(true)+str(love)
if int(love_score)<10 or int(love_score)>90 :
    print(F"your love score is {love_score}")
elif int(love_score)>=40 or int(love_score)<=90:
    print(F"your love score is {love_score}")
else :
    print(F"your love score is {love_score}")









