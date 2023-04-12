import tkinter
from tkinter import *
import os
root = Tk()
class WindowDraggable():
    def __init__(self, label):
        self.label = label
        label.bind('<ButtonPress-1>', self.StartMove)
        label.bind('<ButtonRelease-1>', self.StopMove)
        label.bind('<B1-Motion>', self.OnMotion)
    def StartMove(self, event):
        self.x = event.x
        self.y = event.y
    def StopMove(self, event):
        self.x = None
        self.y = None
    def OnMotion(self, event):
        x = (event.x_root - self.x - self.label.winfo_rootx() + self.label.winfo_rootx())
        y = (event.y_root - self.y - self.label.winfo_rooty() + self.label.winfo_rooty())
        root.geometry("+%s+%s" %(x, y))
class Menu:
    def __init__(self, parent, title):
        self.parent = parent
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOWS", self.keluar)
        lebar = 290
        tinggi = 180
        setTengahX = (self.parent.winfo_screenwidth() - lebar) // 2
        setTengahY = (self.parent.winfo_screenheight() - tinggi) // 2
        self.parent.geometry("%ix%i+%i+%i" %(lebar, tinggi, setTengahX, setTengahY))
        self.parent.overrideredirect(1)
        self.parent.configure(bg = "#75a3a3")
        self.aturKomponen()
    def keluar(self, event = None):
        self.parent.destroy()
    def enkripsiSatuFile(self):
        try:
            print('==================================')
            print('|          ENCRYPT FILE          |')
            print('==================================')
            # take path of image as a input
            path = input(r'Enter path for Encrypt : ')
            
            # taking encryption key as input
            key = int(input('Enter Key for encryption : '))
            
            # print path of image file and encryption key that
            # we are using
            print('The path of file : ', path)
            print('Key for encryption : ', key)
            
            # open file for reading purpose
            fin = open(path, 'rb')

            # storing image data in variable "image"
            image = fin.read()
            fin.close()
            
            # converting image into byte array to
            # perform encryption easily on numeric data
            image = bytearray(image)

            # performing XOR operation on each value of bytearray
            for index, values in enumerate(image):
                image[index] = values ^ key

            # opening file for writing purpose
            fin = open(path, 'wb')
            
            # writing encrypted data in image
            fin.write(image)
            fin.close()
            print('Encryption Done...')

        except Exception:
            print('Error caught : ', Exception.__name__)
        
    def dekripsiSatuFile(self):
        # try block to handle the exception
        try:
            print('==================================')
            print('|          DECRYPT FILE          |')
            print('==================================')
            # take path of image as a input
            path = input(r'Enter path for Decrypt : ')
            
            # taking decryption key as input
            key = int(input('Enter Key for decrpytion : '))
            
            # print path of image file and decryption key that we are using
            print('The path of file : ', path)
            print('Note : Encryption key and Decryption key must be same.')
            print('Key for Decryption : ', key)
            
            # open file for reading purpose
            fin = open(path, 'rb')
            
            # storing image data in variable "image"
            image = fin.read()
            fin.close()
            
            # converting image into byte array to perform decryption easily on numeric data
            image = bytearray(image)

            # performing XOR operation on each value of bytearray
            for index, values in enumerate(image):
                image[index] = values ^ key

            # opening file for writing purpose
            fin = open(path, 'wb')
            
            # writing decryption data in image
            fin.write(image)
            fin.close()
            print('Decryption Done...')

        except Exception:
            print('Error caught : ', Exception.__name__)

    def enkripsiSatuFolder(self):
        print('==================================')
        print('|          ENCRYPT FOLDER        |')
        print('==================================')
        # take path of image as a input
        pathdir = input(r'Enter path for Encrypt Folder : ')
        # taking decryption key as input
        key = int(input('Enter Key for encrpytion : '))
        files = []
        
        # print path of image file and decryption key that we are using
        print('The path of file : ', pathdir)
        print('Key for Decryption : ', key)

        obj = os.scandir(pathdir)
        for item in obj:
            if item.is_file():
                files.append(item.path)
            
        try:
            for item in files:
                print(item)

                path = item

                # open file for reading purpose
                fin = open(path, 'rb')
                
                # storing image data in variable "image"
                image = fin.read()
                fin.close()
                
                # converting image into byte array to perform decryption easily on numeric data
                image = bytearray(image)

                # performing XOR operation on each value of bytearray
                for index, values in enumerate(image):
                    image[index] = values ^ key

                # opening file for writing purpose
                fin = open(path, 'wb')
                
                # writing decryption data in image
                fin.write(image)
                fin.close()
            print('Encryption Done...')

        except Exception:
            print('Error caught : ', Exception.__name__)
    
    def dekripsiSatuFolder(self):
        print('==================================')
        print('|          DECRYPT FOLDER        |')
        print('==================================')
        # take path of image as a input
        pathdir = input(r'Enter path for Decrypt Folder : ')
        
        # taking decryption key as input
        key = int(input('Enter Key for decrpytion : '))

        files = []
        
        # print path of image file and decryption key that we are using
        print('The path of file : ', pathdir)
        print('Note : Encryption key and Decryption key must be same.')
        print('Key for Decryption : ', key)

        obj = os.scandir(pathdir)
        for item in obj:
            if item.is_file():
                files.append(item.path)
            
        try:
            for item in files:
                print(item)

                path = item
                
                # open file for reading purpose
                fin = open(path, 'rb')
                
                # storing image data in variable "image"
                image = fin.read()
                fin.close()
                
                # converting image into byte array to perform decryption easily on numeric data
                image = bytearray(image)

                # performing XOR operation on each value of bytearray
                for index, values in enumerate(image):
                    image[index] = values ^ key

                # opening file for writing purpose
                fin = open(path, 'wb')
                
                # writing decryption data in image
                fin.write(image)
                fin.close()
            print('Decryption Done...')

        except Exception:
            print('Error caught : ', Exception.__name__)
    
    def pro(self, event):
        self.Enkripsi()
    def aturKomponen(self):
        frameUtama = Frame(root, width=400, height=300, bg="#75a3a3")
        frameUtama.grid(row=0, column=1)
        WindowDraggable(frameUtama)
        self.buttonX = Button(frameUtama, text="X", fg="white", bg="#ff0000", width=6, height=2, bd=0, activebackground="#fb8072", activeforeground="white", command=self.keluar, relief=FLAT)
        self.buttonX.grid(row=0, column=0)
        self.encrypt = Button(frameUtama, text="Encrypt File", command=self.enkripsiSatuFile, fg="white", bg="#0066ff", width=13, height=2, bd=0, activebackground="whitesmoke", activeforeground="#444")
        self.encrypt.grid(row=3, column=2, pady=6, padx=2, sticky="e")
        self.decrypt = Button(frameUtama, text="Decrypt File", command=self.dekripsiSatuFile, fg="white", bg="#0066ff", width=13, height=2, bd=0, activebackground="whitesmoke", activeforeground="#444")
        self.decrypt.grid(row=3, column=6, pady=6, padx=2, sticky="e")

        self.decrypt = Button(frameUtama, text="Encrypt Folder", command=self.enkripsiSatuFolder, fg="white", bg="#0066ff", width=13, height=2, bd=0, activebackground="whitesmoke", activeforeground="#444")
        self.decrypt.grid(row=6, column=2, pady=6, padx=2, sticky="e")
        self.decrypt = Button(frameUtama, text="Decrypt Folder", command=self.dekripsiSatuFolder, fg="white", bg="#0066ff", width=13, height=2, bd=0, activebackground="whitesmoke", activeforeground="#444")
        self.decrypt.grid(row=6, column=6, pady=6, padx=2, sticky="e")

def main():
    Menu(root, ":: Encrypt & Decrypt ::")
    root.mainloop()