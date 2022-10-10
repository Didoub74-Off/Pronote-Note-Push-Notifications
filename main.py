import os
import pronotepy
from time import sleep
from sendMail import send_mail
from replit import db

db.clear()

while True:  # infinite loop
    client = pronotepy.Client.qrcode_login({"jeton": os.environ['jeton'],
                                            "login": os.environ['login'],
                                            "url": os.environ['url']},
                                            os.environ['passcode'])
    # check if sucessfully logged in
    if not client.logged_in:
        print("Client is not logged in")
        exit()
    else:
        print("Logged In")

    for period in client.periods:
        # Iterate over all the periods the user has. This includes semesters and trimesters.

        for grade in period.grades:  # the grades property returns a list of pronotepy.Grade
            gradeDate = grade.date.strftime('%d/%m/%y')
            id = grade.grade + '/' + grade.out_of + '->' + grade.average + ' - ' + gradeDate
            if (db.prefix(id) == ()):
                db[id] = "True"
                print(grade.subject.name)
                print(grade.grade + '/' + grade.out_of + ' ' +
                      grade.subject.name)
                send_mail(grade.grade, grade.out_of, grade.subject.name)

            else:
                print('No grade')
                sleep(60)
# print only the grades from the current period
