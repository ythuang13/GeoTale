# GeoTale

## General Info
NOTE: Our program requires our AWS server to be up and running for proper functionality. Please contact @Gr8Dan to organize
a testing period.

GeoTale is a simple audio file sharing program that allows users to upload and download short audio files. Its intention
is to be a story-sharing app allows users to share stories based on geolocation (based on zip code). Stories and
properties are stored on an AWS-hosted server. Story properties (zip code, author, title, description, length) are 
stored in a SQL server. Users are to be able to upload a file, see what files are on the server, and download files to play them
on their local machine.

## Version 2 change log:

1. Added custom cursor
2. update home button
3. refactor server.py
4. refactor guiState.py
5. update README.md
6. add requirements.txt
7. flip through list display with up and down button
8. remove tqdm library (progerss bar)
9. handle value error from data validation
10. display error with a pop up window
11. limit field length for data entry
12. handle lost connection
13. display no connection page
14. after insertion, jump back to menu
15. query all story by submit empty zip code for search
   