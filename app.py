from flask import Flask, redirect, url_for, render_template, request  # import necessary libraries
from APPI import Arra
app = Flask(__name__)  # create an instance of Flask class

# Our_array = []  # Create an empty list/array to save the input integers
res = []
ourarray = Arra([])

# SplitArray function to split our array into to arrays with equal size if possible (this function is replaced by
# using the Arr class form APPI)
# def SplitArray1(Arr):
#     if not Arr:  # check to see if the array is empty
#         return "Array is empty"
#     if np.sum(Arr) % 2 == 0:  # check to see if the sum of array is an even number so if we can split it
#         halfOfSum = np.sum(Arr) / 2
#         sumofFirstElements = 0
#         for i in range(0, len(Arr)):
#             sumofFirstElements += Arr[i]
#             # print(Arr[i])
#             if sumofFirstElements > halfOfSum:
#                 return "spliting is not possible for this array"
#             if sumofFirstElements == halfOfSum:
#                 return [Arr[0:i + 1], Arr[i + 1:]]
#     else:  # if thearray sum is odd, we can not split it in two, because our elements are all integers
#         return "splitting is not possible"
#     return 0


# use the route() decorator to tell Flask what URL should trigger our function. include POST and GET methods to
# access input data
@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":  # if user submits an input(an integer to add to array)
        if request.form["val1"] == '':
            return render_template("index.html", content=res, content1=ourarray)  # if user doesn't input any data,
            # the client side will run the index.html
        val = int(request.form["val1"])  # get the input value of the user from client side
        # print(val)
        return redirect(url_for("result", rsr=val))  # redirects the client side to a new url
    return render_template("index.html", content=res,  content1=ourarray.arr)  # if user doesn't input any data, the
    # client side will run the index.html


# server functions that gets the user input from the client side and process the data to display the results
@app.route("/<rsr>")  # rsr is the input variable of this decorator
def result(rsr):
    # Our_array.append(int(rsr))  # appends the user input integer to our array
    # print(Our_array)
    ourarray.appendd(int(rsr))
    # res = SplitArray1(Our_array)    # call to the SplitArray1 function to process the array
    res = ourarray.spliit()
    return render_template("index.html", content=res, content1=ourarray.arr)   # displays the index.html file on client
    # side with given variables


if __name__ == "__main__":
    app.run()
