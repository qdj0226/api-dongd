import configparser

config = configparser.ConfigParser()
config.read(r"F:\project\api-dongd\config\email.ini",encoding="utf-8")
data = config.get("EMAIL","login_user")
