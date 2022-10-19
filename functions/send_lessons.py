from replit import db
import os
import datetime
from pushsafer import Client
def lessons(client):
  editedLessons = []
  twoTimeEvent = False
  numberOfEditedLessons = 0
  print("Starting fetching events")
  lessonsOfTheYear = client.lessons(datetime.datetime(2022, 9, 1),
                                              datetime.datetime(2023, 8, 31))
  print("Fetching events of the year finish\nStarting using data")
  for lessons in lessonsOfTheYear:

    if (lessons.status != None):
      #print("New event different from default timetable")
      numberOfEditedLessons = numberOfEditedLessons + 1
      idOfLessons = lessons.subject.name + lessons.start.strftime("%m/%d/%Y, %H:%M:%S") + lessons.end.strftime("%m/%d/%Y, %H:%M:%S")
      for editedLesson in editedLessons:
        if (editedLesson[0] == idOfLessons):
          twoTimeEvent = True
          editedLesson[1] = lessons
      if (twoTimeEvent == False):
        editedLessons.append([idOfLessons, lessons])
      else:
        #print("Two Time Events")
        twoTimeEvent = False
  print("Fetching event with database")
  for lesson in editedLessons:
    course = lesson[1]
    lessonsId = course.subject.name + " | " + course.status + " | " + course.start.strftime("%m/%d/%Y, %H:%M:%S") + " | " + course.end.strftime("%m/%d/%Y, %H:%M:%S")
    if (db.prefix(lessonsId) == ()):
      db[lessonsId] = "True"
      print(lessonsId)
      pushClient = Client(os.environ['apikey'])
      resp = pushClient.send_message("Bonjour " + os.environ['first_name'] +",\nUne modification de votre emploi du temps est apparu sur votre emploi du temps!\nLe cours suivant à été modifié:\n" +  course.subject.name + " du " + course.start.strftime("%d/%m/%Y à %H:%M:%S") + " pour le motif suivant: " + course.status + ".", "Modification de votre emploi du temps", os.environ['device_id'], os.environ['device_id'])
      print(resp)
  print("Using data finished")
