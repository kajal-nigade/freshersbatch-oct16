import smtplib
import random
import time

user_email = 'youremailaddress@email.com'
user_pw = 'yourpassword'

emails = ['email1@yahoo.com',
          'email2@yahoo.com',
          'email3@gmail.com',
          'email4@gmail.com']

def assignment():
    chores = ['Wash the dishes',
              'Mop the floor',
              'Walk the dog',
              'Feed the cat',
              'Clean toilet',
              'Mow the lawn',
              'Clean the kitchen']
    for email in emails:
        random_chore = random.choice(chores)
        email_dict[email] = random_chore
        chores.remove(random_chore)
    for email in email_dict:
        message = str('Subject: Your random chore is....\n' + email_dict[email])
        print(email.ljust(27) + ' is assigned: ' + email_dict[email].rjust(23))
        smtp_obj.sendmail(user_email, email, message)

email_dict = {}

smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
smtp_obj.ehlo()
smtp_obj.starttls()
smtp_obj.login(user_email, user_pw)

for i in range(7):
    assignment()
    time.sleep(86400)

smtp_obj.quit()