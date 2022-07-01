

class HexadecimalToDecimal:
    def hexadecimalToDecimal(IP: str):
        x = IP.split('.');
        print(x);
        print(HexadecimalToDecimal.hexadecimalToDecimalNo(x[1]));
        decimalIP = HexadecimalToDecimal.hexadecimalToDecimalNo(x[0])+"."+HexadecimalToDecimal.hexadecimalToDecimalNo(x[1])+"."+HexadecimalToDecimal.hexadecimalToDecimalNo(x[2])+"."+HexadecimalToDecimal.hexadecimalToDecimalNo(x[3]);
        return decimalIP;

    def hexadecimalToDecimalNo(hexadecimal):
        return str(int(hexadecimal, 16));