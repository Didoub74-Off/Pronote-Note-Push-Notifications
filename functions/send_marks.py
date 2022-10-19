from replit import db
import os
from pushsafer import Client


def marks(client):
    print("Starting fetching marks")
    for period in client.periods:
        for grade in period.grades:
            gradeDate = grade.date.strftime('%d/%m/%y')
            id = grade.grade + '/' + grade.out_of + ' - ' + gradeDate
            if (db.prefix(id) == ()):
                db[id] = "True"
                print(grade.subject.name)
                print(grade.grade + '/' + grade.out_of + ' ' +
                      grade.subject.name)
                for averages in period.averages:

                    if (averages.subject.name == grade.subject.name):
                        '''notifications_marks(grade.grade, grade.out_of,
                                            grade.subject.name, grade.average,
                                            averages.student,
                                            period.overall_average)'''
    print("Fetching marks finished")


def notifications_marks(grade, out_of, subject, grade_average,
                        student_subject_average, student_overall_average):
    pushClient = Client(os.environ['apikey'])
    resp = pushClient.send_message(
        "Bonjour " + os.environ['first_name'] + ",\n Une nouvelle note est arrivée !\n" + str(subject) +
        " : " + str(grade) + "/" + str(out_of) +
        "\nLa moyenne de la classe est de: " + str(grade_average) + "/" +
        str(out_of) + "\nVotre moyenne dans cette matière est désormais de: " +
        str(student_subject_average) +
        "/20\nVotre nouvelle moyenne générale est de: " +
        str(student_overall_average) + "/20", "Nouvelle note", os.environ['device_id'])
    print(resp)
