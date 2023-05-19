import random
import sqlite3

people = 39

def connection():
    conn = sqlite3.connect("crawl.db"); 
    return conn; 

def counter():
    conn = connection(); 
    cursor = conn.cursor(); 
    counter = cursor.execute("SELECT * FROM counter "); 
    counter = counter.fetchone(); 
    conn.commit(); 
    return counter

def prowl():
    varA = random.randint(1,5); 
    varB = random.randint(1,3); 
    output = varA - varB; 
    return output; 

def hunt(a):
    conn = connection(); 
    cursor = conn.cursor(); 
    data = cursor.execute("SELECT * FROM victims WHERE houseid = ?",(a,)); 
    data = data.fetchall(); 
    conn.commit(); 
    return data; 

def cantgoback(b):
    if b <= 0:
        b = 1; 
        return b; 
    else:
        return b; 

def getobituary():
    conn = connection(); 
    cursor = conn.cursor(); 
    data = cursor.execute("SELECT victim FROM obituary"); 
    data = data.fetchall(); 
    conn.commit(); 
    return data; 

def serial(d):
    victims = hunt(d); 
    global target
    target = iter(victims[0]); 
    result = next(target); 
    result = next(target); 
    return result

def endgame():
    conn = connection(); 
    cursor = conn.cursor(); 
    number = cursor.execute("SELECT COUNT (victim) FROM obituary")
    number = number.fetchone(); 
    victimnum = number[0]
    if victimnum == people:
        print("Everyone is dead."); 
        exit(); 
    else:
        print("The Hunt is over. The Crawler has left. It is safe, for now.")
        exit(); 

def lost(c):
    if c is None:
        global counter; 
        counter += 1; 
        if counter > 13:
            endgame(); 
        result = serial(counter); 
        lost(result); 
    elif c in obituaries:
        lost(next(target,None)); 
    else:
        print(str(c) + " has been eaten")
        conn = connection(); 
        cursor = conn.cursor(); 
        cursor.execute("INSERT INTO obituary (victim) VALUES (?)",(c,)); 
        cursor.execute("UPDATE counter SET count = ?",(counter,))
        conn.commit(); 




getobituary = getobituary(); 
obituaries = list(); 
for i in getobituary:
    for j in i:
        obituaries.append(j)

counter = (counter()[0]); 

result = counter + prowl(); 

irreversible=cantgoback(result); 
counter = irreversible; 

if counter > 13:
    endgame(); 

victim = serial(counter)
lost(victim); 

