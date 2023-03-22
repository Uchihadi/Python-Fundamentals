#1st try
try:
    hello_file=open("flight.txt","w")
    text="Hello everyone! Welcome"
    hello_file.write(text)
except:
    print("Error occurred, not able to write to file")
finally:
    hello_file.close()
try:
    hello_file=open("flights.txt","r") #Wrong spelling of flights.txt
    text_from_file=hello_file.read()
    print(text_from_file)
except:
    print("Error Occurred, not able to read from file")
finally:
    hello_file.close()

#2nd try
try:
    hello_file=open("flight.txt","w")
    text="Hello everyone! Welcome"
    hello_file.write(text)
except:
    print("Error occurred, not able to write to file")
finally:
    hello_file.close()
try:
    hello_file=open("flight.txt","r")
    text_from_file=hello_file.read()
    print(text_from_file)
except:
    print("Error Occurred, not able to read from file")
finally:
    hello_file.close()