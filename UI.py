class UI:
    def header():
        print("######################################");
        print("# Welcome to IPv4 Validator Program  #");
        print("######################################");
    def footer():
        print("######################################");
        print("####### By Chirag Sardana ############");
        print("######################################");
    def enterAllIpInDecimal():
        print("######################################");
        print("#  Enter All IPv4 in Decimal Format  #");
        print("######################################");
    def inputLine(no: int):
        print("######################################");
        if no is 10:
            print("#    Enter the Input IPv4 "+str(no)+" below   #");
        else:
            print("#    Enter the Input IPv4 "+str(no)+" below    #");
        print("######################################");
    def invalidInput():
        print("######################################");
        print("#   Invalid IP Address Enter Again!  #");
        print("######################################");
    def outputLine(no: str, toBePrinted: str):
        print("The "+str(no)+" IP address in Decimal, Binary, Octal and hexadecimal format is "+str(toBePrinted));
    def output(output: list):
        noList = ["first", "second", "third", "forth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"];
        print("######################################");
        print("#               Outputs              #");
        print("######################################");
        # print(output);
        for i in range(10):
            UI.outputLine(no=noList[i], toBePrinted=output[i]);
    
    