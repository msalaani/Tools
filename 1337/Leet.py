import sys

def help():
        print("""\nUsage program.py MESSAGE [-i | --indexes N11-N12--N21-N22--..--Nn1-Nn2]\nOr simply INPUT.""")  


charset = { "a":"4",
            "b":"6",
            "e":"3",
            "g":"9",
            "i":"1",
            "o":"0",
            "s":"5",
            "B":"8",
            " ":"_"
            }


def _to_1337(msg):
    out = list(msg)
    for i in range(len(msg)):
        try:
            out[i] = charset[out[i]]
        except:
            pass
    return "".join(out)


def to_1337(msg,indexes=[]):
    leet = msg
    if len(indexes) != 0:
        leet = list(leet)
        for i in range(len(indexes)):
            for k in range(indexes[i][0],indexes[i][1]):
                leet[k] = _to_1337(msg[k])
        leet = "".join(leet)
    
    else:
        leet = _to_1337(leet)
    
    return leet

def from_cmdline():
    
    #print ("the name of the program is", sys.argv[0]) 
    
    arguments = sys.argv[1:]
    if len(arguments) == 0:
        return None,[]

    try:

        msg = arguments[0]
        indexes = []

        i = 1
        while i < len(arguments) :
            arg = arguments[i]
            if arg == "-i" or arg == "--indexes" :
                i += 1
                arg = arguments[i]
                arg = arg.split("--")
                arg = [ (int(k.split("-")[0]),int(k.split("-")[1])) for k in arg ]
                indexes += arg
            else:
                if len(arguments) != 1:
                    exit(0)
            i += 1
        return msg,indexes
    except:
        help()
        exit(0)

def main():
    msg,indexes = from_cmdline()
    if msg != None:
        print(to_1337(msg,indexes))
    else:
        msg = input("MSG: ")
        indexes = input("INDEXES: ")
        if len(indexes) > 0:
            try:
                indexes = indexes.split("--")
                indexes = [ (int(k.split("-")[0]),int(k.split("-")[1])) for k in indexes ]
                print(to_1337(msg,indexes))
            except:
                help()
                exit(0)
        else:
            print(to_1337(msg))
    

if __name__ == "__main__":
    main()


