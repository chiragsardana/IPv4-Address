

class DecimalToBinary:
    def decimalToBinary(IP: str):
        x = IP.split('.');
        # print(x);
        # print(DecimalToBinary.decimalToBinaryNo(x[0]));
        binaryIP = DecimalToBinary.decimalToBinaryNo(x[0])+"."+DecimalToBinary.decimalToBinaryNo(x[1])+"."+DecimalToBinary.decimalToBinaryNo(x[2])+"."+DecimalToBinary.decimalToBinaryNo(x[3]);
        # binaryIP = str(int(bin(x[0])[2:]))+"."+str(int(bin(x[1])[2:]))+"."+str(int(bin(x[2])[2:]))+"."+str(int(bin(x[3])[2:]))+".";
        return binaryIP;
    def decimalToBinaryNo(n):
        return "{0:b}".format(int(n))