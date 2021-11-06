from tobrot.sample_config import Config
#Fill your all data, read readme for reference

class Config(Config):
    TG_BOT_TOKEN= "2063169401:AAFxvR0VsSAhNPsRSnl72Y8WJUkKCZ1uRPg"
    APP_ID = 7556621
    API_HASH = "0775c99530b756c6f652c8a9ee572aa8"
    OWNER_ID = 1263291513
    AUTH_CHANNEL = [-701661471]
    DESTINATION_FOLDER = "yash unlimited" #Name of your folder read readme(not id of the folder)
    RCLONE_CONFIG = """type = drive\nscope = drive\ntoken = {"access_token":"ya29.a0ARrdaM-FI1QPcXFCJDYhpD8hqQyYPhUYMrJLuSiggSEtGz-Zkl3k19iK6PAyhdPwYfXGc2giSaxzGAU1SINDxO43w1HPMq0w30ogtHZuX_dtMkXqbJHKkjnIntz8HNOsl7BJgU6GFID3m1IaCPf4LA_9vyip","token_type":"Bearer","refresh_token":"1//0gmrUoML28wmkCgYIARAAGBASNwF-L9Ir9W2wTuQ_2AuWavGjAZL3ORjhnK5nbdfH-XhV4ATlYB2jjVtMV55q9dSa5VIZURkje8E","expiry":"2021-11-05T12:54:20.8695475+05:30"}"""
    #fill taking reference of this config, dont remove """ from both side of the RCLONE_CONFIG variable 
    #FOR CUSTOM COMMANDS READ REAME AND FILL THEM...
