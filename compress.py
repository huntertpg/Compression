from PIL import Image
import PIL
import os
import glob
from datetime import date

directory = str(date.today())
rootdir = '2021-05-20/'

def listdirs(rootdir):
    for file in os.listdir(rootdir):
        d = os.path.join(rootdir, file)
        if os.path.isdir(d):
            print(d)
            listdirs(d)

def compressAmerican():
    
    currentDir = rootdir + "American/"
    directories = os.listdir(currentDir)
    for directory in directories:
        print(currentDir + directory)
        images = [file for file in os.listdir( currentDir + directory) if file.endswith(('jpg', 'png' ))]
        for image in images:
            # 1. Open the image
            img = Image.open(currentDir + directory + "/" + image)
            # 2. Compressing the image
            img.save(currentDir + directory + "/" + image,
                optimize=True,
                quality=20)

def compressKenjoh():
    
    currentDir = rootdir + "Kenjoh/"
    directories = os.listdir(currentDir)
    for directory in directories:
        print(currentDir + directory)
        images = [file for file in os.listdir( currentDir + directory) if file.endswith(('jpg', 'png' ))]
        for image in images:
            # 1. Open the image
            img = Image.open(currentDir + directory + "/" + image)
            # 2. Compressing the image
            img.save(currentDir + directory + "/" + image,
                optimize=True,
                quality=20)

def compressMileHigh():
    
    currentDir = rootdir + "Mile-High/"
    directories = os.listdir(currentDir)
    for directory in directories:
        print(currentDir + directory)
        images = [file for file in os.listdir( currentDir + directory) if file.endswith(('jpg', 'png' ))]
        for image in images:
            # 1. Open the image
            img = Image.open(currentDir + directory + "/" + image)
            # 2. Compressing the image
            img.save(currentDir + directory + "/" + image,
                optimize=True,
                quality=30)

def compressPOAO():
    
    currentDir = rootdir + "POAO/"
    directories = os.listdir(currentDir)
    for directory in directories:
        print(currentDir + directory)
        images = [file for file in os.listdir( currentDir + directory) if file.endswith(('jpg', 'png' ))]
        for image in images:
            # 1. Open the image
            img = Image.open(currentDir + directory + "/" + image)
            # 2. Compressing the image
            img.save(currentDir + directory + "/" + image,
                optimize=True,
                quality=20)

def compressPOAW():
    
    currentDir = rootdir + "POAW/"
    directories = os.listdir(currentDir)
    for directory in directories:
        print(currentDir + directory)
        images = [file for file in os.listdir( currentDir + directory) if file.endswith(('jpg', 'png' ))]
        for image in images:
            # 1. Open the image
            img = Image.open(currentDir + directory + "/" + image)
            # 2. Compressing the image
            img.save(currentDir + directory + "/" + image,
                optimize=True,
                quality=20)

compressAmerican()
compressKenjoh()
compressMileHigh()
compressPOAO()
compressPOAW()