from configparser import  ConfigParser

# intailize the config parser
config=ConfigParser()

# read the config file
config.read("EnvironmentDetails.cnf")

#Print the sections
print(config.sections())

print(config.get('QA','url'))