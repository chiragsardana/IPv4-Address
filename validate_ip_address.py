from ipaddress import IPv4Address, ip_address
class ValidateIPAddress:
    def validIPAddress(IP: str) -> str:
        try:
            print(IP);
            if type(ip_address(IP)) is IPv4Address:
                return "IPv4"; 
        except ValueError:
            return "Not an Valid IPv4 Address"