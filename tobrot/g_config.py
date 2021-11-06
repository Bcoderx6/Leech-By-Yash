from tobrot.sample_config import Config
#Fill your all data, read readme for reference

class Config(Config):
    TG_BOT_TOKEN= "2063169401:AAFxvR0VsSAhNPsRSnl72Y8WJUkKCZ1uRPg"
    APP_ID = 7556621
    API_HASH = "0775c99530b756c6f652c8a9ee572aa8"
    OWNER_ID = 1263291513
    AUTH_CHANNEL = [-701661471]
    DESTINATION_FOLDER = "yash" #Name of your folder read readme(not id of the folder)
    RCLONE_CONFIG = """type = drive\nscope = drive\ntoken = {"access_token":"ya29.a0ARrdaM9L9s7WtThZKaJVSv067JFbrwbBkN21zsltQPZ4cWBsCCAAaWS-hwmF9TA2veZt0LDMC695ix5067574F0albRMFw7aLfFyUrtqMX4jqPF5gTb5aFPW2SxEv5y4YEaYctf_4UGJU1dYFhm24ocOsNgJ","token_type":"Bearer","refresh_token":"1//0g5AM-27B_SHKCgYIARAAGBASNwF-L9IrY7cV86dqoEsjrVxOBjqCNWAK_e0982RA0Gjg9iCeyWtReDDsg5NaLEuUD8dytPnRr_w","expiry":"2021-11-06T14:44:30.7056398+05:30"}"""
    #fill taking reference of this config, dont remove """ from both side of the RCLONE_CONFIG variable 
    #FOR CUSTOM COMMANDS READ REAME AND FILL THEM...
