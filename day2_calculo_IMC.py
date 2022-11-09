# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
two_height = float (height)
two_weight = float (weight)
bmi = two_weight / (two_height*two_height)
print (round(bmi))