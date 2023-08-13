import os
from dotenv import load_dotenv




#> invoking this function loads contents of the ".env" file into the script's environment...
load_dotenv() 

#to access to spotify api, you need client_id, client_secret
client_id = os.getenv("client_id")
client_secret =os.getenv("client_secret")