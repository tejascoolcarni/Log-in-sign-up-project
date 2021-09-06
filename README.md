# log-in-sign-up-project

About:

This is a user authentification system. There is a log-in page, sign-up page, forgot password page, and an empty page for the project.
I have used Tkinter for the user interface, sqlite3 for the database, OS module for switching between windows, pillow module for setting up the background image and Regex module for email authentification.

Note: Download all files and store them in a single folder. Open the sign up page and test it!

Working in brief:

Sign Up page -

There are labels like name, email, username, password, security question etc, and then there are corresponding text boxes for the user to enter the response.
At the end of the page, there are 3 buttons, 'submit', 'clear' and 'log in'. All three buttons have been bound to their respective functions.

1) Submit - It is bound to a function called validate_all( ). I have defined the validate_all( )function in such a way that it consists of multiple if-else conditional statements that authenticate the user response. Like, say, for example, it checks that the user doesn't keep any field blank, if mobile number is 10 digit, if password and confirm-password both match, if the email/username/phone isn't already registered in the database etc. In the end, if all the conditions are satisfied, I have called another function named store(). ( store() function is called within the validate_all() function ). I have defined the store( ) function in such a way that when it is called, it opens a database file (.db) on the computer and stores the user response. 

2) Clear - This button is bound to a function called clear_all( ). It is defined in such a way, tha using .set, all the text boxes are cleared, i.e. set to blank.
 
3) Log in -  This button has been bound to a function called call_newscreen( ). It is defined using OS module, and it closes the current window and opens new one. I have defined several call_newscreen( ) functions throughout the programme, for each page. This particular one in this case, closes the sign up page and opens the log in page.


Log in page -

There are two textboxes, one for the user to enter username/email/ and another one to enter password. At the end there are 3 buttons. A submit button, and two buttons for jumping to different page, i.e. sign up and forgot password page.

1) Submit - This button is bound to a function named login_val( ). It is defined in such a way, that first, using sqlite3 code, it connects to the database file on which the user data is stored. Then cross verifies the  email/username and password entered by the user with the database. If the entered response matches with the user-data in the database then at this point I have called call_newscreen( ) function which closes the log in page and opens the project page. If the data doesnt match then a messagebox pops up saying 'error, try again'. The messagebox is part of the tkinter module.

2) Sign up and Forgot password- Both these buttons are attached to the repective call_newscreen( ) functions which close the log in page and open the respective pages.

Forgot Password page -

There are 2 sections on this page. 

First section

It has a textbox for the user to enter their email or username and below that is the verify button.

1) Verify button - This button is bound to function named verify(). The verify function first connects to the database and cross checks if a user with the credentials entered in the textbox exists. If yes, then it fetches the security question selected by that user at the time of sign up, and stores it in a variable 'a'. The variable 'a' is configured in the label in second section where security question is displayed. If the user with the credentials entered in the textbox doesn't exist then a messagebox is displayed stating the same.

Second Section

It has a label where security question is displayed. Subsequently there are three textboxes, first to enter the answer to the security question, second to enter the new password, third to enter the new password again. After that, there is a submit button and at the very bottom there are two buttons named sign up and log in.

1) Submit Button - This button is bound to function named reset( ). This button has set of if-else conditional statements to verify conditions like say, for example, if the password and confirm password inputs are matching, if the password length is greater than 4 characters, if none of the textboxes are kept empty etc. It also connects to the databse and verifies if the answer to the security question matches with the answer stored in the database. If it does, the old password stored in the datbase is replaced by the the new password entered by the user and a messagebox saying "password reset successfully!" is displayed.

2) Log in and Sign Up - These two buttons are bound to their respective call_newscreen( ) function as explained above. Log in button closes the current page opens log in page, sign up button closes the current page opens sign up page.

This programme works with lots of user inputs, which means there are chances of errors and wrong inputs by users. I have tried to include as many test cases as possible. Try this project and let me know your views!

This was the overall working of this project in brief, if you have any doubts, suggestions or you find any bugs you can always ping me on tejascoolcarni@gmail.com !
