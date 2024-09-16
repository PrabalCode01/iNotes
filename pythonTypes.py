def add(firstname:str, lastname:str | None):
    a = [['apple', 'banana', 'cherry']]
    b = ['Ford', 'BMW', 'Volvo']
    a.append(b)
    print(a)
    return firstname.capitalize()+" "+lastname


fname = "pRabal"
lname = "Singh"
name = add(fname,lname)
print(name)