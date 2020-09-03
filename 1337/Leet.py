import sys

def help():
        print("""
        Usage python3 leet.py MESSAGE 
        Options:    [ -iL | --LeetIndexes  N11-N12--N21-N22--..--Nn1-Nn2 ]
                    [ -iA | --AvoidIndexes N11-N12--N21-N22--..--Nn1-Nn2 ]
        Or simply INPUT.
        
        == By Melek Salaani ==
        """)  

def split_indexes(indexe,BigSep="--",LitSep="-"):
    if len(indexe) == 0:
        return []
    indexes = indexe.strip()
    indexes = indexes.split(BigSep)
    indexes = [ (int(k.split(LitSep)[0]),int(k.split(LitSep)[1])) for k in indexes ]
    return indexes

charset = { "a":"4",
            "e":"3",
            "i":"1",
            "o":"0",
            "s":"5",
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


def to_1337(msg,indexes=[],indexes_to_avoid=[]):
    leet = msg
    if len(indexes) != 0:
        leet = list(leet)
        for i in range(len(indexes)):
            for k in range(indexes[i][0],indexes[i][1]):
                leet[k] = _to_1337(msg[k])
        print(indexes,leet)
        leet = "".join(leet)
        print(leet)
    
    if len(indexes_to_avoid) != 0:
        print("hey")
        leet = list(leet)
        ind = [i for i in range(len(leet))]
        for i in range(len(indexes_to_avoid)):
            for k in range(indexes_to_avoid[i][0],indexes_to_avoid[i][1]):
                ind.remove(k)
        for i in ind:
            leet[i] = _to_1337(leet[i])
        leet = "".join(leet)

    else:
        leet = _to_1337(leet)
    
    return leet

def from_cmdline():
    
    #print ("the name of the program is", sys.argv[0]) 
    
    arguments = sys.argv[1:]
    if len(arguments) == 0:
        return None,[],[]

    try:

        msg = arguments[0]
        indexes_for_leet = []
        indexes_to_avoid = []

        i = 1
        while i < len(arguments) :
            arg = arguments[i]
            if arg == "-iL" or arg == "--LeetIndexes" :
                i += 1
                arg = arguments[i]
                arg = split_indexes(arg)
                indexes_for_leet += arg
            elif arg == "-iA" or arg == "--AvoidIndexes":
                i += 1
                arg = arguments[i]
                arg = split_indexes(arg)
                indexes_to_avoid += arg
            else:
                if len(arguments) != 1:
                    exit(0)
            i += 1
        return msg,indexes_for_leet,indexes_to_avoid
    except:
        help()
        exit(0)

def main():
    msg,indexes_for_leet,indexes_to_avoid = from_cmdline()
    if msg != None:
        print(to_1337(msg,indexes_for_leet,indexes_to_avoid))
    else:
        msg = input("MSG: ")
        indexes_for_leet = input("INDEXES FOR LEET: ")
        indexes_to_avoid = input("INDEXES TO AVOID: ")
        if len(indexes_for_leet) > 0 or len(indexes_to_avoid) > 0:
            try:
                indexes_for_leet = split_indexes(indexes_for_leet)
                indexes_to_avoid = split_indexes(indexes_to_avoid)
                print(indexes_to_avoid,indexes_for_leet)
                print(to_1337(msg,indexes_for_leet,indexes_to_avoid))
            except:
                help()
                exit(0)
        else:
            print(to_1337(msg))
    

if __name__ == "__main__":
    main()

