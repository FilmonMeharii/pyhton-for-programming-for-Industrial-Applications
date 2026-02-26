

with open("data.csv", "w") as f:
    f.write("a,b\n")
    for i in range(1, 6):
        f.write(f"{i},{i*10}\n")