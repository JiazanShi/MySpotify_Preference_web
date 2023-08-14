import os
from dotenv import load_dotenv




#> invoking this function loads contents of the ".env" file into the script's environment...
load_dotenv() 
## 
#to access to spotify api, you need client_id, client_secret
SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET =os.getenv("SPOTIPY_CLIENT_SECRET")