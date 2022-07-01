import ipaddress


class DecimalToOctal:
    def decimalToOctal(IP: str):
        x = IP.split('.');
        # print(x);
        # print(DecimalToOctal.decimalToOctalNo(int(x[0])));
        octalIP = str(DecimalToOctal.decimalToOctalNo(int(x[0])))+"."+str(DecimalToOctal.decimalToOctalNo(int(x[1])))+"."+str(DecimalToOctal.decimalToOctalNo(int(x[2])))+"."+str(DecimalToOctal.decimalToOctalNo(int(x[3])));
        return octalIP;
    def decimalToOctalNo(deciNum):
 
        # initializations
        octalNum = 0
        countval = 1
        dNo = deciNum
    
        while (deciNum != 0):
    
            # decimals remainder is calculated
            remainder = deciNum % 8
    
            # storing the octalvalue
            octalNum += remainder * countval
    
            # storing exponential value
            countval = countval * 10
            deciNum //= 8
    
        return octalNum;
