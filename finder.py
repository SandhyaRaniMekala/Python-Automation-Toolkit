import os
path = "."
target = "ERROR_CODE_99"
files = os.listdir(path)
for filename in files:
    if filename.endswith(".txt"):
        with open(filename, 'r') as f:
            data = f.read()
            if target in data:
                print(f"we got it! Secret is in: {filename}")
            else:
                    print(f"no! we did not get it: {filename}")