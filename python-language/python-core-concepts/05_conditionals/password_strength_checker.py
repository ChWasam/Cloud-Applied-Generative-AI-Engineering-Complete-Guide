# Problem: Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).

password:str = input("Enter Password")

if len(password)<6:
    print("Weak Password")
elif len(password)<11:
    print("Medium Password")
else:
    print("Strong Password")