import subprocess

baseurl ="https://jakubkowalski.tech/Projects/LOCM/portraits/"

for i in range(1,160):
    num = ["0",""][i>99] + ["0",""][i>9] + str(i)
    img = baseurl + num + ".png"
    subprocess.run("wget " + img)