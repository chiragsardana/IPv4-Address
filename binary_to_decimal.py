

class BinaryToDecimal:
    def binaryToDecimal(IP: str):
        x = IP.split('.');
        print(x);
        # print(BinaryToDecimal.binaryToDecimalNo(int(x[0])));

        decimalIP = str(BinaryToDecimal.binaryToDecimalNo(int(x[0])))+"."+\
        BinaryToDecimal.binaryToDecimalNo(int(x[1]))+"."+\
        BinaryToDecimal.binaryToDecimalNo(int(x[2]))+"."+\
        BinaryToDecimal.binaryToDecimalNo(int(x[3]));
        return decimalIP;
    def binaryToDecimalNo(binary):
        binary1 = binary
        decimal, i, n = 0, 0, 0
        while(binary != 0):
            dec = binary % 10
            decimal = decimal + dec * pow(2, i)
            binary = binary//10
            i += 1
        # print(decimal)
        return str(decimal);