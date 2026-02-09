import os

# initialize git repository
os.system("git init")

# create a sample file
f = open("file.txt", "w")
f.write("This is main branch file")
f.close()

# add and commit in main branch
os.system("git add .")
os.system('git commit -m "Initial commit in main branch"')

# create and switch to new branch
os.system("git checkout -b feature")

# modify file in feature branch
f = open("file.txt", "a")
f.write("\nThis line is added in feature branch")
f.close()

# add and commit in feature branch
os.system("git add .")
os.system('git commit -m "Commit in feature branch"')

# switch back to main branch
os.system("git checkout master")

# merge feature branch into main
os.system("git merge feature")

print("Branching and merging completed successfully!")
