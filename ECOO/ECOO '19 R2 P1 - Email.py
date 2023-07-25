for i in range(10):
    emails = []
    for j in range(int(input())):
        email = input()
        email = email.lower().split("@")
        email[0] = email[0].replace(".", "")
        email[0] = email[0].split("+")[0]
        emails.append(email[0] + "@" + email[1])

    print(len(set(emails)))
