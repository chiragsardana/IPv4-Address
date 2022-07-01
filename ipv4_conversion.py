from decimal_to_binary import DecimalToBinary
from decimal_to_hexadecimal import DecimalToHexadecimal
from decimal_to_octal import DecimalToOctal


class IPv4Conversion:
    def ipv4Conversion(ipv4: list):
        # print("IPv4 Conversion");
        ipv4List = ["","","","","","","","","",""];
        # print(ipv4);
        for i in range(10):
            decimalIP = str(ipv4[int(i)]);
            # print(decimalIP);
            binaryIP = DecimalToBinary.decimalToBinary(IP=decimalIP);
            octalIP = DecimalToOctal.decimalToOctal(IP=decimalIP);
            hexadecimalIP = DecimalToHexadecimal.decimalToHexadecimal(IP=decimalIP);
            ipv4List[i] = decimalIP+", "+binaryIP+", "+octalIP+", "+hexadecimalIP;
        # print(ipv4List);
        return ipv4List;