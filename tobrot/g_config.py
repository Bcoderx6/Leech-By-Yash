from tobrot.sample_config import Config
#Fill your all data, read readme for reference

class Config(Config):
    TG_BOT_TOKEN= "2025975336:AAFyFrU2FuaIluETcoLUQpVsorY85-_bUlw"
    APP_ID = 7556621
    API_HASH = "0775c99530b756c6f652c8a9ee572aa8"
    OWNER_ID = 1263291513
    AUTH_CHANNEL = [-1001539450185]
    DESTINATION_FOLDER = "yash" #Name of your folder read readme(not id of the folder)
    RCLONE_CONFIG = """type = drive\nscope = drive\ntoken = {"access_token":"ya29.a0ARrdaM9hPbVwW4J3PtojsVWf6CJ_r5AMPSZm6k4SPhG5NSCdmnw5uQxr5swB0fycsrjMpCWOjZ84OeweE90ARX5OnBx0h7gb6qKVEtUFXJu5q1IGicN-DU659wzVnk5tFscp0aqMpEKLFQkdEYpNiPxwRblg","token_type":"Bearer","refresh_token":"1//0gv-Pw39MvGoVCgYIARAAGBASNwF-L9IrQ_kYvDYAUWpecLeacjQ-4GuK-Dai88RNtKgjwdVgQy7Ap53w8Jq43D7WcnbYteFyZcA","expiry":"2021-11-06T15:49:16.9309253+05:30"}"""
    #fill taking reference of this config, dont remove """ from both side of the RCLONE_CONFIG variable 
    #FOR CUSTOM COMMANDS READ REAME AND FILL THEM...
