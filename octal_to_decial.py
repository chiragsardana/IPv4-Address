import ipaddress


class OctalToDecimal:
    def OctalToDecimal(IP: str):
        x = IP.split('.');
        print(x);
        print(OctalToDecimal.octalToDecimalNo(int(x[0])));
        decimalIP = str(OctalToDecimal.octalToDecimalNo(int(x[0])))+"."+str(OctalToDecimal.octalToDecimalNo(int(x[1])))+"."+str(OctalToDecimal.octalToDecimalNo(int(x[2])))+"."+str(OctalToDecimal.octalToDecimalNo(int(x[3])));
        return decimalIP;

    def octalToDecimalNo(n):
 
        num = n
        dec_value = 0
    
        # Initializing base value
        # to 1, i.e 8^0
        base = 1
    
        temp = num
        while (temp):
    
            # Extracting last digit
            last_digit = temp % 10
            temp = int(temp / 10)
    
            # Multiplying last digit
            # with appropriate base
            # value and adding it
            # to dec_value
            dec_value += last_digit * base
    
            base = base * 8
    
        return dec_value
