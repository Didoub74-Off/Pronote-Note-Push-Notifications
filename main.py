import os
import pronotepy
from time import sleep
from functions.send_marks import marks
from functions.send_lessons import lessons
if True == True:
    try:
      client = pronotepy.Client(
          os.environ['url'],
          username=os.environ['username'],
          password=os.environ['password'])
    except Exception:
      quit("Une erreur est survenue lors de l'éxecution du programme -> sûrement de mauvais identifiants.\n")
      
    # check if sucessfully logged in
    if not client.logged_in:
        print("Client is not logged in")
        exit()
    else:
        print("Logged In")
    while True:  # infinite loop
        if (1 == 1):
            marks(client)
            lessons(client)
        print("Program go sleep for 5min\n-------------------")          
        sleep(300)