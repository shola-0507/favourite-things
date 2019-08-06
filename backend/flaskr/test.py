from flaskr.system.config import config

print("mysql+pymysql://" + config["database"]["sql"]["user"] + ":" + config["database"]["sql"]["pass"] + "@"
      + config["database"]["sql"]["host"] + ":" + config["database"]["sql"]["port"]
      + "/" + config["database"]["sql"]["name"])
