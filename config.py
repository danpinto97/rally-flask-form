import os
import json


#config for flask forms
class Config(object):
    f = open("credentials.json")
    creds = json.load(f)
    SECRET_KEY = creds['flask_credentials']["form_creds"]

#config for postgres db
class ConfigDb(object):
    def __init__(self):
        f = open("credentials.json")
        creds = json.load(f)
        db_host = creds['db_credentials']["db_host"]
        db_name = creds['db_credentials']["db_name"]
        db_user = creds['db_credentials']["db_user"]
        db_pass = creds['db_credentials']["db_pass"]
        db_port = creds['db_credentials']["db_port"]
        self.conn = psycopg2.connect(database= db_name, user= db_user, password= db_pass, host= db_host, port= db_port)
