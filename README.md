# Log-in-sign-up-project
About:

This is a user authentification system. There is a log-in page, sign-up page, forgot password page, and an empty page for the project.
I have used Tkinter for the user interface, sqlite3 for the database, OS module for switching between windows, pillow module for setting up the background image, and 're' package from Regex module for email authentification.

Working in brief:

Sign Up page-

There are labels like name, email, username, password, security question etc, and then there are corresponding text boxes for the user to enter the response.
At the end of the page, there are 3 buttons, submit, clear and log in. All three buttons have been bound to their respective functions.

1) Submit- It is bound to a function called validate_all( ). I have defined the validate_all( )function in such a way that it consists of multiple if-else conditional statements that authenticate the user response. Like, say, for example, it checks that the user doesn't keep any field blank, if mobile number is 10 digit, if password and confirm-password both match, if the email/username/phone isn't already registered in the database etc. In the end, if all the conditions are satisfied, I have called another function named store( ). (store() function is called within the validate_all() function). I have defined the store( ) function in such a way that when it is called, it opens a database file (.db) on the computer and stores the user response. 

2) Clear- This button is bound to a function called clear_all( ). It is defined in such a way, tha using .set, all the text boxes are cleared, i.e. set to blank.
 
3) Log in-  This button has been bound to a function called call_newscreen( ). It is defined using OS module, and it closes the current window and opens new one. I have defined several call_newscreen( ) functions throughout the programme, for each page. This particular one n this case, closes the sign up page and opens the log in page.


Log in page-

There are two textboxes, one for the user to enter username/email/ and another one to enter password. At the end thereare 3 buttons. A submit button, and two buttons for jumping to different page, i.e. sign up and forgot password page.

1) Submit- This button is bound to a function named login_val( ). It is defined in such a way, that first, using sqlite3 code, it connects to the database file on which the user data is stored. Then cross verifies the  email/username and password entered by the user with the database. If the entered response matches with the user-data in the database then at this point I have called call_newscreen( ) function which closes the log in page and opens the project page. If the data doesnt match then a messagebox pops up saying 'error, try again'. The messagebox are part of the tkinter module.

2) Sign up and Forgot password- Both these buttons are attached to the repective call_newscreen( ) functions which close the log in page and open the respective pages.

Forgot Password page -

