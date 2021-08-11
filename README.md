# rest_apii
This is a simple example to develop a simple HTTP-based web site with REST API

The design of this work comprises of 2 parts:
•	Server or backend side
•	Client or user side
•	A module containing an array class with necessary functions
For the backend, I have used the flask library, which supports HTTP protocol. I initiate an object in the backend to save the user input data, manipulate the array, and display the results.
On the client side, the content of the array and the possibility of splitting the array are displayed. Also, to get the user input data, a number box is placed for the user to enter the desired integer in the form of an integer number. A button is placed below the input box for submitting the user input to the backend. 
The APPI module is used to handle the specific integer arrays defined for this task. It involves an appending and splitting method to add user input data and split the data array if possible.
The connection protocol between the server and the client is HTTP.

Algorithm efficiency:
For the array to be splittable, the sum of the array elements needs to be an even number. By checking this constraint, I avoid unnecessary calculations. Given the integer nature of the data and the rule prohibiting reordering:
•	Since in every call to the splitt method, The program only gets one integer added to the array, I start calculating the sum of all the elements by adding the new integer to the previous sum.
•	Then to find the right index for splitting, I calculate from the first index (0) by adding the new element to the variable sumofFirstElements and compare it with half of the total sum (halfOfSum) to check if I can find the right index for splitting.
•	This process terminates after the sum of data from the index 0 up to index i exceeds halfOfSum. Meaning the splitting is not possible. 
•	Since the user may enter negative integers, there is no easier way to determine the position of i based on the previous splitting index.
To run the code, preferably in PyCharm, create a new flask project. Replace the app.py file with the file provided. Add the APPI.py module to the same directory as the app.py file. Then create a templates folder and place the index.html file in it. After running the app.py code, you will get a URL. Copy the URL in your web browser application to test the code. 
Another option is to put the app.py and APPI.py file in a folder, e.g., ‘test.’ Create a new folder in the ‘test’ folder and name it ‘templates.’ Put the index.html file inside the ‘templates’ folder. Open the windows command prompt and Type in python app.py
File.py should include the directory of the app.py
Good Luck 😊
