from ast import IsNot
from telnetlib import IP
from UI import UI
from validate_ip_address import ValidateIPAddress


class InputTaker:
    def inputTaker():
        ipv4List = ["","","","","","","","","",""];
        for i in range(10):
            UI.inputLine(i+1);
            ipAddress = InputTaker.inputIPv4Address();
            while ValidateIPAddress.validIPAddress(IP = ipAddress) != "IPv4":
                UI.invalidInput();
                UI.inputLine(i+1);
                ipAddress = InputTaker.inputIPv4Address();
            ipv4List[i] = ipAddress;
        # print(ipv4List);
        return ipv4List;

    def inputIPv4Address():
        ipAddress = input('-->');
        return ipAddress;
    

