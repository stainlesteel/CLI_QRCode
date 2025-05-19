import qrcode
import validators
import tkinter
from tkinter import filedialog
import qrcodeT
from wifi_qrcode_generator import wifi_qrcode
from pyzbar.pyzbar import decode
from PIL import Image
import cv2
import webbrowser

def url():
   while True:
     link = input("Please enter a url (/w https://)")
     
     if not validators.url(link):
        print("Incorrect URL try again")
        continue
     else:
        print("successful")
        kr = qrcode.make(link)
        bit = int(input("How should I distribute the QR Code? (1. print it now), (2. save to a file): "))
        match bit:
            case 1:
                qrcodeT.qrcodeT(link) 
                print("The QR Code has been printed to the console.")
            case 2:
                print("Where should I save this to?")
                tkinter.Tk().withdraw()
                fpath = filedialog.askdirectory()
                tpath = f"{fpath}/urlqrcode.png"
                kr.save(f"{tpath}")
     break

def string():
    cable = input("Input the text you want to generate as a QR Code: ")
    ar = qrcode.make(cable)
    bit = int(input("How should I distribute the QR Code? (1. print it now), (2. save to a file): "))
    match bit:
     case 1:
         qrcodeT.qrcodeT(cable) 
         print("The QR Code has been printed to the console.")
     case 2:
         print("Where should I save this to?")
         tkinter.Tk().withdraw()
         fpath = filedialog.askdirectory()
         tpath = f"{fpath}/textqrcode.png"
         ar.save(f"{tpath}")

def wifi():
    ssid = input("What is the SSID (network name) of your wi-fi interface?")
    auths = ["1. WPA/WPA-2/WPA-3", "2. WEP", "3. nopass (No Password/Unsecured Network)"]
    while True:
     for auth in auths:
        print(auth)
     lock = input("Select the security of your selected wifi network (You can check in your device's Wi-Fi settings)")
     if lock == "1":
        passwd = input("Please enter the password for the Wi-Fi network")
        wifiqr = wifi_qrcode(ssid, hidden=False, authentication_type="WPA", password=passwd)
        wifiqr.print_ascii()
        break
     elif lock == "2":       
        passwd = input("Please enter the password for the Wi-Fi network")
        wifiqr = wifi_qrcode(ssid, hidden=False, authentication_type="WEP", password=passwd)
        wifiqr.print_ascii()
        break
     elif lock == "3":   
        wifiqr = wifi_qrcode(ssid, hidden=False, authentication_type="nopass", password="")
        wifiqr.print_ascii()
        break      

def fil():
    print("WFind the location of the file.")
    tkinter.Tk().withdraw()
    fpath = filedialog.askopenfilename()
    img = Image.open(fpath)
    dob = decode(img)
    for obj in dob:
        print("Data:", obj.data.decode("utf-8"))

def video():
   print("This will take a while to load.")
   print("Do not close the window to close the script, press the Q key.") 
   cap = cv2.VideoCapture(0)  

   if not cap.isOpened():
        print("Error: Could not open video stream.")
        return
   detector = cv2.QRCodeDetector()

   print("Press 'q' or close the window to exit.")

   while True:
        success, img = cap.read()

        if not success:
            print("Error: Could not read frame.")
            break

        data, bbox, _ = detector.detectAndDecode(img)
        if data:
            print("QR Code detected! Data:", data)
        
        cv2.imshow("QR Code Scanner - Press 'q' to exit", img)

        key = cv2.waitKey(1) & 0xFF 
        if key == ord("q"):
            break
    
   cap.release()
   cv2.destroyAllWindows()
   print("Video capture released and windows closed.")



def main():
    salad = ["1. Generate for URL","2. Generate for Text","3. Generate for Wi-Fi","4. Parse via File","5. Parse via Camera","6. Quit"]
    while True:
     for soup in salad:
        print(soup)   
     num = int(input("What do you want to do?: "))
     match num:
        case 1:
            url()
        case 2:
            string()
        case 3:
            wifi()
        case 4:
            fil()    
        case 5:
            video()
        case 6:
            break
        case _:
            print("Not an option.")        

if __name__ == "__main__":
    main()