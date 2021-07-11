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


    def PrintAll(self):
        print(self.name)
        print(self.age)
        print(self.gender)
        print(self.race)
        print(self.state)
        print(self.edu)
        print(self.discord)
        print(self.media)
        print(self.investingtime)

        print(self.followers)
        print(self.contenttime)
        print(self.postcount)
        print(self.ppw)
        print(self.lastpostdate)
        print(self.charts_displays)
        print(self.screenrec)
        print(self.qanda)
        print(self.livetrading)
        print(self.avgpostlength)

        print(self.usereng)
        print(self.disceng1)
        print(self.tceng1)
        print(self.tweng1)
        print(self.reng1)
        print(self.othereng1)
        print(self.disceng2)
        print(self.tceng2)
        print(self.tweng2)
        print(self.reng2)
        print(self.othereng2)
