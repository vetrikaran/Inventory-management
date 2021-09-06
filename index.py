import os
import fileinput
print('===============================')
print('= Inventory Management System =')
print('===============================')
def menuDisplay():
    print('(1) Add New Item')
    print('(2) Remove Item')
    print('(3) purchase Item')
    print('(4) Print Inventory Report')
    print('(5) Quit')
    CHOICE = int(input("Enter choice: "))
    menuSelection(CHOICE)

def menuSelection(CHOICE):
    if CHOICE == 1:
        addInventory()
    elif CHOICE == 2:
        removeInventory()
    elif CHOICE == 3:
        purchaseInventory()
    elif CHOICE == 4:
        printInventory()
    elif CHOICE == 5:
        exit()

def addInventory():
    InventoryFile = open('Inventory.txt', 'a')
    print("Adding Inventory")
    print("================")
    item_description = input("Enter the name of the item: ")
    item_quantity = input("Enter the quantity of the item: ")
    item_price = input("Enter the price of the item: ")
    item_availablity = input("Enter the availability if the item: ") 
    item_manufacture_date = input("Enter the manufacture date of the item: ")
    item_expired_date = input("Enter the expiry date of the item: ")
    InventoryFile.write(item_description + '\n')
    InventoryFile.write(item_quantity + '\n')
    InventoryFile.write(item_price + '\n')
    InventoryFile.write(item_availablity + '\n')
    InventoryFile.write(item_manufacture_date + '\n')
    InventoryFile.write(item_expired_date + '\n')
    print("your product successfully added")
    InventoryFile.close()
    CHOICE = input('Enter y to continue or n to exit: ')
    if CHOICE == 'y':
            menuDisplay()
    else:
        exit()
    
def removeInventory():
    print("Removing Inventory")
    print("==================")
    item_description = input("Enter the item name to remove from inventory: ")

    file = fileinput.input('Inventory.txt', inplace=True)

    for line in file:
         if item_description in line:
             for i in range(1):
                 next(file, None)
                 next(file, None)
                 next(file, None)
                 next(file, None)
                 next(file, None)
         else:
             print(line.strip('\n'), end='\n')
    item_description
    CHOICE = input('Enter y to continue or n to exit: ')
    if CHOICE == 'y':
            menuDisplay()
    else:
        exit()

def purchaseInventory():
    AvailableInventory()
    print('purschase Inventory')
    print('===================')
    item_description = input('Enter the name of the item: ')
    
    f = open('Inventory.txt', 'r')
    search = f.readlines()
    f.close
    
    for i, line in enumerate(search):
        if item_description in line:
            for b in search[i:i+1]:
                print('Item:     ', b, end='')
            for c in search[i+1:i+2]:
                print('Quantity: ', c, end='')
            for d in search[i+2:i+3]:
               rate = d;
               print('Price:',d,end='')
           
    item_rate = int(input('Enter the quantity of this item: '))
    
    print('Bill Amount =',(int(rate) * item_rate))
    print('------------')
    
    CHOICE = input('Enter y to continue or n to exit: ')
    if CHOICE == 'y':
            menuDisplay()
    else:
        exit()
        
def printInventory():
    InventoryFile = open('Inventory.txt', 'r')
    item_description = InventoryFile.readline()
    print('Current Inventory')
    print('-----------------')
    while item_description != '':
        item_quantity = InventoryFile.readline()
        item_price = InventoryFile.readline()
        item_availablity = InventoryFile.readline()
        item_manufacture_date = InventoryFile.readline()
        item_expired_date = InventoryFile.readline()
        item_description = item_description.rstrip('\n')
        item_quantity = item_quantity.rstrip('\n')
        item_price = item_price.rstrip('\n')
        item_availablity = item_availablity.rstrip('\n')
        item_manufacture_date = item_manufacture_date.rstrip('\n')
        item_expired_date = item_expired_date.rstrip('\n')
        print('Item:     ', item_description)
        print('Quantity: ', item_quantity)
        print('price: ', item_price)
        print('Availability: ', item_availablity)
        print('Manufacture Date: ', item_manufacture_date)
        print('Expiry Date: ', item_expired_date)
        print('----------')
        item_description = InventoryFile.readline()
    InventoryFile.close()

    CHOICE = input('Enter y to continue or n to exit: ')
    if CHOICE == 'y':
            menuDisplay()
    else:
        exit()
def AvailableInventory():
    InventoryFile = open('Inventory.txt', 'r')
    item_description = InventoryFile.readline()
    print('Current Availablity')
    print('-----------------')
    while item_description != '':
        item_quantity = InventoryFile.readline()
        item_price = InventoryFile.readline()
        item_availablity = InventoryFile.readline()
        item_manufacture_date = InventoryFile.readline()
        item_expired_date = InventoryFile.readline()
        item_description = item_description.rstrip('\n')
        item_quantity = item_quantity.rstrip('\n')
        item_price = item_price.rstrip('\n')
        item_availablity = item_availablity.rstrip('\n')
        item_manufacture_date = item_manufacture_date.rstrip('\n')
        item_expired_date = item_expired_date.rstrip('\n')
        print('Item:     ', item_description)
        item_description = InventoryFile.readline()
    print('----------')
    InventoryFile.close()

menuDisplay()
