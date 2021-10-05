def Writepwd():
    file = open("D:\Python Projects\password manager\info.txt", 'a')

    user_Name = input("Please enter the user name: ")
    pwd = input("Please enter the password here: ")
    website_Name = input("Please enter the website address here: ")

    print()
    print()

    usrnm ="UserName: " + user_Name + "\n"
    pwd ="Password: " + pwd + "\n"
    web ="Website: " + website_Name + "\n"

    file.write("---------------------------------\n")
    file.write("\n")
    file.write(usrnm)
    file.write(pwd)
    file.write(web)
    file.write("\n")
    file.write("---------------------------------\n")
    file.close


def rpwd():
    
    file = open('D:\Python Projects\password manager\info.txt', 'r')
    content = file.read()
    file.close()
    print(content)


print()
print()



print("Welcome to Password management system")

print()
print()

choice = input("Enter your Choice Write (__a__)/Read(__r__) : ")

if choice=="a":
    Writepwd()
else:
    rpwd()

