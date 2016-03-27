#Derek Thompson
#3/9/15
#A7: IP Addressing
#Purpose: Is to have an IP address and to cause the program to display information useful for that IP address.
#http://stackoverflow.com/questions/7844118/how-to-convert-comma-delimited-string-to-list-in-python used for spilting the ipaddress.


def returnClass(my_list): # This function will return what class the IP address is in.
 if int(my_list[0]) > 0 and int(my_list[0]) < 127:
      print "Class A"
 elif int(my_list[0]) > 126 and int(my_list[0]) < 192:
      print "Class B"
 elif int(my_list[0]) > 192 and int(my_list[0]) < 224:
     print "Class C"
 else:
     print "error"
     pass

def returnNetworkAddress(my_list): # This function will return the correct network address.
  if int(my_list[0]) >= 1 and int(my_list[0]) <= 126:
      my_list[1] = 0
      my_list[2] = 0
      my_list[3] = 0
      print ("Network Address " + str(my_list))
  elif int(my_list[0]) > 126 and int(my_list[0]) <= 191:
      my_list[2] = 0
      my_list[3] = 0
      print ("Network Address " + str(my_list))
  elif int(my_list[0]) > 192 and int(my_list[0]) <= 223:
     my_list[3] = 0
  else:
     print "error"
     pass

def returnValidRange(my_list): #this function will return the valid ranges for the IP address.
 if int(my_list[0]) >= 1 and int(my_list[0]) <= 126:
      my_list[3] = 1
      print ("Starting Valid range ") + str(my_list)
      my_list[3] = 254
      print ("Ending Valid Range ") + str(my_list)
 elif int(my_list[0]) > 126 and int(my_list[0]) <= 191:
      my_list[3] = 1
      print ("Starting Valid Range ") + str(my_list)
      my_list[3] = 254
      print("Ending Valid Range ") + str(my_list)
 elif int(my_list[0]) > 192 and int(my_list[0]) <= 223:
     my_list[3] = 1
     print("Starting Valid Range ")+ str(my_list)
     my_list[3] = 254
     print ("Ending Valid Range ") + str(my_list)
 else:
     print "error"
     pass

def returnBroadcastAddress(my_list): # this function will return the broadcast address.
 if int(my_list[0]) >= 1 and int(my_list[0]) <= 126:
      my_list[3] = 255
      print ("Broadcast Address ")+ str(my_list)
 elif int(my_list[0]) > 126 and int(my_list[0]) <= 191:
      my_list[3] = 255
      print ("Broadcast Address ")+ str( my_list)
 elif int(my_list[0]) > 192 and int(my_list[0]) <= 223:
     my_list[3] = 255
     print("Broadcast Address ") + str(my_list)
 else:
     print "error"

def testIP(my_list): #This function tests to see if the IP address is good or bad.
 if len(my_list) != 4:
    return False
 else:
    return True


def main():
    print('Welcome to the IP information station.')

    ip_address = raw_input("Please type in the IP address you would like to know about.")



    my_ipaddress = ip_address
    my_list = my_ipaddress.split(".")
    print my_list
    testresults = testIP(my_list)
    if testresults == True:
        answer = raw_input("Is this IP address classful or classless?")
        if answer == 'classful' or answer == 'Classful':

            returnClass(my_list);
            returnNetworkAddress(my_list);
            returnValidRange(my_list);
            returnBroadcastAddress(my_list);
            pass
        else:
            print "End Program!"

    else:
        pass

main()