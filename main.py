__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'

import os
import datetime
from zipfile import ZipFile

def clean_cache():
    #subfolder in de CWD
    folder = os.path.join(os.getcwd(), 'cache')
    
    if os.path.exists(folder):
        #bestaat al> leeg maken
        for file in os.scandir(folder):
            os.remove(file.path)
    else :
       #Bestaat niet > aanmaken
       os.mkdir(folder) 

def cache_zip(path_to_zip_file,directory_to_extract_to):
    #Volledige pathnamen gebruiken
    with ZipFile(path_to_zip_file, 'r') as zip_ref:
        zip_ref.extractall(directory_to_extract_to)

def cached_files():
    #vaste folder
    pad = os.path.join(os.getcwd(), 'cache')
    #Hier komen de bestandsnamen
    files =[]
    for f in os.listdir(pad):
        #Voeg toe aan list
       files.append(pad + '\\' + f)

    return files

def find_password(file_paths):
    #Loop door list met bestanden
    for txt in file_paths:
        #open bestand
        bestand = open(txt, "r")
        #Lees per regel
        for regel in bestand:
            #Convert naar lowercase
            check_lower = regel.lower()
            #check of in regel letters zijn
            contains_letters = check_lower.islower()
            if contains_letters:
                #Tekst na de spatie is de pw
                return regel[regel.find(' '):].strip()

#locatie van dit bestand
#pad = os.getcwd()

#clean_cache()
#cache_zip(os.path.join(os.path.dirname(__file__),'data.zip') , os.path.join(os.getcwd(), 'cache'))
#print(cache_files())
#print(find_password(cached_files()))