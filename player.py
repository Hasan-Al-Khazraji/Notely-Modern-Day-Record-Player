#!/sr/bin/env python
#The following is sample code of a local database
#The rest has been uploaded to a cloud database
#If coded is needed email: hasanwatheq2014@gmail.com
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from time import sleep

DEVICE_ID="ID-HERE"
CLIENT_ID="ID-HERE"
CLIENT_SECRET="TOKEN-HERE"

while True:
    try:
        reader=SimpleMFRC522()
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                       client_secret=CLIENT_SECRET,
                                                       redirect_uri="http://localhost:8080",
                                                       scope="user-read-playback-state,user-modify-playback-state"))
        
        # create an infinite while loop that will always be waiting for a new scan
        while True:
            print("Waiting for record scan...")
            id= reader.read()[0]
            print("Card Value is:",id)
            sp.transfer_playback(device_id=DEVICE_ID, force_play=False)
            
            # DONT include the quotation marks around the card's ID value, just paste the number
            if (id==29484067731):
                
                # playing a song
                sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:6Czb2BTCg2CMjbKFYNGTap'])
                sleep(2)
            
            # 2. "The Box"
            elif (id==302919068552):
                
                # playing a song
                sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:0nbXyq5TXYPCO7pr3N8S4I'])
                sleep(2)
            
            # 3. "Blinding Lights"
            elif (id==163701861236):
                
                # playing a song
                sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:0VjIjW4GlUZAMYd2vXMi3b'])
                sleep(2)
                
            # 4. "Starboy"
            elif (id==98102881161):
                
                # playing a song
                sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:7MXVkk9YMctZqd1Srtv4MB'])
                sleep(2)
            
            # 5. "No Role Modelz"
            elif (id==508507138907):
                
                # playing a song
                sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:68Dni7IE4VyPkTOH9mRWHr'])
                sleep(2)
            
            # 6. "Snow On Tha Bluff"
            elif (id==165782170615):
                
                # playing a song
                sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:1oOEkBNp4zWnkD7nWjJdog'])
                sleep(2)
            
            # 7. "Wants and Needs"
            elif (id==372997499847):
                
                # playing a song
                sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:65OVbaJR5O1RmwOQx0875b'])
                sleep(2)
            
            # 8. "Forever Set In Stone"
            elif (id==575934770134):
                
                # playing a song
                sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:2eG49TEm56KszFmCLOM5PK'])
                sleep(2)
            
            # 9. "wonderful"
            elif (id==507315956512):
                
                # playing a song
                sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:1cZlBZwnwGPtYeRIeQcoFh'])
                sleep(2)
            
            # 10. "Big Poppa"
            elif (id==575564819449):
                
                # playing a song
                sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:4sGylyGhQaOzhi77fLrMmP'])
                sleep(2)
            
            # continue adding as many "elifs" for songs/albums that you want to play

    # if there is an error, skip it and try the code again (i.e. timeout issues, no active device error, etc)
    except Exception as e:
        print(e)
        pass

    finally:
        print("Cleaning  up...")
        GPIO.cleanup()