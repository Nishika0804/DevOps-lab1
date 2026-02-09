import os

os.system("git init")

# main branch file
with open("file.txt", "w") as f:
    f.write("This is the main branch.")

os.system("git add .")
os.system('git commit -m "Main branch commit"')

# create feature branch
os.system("git checkout -b feature")

# modify same line
with open("file.txt", "w") as f:
    f.write('This is the main branch. "Change from feature branch"')

os.system("git add .")
os.system('git commit -m "Feature branch change"')

# go back to main
os.system("git checkout master")

# modify same line again
with open("file.txt", "w") as f:
    f.write("This is the main branch.")

os.system("git add .")
os.system('git commit -m "Main branch update"')

# merge (this will cause conflict)
os.system("git merge feature")

print("Merge conflict occurred")
