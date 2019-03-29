def printInfo():
    print("-------------------------------||| MONSTERS AND SAINTS |||-----------------------------------")
    print("")
    print("Three Monsters [m1,m2,m3] and three Saints[s1,s2,s3] are trying to cross the river using a boat")
    print("The boat can carry at the max two passengers at a time, and the boat CANNOT row if its empty.")
    print("Help them cross the river!!!!!")
    print("However, the monsters and the saints have an understanding among them,")
    print( "If anywhere (either in source or destination), the number of monsters are more than number of saints,")
    print("then monsters will eat the saints and the game ends.")
    print("")
    print("---------------------------------------ALL THE BEST-----------------------------------------")
    print("")
	
def printStatus(source,dest,boat_loc,boat):
    if boat_loc == "s":
         print("==Source=="+str(source)+"<_"+str(boat)+"_>~~~~~~~~~~~~~~~~~"+str(dest)+"==Destination==")
    else:
        print("==Source=="+str(source)+"~~~~~~~~~~~~~~~~~<_"+str(boat)+"_>"+str(dest)+"==Destination==")    

def putInBoat(boat,p):
    boat.append(p)
	
def showBoat(boat,boat_loc):
    rowTo = ""
    if(len(boat)==0):
        print("you cant row with empty boat!!!")
        return False
    if(boat_loc == "s"):
        rowTo = "destination"
    else:
        rowTo = "source"
    print("your boat contains:-")
    print(boat)
    print("do you wish to row to "+rowTo+" ? (y/n)")
    ch = input("(y/n) - >")
    if(ch.lower() == "y"):
        return True
    else:
        return False
 
def checkGameEnd(source,dest):
    ms = source.count("m1")+source.count("m2")+source.count("m3")
    md = dest.count("m1")+dest.count("m2")+dest.count("m3")
    ss = source.count("s1")+source.count("s2")+source.count("s3")
    sd = dest.count("s1")+dest.count("s2")+dest.count("s3")
    if((ms>ss and ss!=0) or (md>sd and sd != 0)):
        return "dead"
    elif(md == 3 and sd == 3):
        return "won"
    else:
        return "continue"

def row(source,dest,boat,boat_loc):
    if(boat_loc == "s"):
        print("moving to dest"+str(len(boat)))
        for b in range(0,len(boat)):
            dest.append(boat[b])
        boat.clear()
        return("d")
    else:
        for b in range(0,len(boat)):
            source.append(boat[b])
        boat.clear()
        return("s")
		
def fillBoat(source,dest,boat,boat_loc):
    loop = True
    if(len(boat)>=2):
        print("boat is already full!! do you want to clear it?")
        cl = input("(y/n) - >")
        if(cl.lower() == "y"):
            if(boat_loc == "s"):
                for b in range(0,len(boat)):
                    source.append(boat[b])
                boat.clear()
            else:
                for b in range(0,len(boat)):
                    dest.append(boat[b])
                boat.clear()
        else:
            loop = False
            print("boat not cleared!")
    while(loop):
        print("enter boat passenger :")   
        p = input("->")
        p = p.lower()
        if(p in source or p in dest):
            if(boat_loc == "s"):
                if(p in source):
                    putInBoat(boat,p)
                    source.remove(p)
                else:
                    print("the passenger is not in source")
            else:
                if(p in dest):
                    putInBoat(boat,p)
                    dest.remove(p)
                else:
                     print("the passenger is not in destination")
            printStatus(source,dest,boat_loc,boat)
            if(len(boat) < 2):
                print("add another??(y/n)")
                ch = input("(y/n) - >")
                if(ch.lower() == "n"):
                    loop = False
            else:
                loop = False
        else:
            print("wrong input!!! try again")
			
def initGame():
    printInfo()
    source = ["m1","m2","m3","s1","s2","s3"]
    dest = []
    boat=[]
    boat_loc = "s"
    gameOn = True
    confirm = False
    while(gameOn):
        printStatus(source,dest,boat_loc,boat)
        while(not confirm):
            fillBoat(source,dest,boat,boat_loc)
            confirm = showBoat(boat,boat_loc)
        confirm = False
        boat_loc = row(source,dest,boat,boat_loc)
        chk = checkGameEnd(source,dest)
        if(chk=="won"):
            printStatus(source,dest,boat_loc,boat)
            print("Bravo!! you have completed the challenge!!!!!")
            gameOn = False
        elif(chk=="dead"):
            printStatus(source,dest,boat_loc,boat)
            print("help!!!!! monsters are eating the saints... you lost")
            gameOn = False
    

initGame()