import os

# Step 1: Initialize git repository
os.system("git init")

# Step 2: Configure git
os.system('git config user.name "nishika"')
os.system('git config user.email "nishika.email@example.com"')

# Step 3: Create a sample file
f = open("app.py", "w")
f.write("print('Hello from GitHub')")
f.close()

# Step 4: Add files
os.system("git add .")

# Step 5: Commit
os.system('git commit -m "Initial commit"')

# Step 6: Add remote repository
repo_url = "https://github.com/Nishika0804/DevOps-lab1.git "
os.system(f"git remote add origin {repo_url}")

# Step 7: Push to GitHub
os.system("git push -u origin master")

print("Code pushed to GitHub successfully!")
