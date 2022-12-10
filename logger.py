from datetime import datetime as dt
from ui import ch

def add(ch):
    time = dt.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("log.txt", "a", encoding = 'UTF-8') as file:
        # file.write(f"{data}; {ch}; {time} \n")
        file.write(f"{ch}; {time} \n")

    
add(ch)

