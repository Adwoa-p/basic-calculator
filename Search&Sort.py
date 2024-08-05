# Linear Search
# MyList = [23,4,45,7,5,78]
# MaxIndex=6
# SearchValue = int(input("Input SearchValue: "))
# found=False
# index=-1
# while not found and index < MaxIndex:
#     if MyList[index] == SearchValue:
#         found = True
#     else:
#         index += 1
# if found==True:
#     print("Value at location: ",index)
# else:
#     print("Value not found")

from faker import Faker
fake = Faker('it_IT')

print("Name,Email,Date of birth")
for _ in range(10):
    name = fake.name()
    email = fake.email()
    dob = fake.date_of_birth()
    print(f"{name},{email},{dob}")