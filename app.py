from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Password generation function
def generate_password(length, upperBool, lowerBool, numBool, symBool):
    lowercase = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"] # list for lowercase letters
    uppercase =  ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"] # list for uppercase letters
    number = ["1","2","3","4","5","6","7","8","9","0"] # list for numbers
    symbol = ["~","`","!","@","#","$","%","^","&","*","(",")","_","-","+","=","{","[","}","]","|","\\",":",";","\"","'","<",",",">",".","?","/"] # list for symbols
    password = str() # initiates password string


    charAllowed = [] # initiates charAllowed list, contains what type of characters the user wants in the password
    if lowerBool == True: # if the user would like lowercase letters, adds lowercase letters to the pool of allowed character types
        charAllowed.append("lowerItem")
    if upperBool == True: # if the user would like uppercases letters, adds uppercases letters to the pool of allowed character types
        charAllowed.append("upperItem")
    if numBool == True: # if the user would like numbers, adds numbers to the pool of allowed character types
        charAllowed.append("numItem")
    if symBool == True: # if the user would like symbols, adds symbols to the pool of allowed character types
        charAllowed.append("symItem")
    
    if lowerBool == False and upperBool == False and numBool == False and symBool == False: # checks if all character types are disabled
        return("No character types permitted. Please try again.")
    else: # if at least one character type is allowed, run this code
        for i in range(length): # adds a random character of random character type for the length of the password
            charChosen = charAllowed[random.randint(0,len(charAllowed) - 1 )] # picks a type of character out of the pool that the user allows
            if charChosen == "lowerItem": 
                password = password + lowercase[random.randint(0,len(lowercase)-1)] # if it picks lowercase, add a lowercase letter to the password
            if charChosen == "upperItem":
                password = password + uppercase[random.randint(0,len(uppercase)-1)] # if it picks uppercase, add an uppercase letter to the password
            if charChosen == "numItem":
                password = password + number[random.randint(0,len(number)-1)] # if it picks number, add a number to the password
            if charChosen == "symItem":
                password = password + symbol[random.randint(0,len(symbol)-1)] # if it picks symbol, add a symbol to the password

    return password

@app.route('/', methods=['GET', 'POST'])
def index():
    password = ""
    upperBool = True
    lowerBool = True
    numBool = True
    symBool = True
    if request.method == 'POST':
        
        length = int(request.form['length'])
        
        # Get checkbox values (default to True if not checked)
        upperBool = 'uppercase' in request.form
        lowerBool = 'lowercase' in request.form
        numBool = 'numbers' in request.form
        symBool = 'symbols' in request.form
        
        password = generate_password(length, upperBool, lowerBool, numBool, symBool)
    
    return render_template('index.html', password=password,
                           upperBool=upperBool, lowerBool=lowerBool,
                           numBool=numBool, symBool=symBool)

if __name__ == '__main__':
    app.run(debug=True)