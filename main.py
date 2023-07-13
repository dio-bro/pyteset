uIn = []
for i in range(2):
    uIn.append(input("Enter your name: "))
    uIn.append(int(input("Enter your age: ")))
    if uIn[-1] < 18:
        uIn[-2] = f"Go home, {uIn[-2]}! You are too young!"
    else:
        uIn[-2] = f"Hello, Mr. {uIn[-2]}. Wanna have some fun?"

print(f"\n{uIn[0]}\n"
      f"{uIn[2]}")