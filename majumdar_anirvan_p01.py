import sys
import re

def main(argv):
    
    if len(argv)<2:
        print "file not entered"
        return 0
    
    length=7
    minimum=4
    fp=None
    if argv[1].endswith(".tar.gz"):
        fp=open(argv[1],'rb')
    if argv[1].endswith(".txt"):
        fp=open(argv[1],'r')
    
        
    subtext=fp.read(length)
    i=1
    dict1={}
    list1=[]
    counter=0;
    total=0;
    while len(subtext)==length:
                
        if ord(subtext[0])<128:
            total+=ord(" ")
            if counter<=20:
                list1.append(subtext[0])
        
        if len(re.findall('[a-z]',subtext))>=minimum:
            if subtext in dict1:
                dict1[subtext]+=1
            else:
                dict1.update({subtext:1})            
        
        
        fp.seek(i)
        subtext=fp.read(length)
        i+=1
    
    for elem in subtext:
        if ord(elem)<128:
            total+=ord(" ")
            if counter<=20:
                list1.append(elem)
        
    fp.close()
    
    val=max(dict1, key=dict1.get)
    with open("majumdar_anirvan_p01.txt","w") as f:
        f.write("the number of unique 7-character strings with four or more ASCII characters is: "+str(len(dict1.keys())))
        f.write("\nthe most frequently occurring 7-character string is: " + val)
        f.write("\nthe first 20 mapped characters are: ")
        for elem in list1:
            f.write(elem + " ")
        f.write("\nthe sum of the decimal values of all characters after mapping is: " + str(total))
    
    
if __name__=="__main__":
    main(sys.argv[0:])
