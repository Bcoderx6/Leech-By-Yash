from tobrot.sample_config import Config
#Fill your all data, read readme for reference

class Config(Config):
    TG_BOT_TOKEN= "2063169401:AAFxvR0VsSAhNPsRSnl72Y8WJUkKCZ1uRPg"
    APP_ID = 7556621
    API_HASH = "0775c99530b756c6f652c8a9ee572aa8"
    OWNER_ID = 1263291513
    AUTH_CHANNEL = [-701661471]
    DESTINATION_FOLDER = "yash" #Name of your folder read readme(not id of the folder)
    RCLONE_CONFIG = """type = drive\nscope = drive\ntoken = {"access_token":"ya29.a0ARrdaM_YKvlvZxhCIaI3GpKF-xKB81bFo0G2QnfQk400vWaGrl1OsS8qyeET1UMMKj2563WwKlR4fLlN01BHGXDgIUtwiBQ6SlJmrKysx6jidXsUKIkYy3XQYL_0VzWFa8jqFfrhJN0Scxx7621e_KMPHrpa","token_type":"Bearer","refresh_token":"1//0gBkesInNepDSCgYIARAAGBASNwF-L9IrH8WguGJos7RxqLQm_eLMYmEoKeD73oGZXLdGTw3V6ePbV3Fz62bMJ-Mf_N6SNu84JIQ","expiry":"2021-11-06T14:28:02.9448117+05:30"}"""
    #fill taking reference of this config, dont remove """ from both side of the RCLONE_CONFIG variable 
    #FOR CUSTOM COMMANDS READ REAME AND FILL THEM...
