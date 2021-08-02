from werkzeug.utils import secure_filename
from psycopg2.extras import execute_values
import os
import psycopg2
import json

def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

class BasicSubmission(object):
    def __init__(self, form_answers):
        #Profile
        self.name = form_answers.get("name")
        self.age = form_answers.get("age")
        self.gender = form_answers.get("gender")
        self.race = form_answers.get("race")
        self.state = form_answers.get("state")
        self.edu = form_answers.get("edu")
        self.discord = form_answers.get("discord")
        self.media = form_answers.get("media")
        self.investingtime = form_answers.get("investingtime")

        #Current Content
        self.followers = form_answers.get("followers")
        self.contenttime = form_answers.get("contenttime")
        self.postcount = form_answers.get("postcount")
        self.ppw = form_answers.get("ppw")
        self.lastpostdate = form_answers.get("lastpostdate")
        self.charts_displays = form_answers.get("charts_displays")
        self.screenrec = form_answers.get("screenrec")
        self.qanda = form_answers.get("qanda")
        self.livetrading = form_answers.get("livetrading")
        self.avgpostlength = form_answers.get("avgpostlength")

        #User Engagement
        self.usereng = form_answers.get("usereng")
        #Engagement Platforms
        self.disceng1 = form_answers.get("disceng1") #Discord
        self.tceng1 = form_answers.get("tceng1")    #Twitch
        self.tweng1 = form_answers.get("tweng1")    #Twitter
        self.reng1 = form_answers.get("reng1")      #Reddit
        self.othereng1 = form_answers.get("othereng1")  #Other
        #Most Popular Engagement Platform
        self.disceng2 = form_answers.get("disceng2")
        self.tceng2 = form_answers.get("tceng2")
        self.tweng2 = form_answers.get("tweng2")
        self.reng2 = form_answers.get("reng2")
        self.othereng2 = form_answers.get("othereng2")

    def AddImage(self, file):
        UPLOAD_FOLDER = '/'
        self.filename = secure_filename(file.filename)
        self.file = file

    def ValidateFile(self, file):
        #print("allowed, saving")
        self.AddImage(file)

class InternalFormSubmission(object):
    def ConnectDb(self):
        f = open("credentials.json")
        creds = json.load(f)
        db_host = creds['db_credentials']["db_host"]
        db_name = creds['db_credentials']["db_name"]
        db_user = creds['db_credentials']["db_user"]
        db_pass = creds['db_credentials']["db_pass"]
        db_port = creds['db_credentials']["db_port"]
        conn = psycopg2.connect(database= db_name, user= db_user, password= db_pass, host= db_host, port= db_port)
        return conn

    def __init__(self, form_answers):
        self.original_form = form_answers
        self.name = form_answers.get("name")
        self.dob = form_answers.get("dob")
        #self.meeting = form_answers.get("meeting")
        self.grad = form_answers.get("grad")

    def PrintAll(self):
        print(form_answers)

    def SubmitAnswers(self):
        conn = self.ConnectDb()
        cur = conn.cursor()
        #If user already exists do nothing (don't insert) maybe want to update it instead?
        cur.execute("INSERT INTO survey_model_001.users (username) VALUES (%s) ON CONFLICT DO NOTHING", (self.name,))
        conn.commit()
        cur.execute("SELECT * FROM survey_model_001.users WHERE username = %s", (self.name,))
        user = cur.fetchone()
        user_id = user[0]
        execute_values(cur,
            "INSERT INTO survey_model_001.answers (user_id, question_option_id, answer_numeric, answer_text, answer_yn) VALUES %s",
            [(user_id, 1, 1, self.name, False), (user_id, 2, 1, self.dob, False), (user_id, 5, 1, 1, self.grad)])
        conn.commit()
        conn.close()
