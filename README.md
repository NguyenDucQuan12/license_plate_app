# license_plate_app
## First
You need to download the following video and rename it to: `demo`.  
Link to download [Here](https://www.youtube.com/watch?v=o4bRh9zzJaU)  
Then put in `demo folder`
## Second
change your server, database, username, password database and your driver ODBC in `license_plate_DB.py`
*If you don't have an account or don't want to log in, it will take about 15 seconds to start the software because it can't connect to the database.*

### Currently the software is having many errors and performance issues. We look forward to receiving contributions and advice from everyone
* If you press the quick_view button, a new window will appear for easy viewing by others, however it is causing an error that one of the first two cameras in the main window will freeze the image.
* There is a RAM leak with frequency increasing by 0.1% in 1 minute, I think this problem is due to using cv2
* When packaging with auto-py-to-exe, using the card swipe function for the first time will cause the application to reopen again.

