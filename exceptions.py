try :
    age=int(input("age:"))
    income=29000
    risk=income/age
    print(risk)
    print(age)
except ZeroDivisionError:
    print('age no 0')
except ValueError:
    print("Invalid error")
