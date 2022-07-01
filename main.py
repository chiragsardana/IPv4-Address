from UI import UI
from binary_to_decimal import BinaryToDecimal
from decimal_to_binary import DecimalToBinary
from decimal_to_hexadecimal import DecimalToHexadecimal
from decimal_to_octal import DecimalToOctal
from hexadecimal_to_decimal import HexadecimalToDecimal
from input_taker import InputTaker
from ipv4_conversion import IPv4Conversion
from octal_to_decial import OctalToDecimal
from read_file import ReadFile
from save_to_file import SaveToFile
from validate_ip_address import ValidateIPAddress;


class Main:
    UI.header();
    UI.enterAllIpInDecimal();
    # print(ValidateIPAddress.validIPAddress(IP='01100111.01011011.01001011.10101001'))
    # print(DecimalToBinary.decimalToBinary(IP='103.91.75.169'))
    # print(DecimalToOctal.decimalToOctal(IP='103.91.75.169'))
    # print(DecimalToHexadecimal.decimalToHexadecimal(IP='103.91.75.169'))
    # print(BinaryToDecimal.binaryToDecimal('1100111.1011011.1001011.10101001'));
    # print(OctalToDecimal.OctalToDecimal('147.133.113.251'));
    # print(HexadecimalToDecimal.hexadecimalToDecimal('67.5B.4B.A9'));
    # print(ValidateIPAddress.validIPAddress(IP='01100111.01011011.01001011.10101001'))
    # UI.inputLine(no=2);
    ipv4List = InputTaker.inputTaker();
    
    # print()
    # print(ipv4List);
    outputToBeWrittenOnFile = IPv4Conversion.ipv4Conversion(ipv4=ipv4List);
    # print(outputToBeWrittenOnFile);
    SaveToFile.saveToFile(output=outputToBeWrittenOnFile);
    outputReaded = ReadFile.readFile();
    # print(outputReaded);
    UI.output(output=outputReaded);
    UI.footer();

