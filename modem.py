import subprocess
import os

def get_usb_modem():
    status, output = subprocess.getstatusoutput(
        "lsusb | grep 'Huawei'")
    if status:
        print("Modem not found. Please connect your USB modem and try again\n")
        input("Press any key to exit.")
        exit()
    return output

def check_dependencies():
    status, output = subprocess.getstatusoutput(
        "usb_modeswitch -v")
    if status:
        response = input(
            "usb modeswitch is not installed. Do you want to install it? (Y or N)")
        if response.lower() == 'y':
            os.system("apt-get install usb-modeswitch")
        else:
            print("Please install usb modeswitch")
            exit()
    return output

def main():
    output = get_usb_modem()
    check_dependencies()
    print("[OK] USB modeswitch installed..")
    print("[*]  Starting switch process")

    bus = output.split(" ")[1]
    device = output.split(" ")[3][:-1]
    os.system("sudo usb_modeswitch -v {} -p {} -M '55534243123456780000000000000011062000000100000000000000000000'".format(bus, device))
    print("[OK] Modem mode switch success")
    reboot = input(
        """The changes have been made to your Huawei E3551 USB modem. 
        Do you wish to reboot for changes to take place?(Y or N)""")
    os.system("reboot") if reboot.lower() == 'y' else exit()

if __name__ == "__main__":
    print("""
    _                              _ 
    | |__  _   _  __ ___      _____(_)
    | '_ \| | | |/ _` \ \ /\ / / _ \ |
    | | | | |_| | (_| |\ V  V /  __/ |
    |_| |_|\__,_|\__,_| \_/\_/ \___|_|
        E3531 modem mode switcher
    """)
    main() 