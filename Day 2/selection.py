def display(num):
    if num%3==0 and num%5==0:
        message="Zoom"
    elif num%3==0:
        message="Zip"
    elif num%5==0:
        message="Zap"
    else:
        message="Invalid"
    return message

number=15
msg=display(number)
print(msg)