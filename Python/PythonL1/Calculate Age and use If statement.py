Child1YoB = 1999
Child2YoB = 2015
Child3Yob = 1962
CurrentYear = 2024

Child1Age = CurrentYear - Child1YoB
Child2Age = CurrentYear - Child2YoB
Child3Age = CurrentYear - Child3Yob

if Child1Age > 30:
    print("Child1 is ", end=''),print(Child1Age, end=''), print(" years old and he is above 60")
elif Child1Age > 18:
    print("Child1 is ", end=''),print(Child1Age, end=''), print(" years old and he is above 18 but below 60")
else:
    print("Child1 is ", end=''),print(Child1Age, end=''), print(" years old and he is below 18")

if Child2Age > 30:
    print("Child2 is ", end=''),print(Child2Age, end=''), print(" years old and he is above 60")
elif Child2Age > 18:
    print("Child2 is ", end=''),print(Child2Age, end=''), print(" years old and he is above 18 but below 60")
else:
    print("Child2 is ", end=''),print(Child2Age, end=''), print(" years old and he is below 18")  

if Child3Age > 30:
    print("Child3 is ", end=''),print(Child3Age, end=''), print(" years old and he is above 60")
elif Child3Age > 18:
    print("Child3 is ", end=''),print(Child3Age, end=''), print(" years old and he is above 18 but below 60")
else:
    print("Child3 is ", end=''),print(Child3Age, end=''), print(" years old and he is below 18")      