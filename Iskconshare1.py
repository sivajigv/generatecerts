#importing the PIL library
import pandas as pd
import os
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from fontTools.ttLib import TTFont
 
path = r'./'
out_path = r'./out/'

def generate_certificates():
    name_list = pd.read_csv(path + 'inputfile.csv', sep=';')
    
    for index, row in name_list.iterrows():
        #Open an image
        img=Image.open(path + 'isk1.jpeg')
        
        #call draw Method to add 2D graphics in an image
        i1=ImageDraw.Draw(img)

        #Add Text to an image
        fnt = ImageFont.truetype(path + 'lucida-sans/Lucida Sans Demibold Italic.ttf', 25)
        i1.text((250,420), str(row['NAME']), font=fnt,fill=(0,0,0))
        i1.text((953,420), str(row['AGE']), font=fnt,fill=(0,0,0))
        i1.text((250,487), row['PLACE'], font=fnt,fill=(0,0,0))
        i1.text((677,487), row['ACTIVITY'], font=fnt,fill=(0,0,0))

        #save edited image
        #img.save(out_path + "\\iskgen_"+str(row['No'])+"_"+str(row['Name']).split()[0]+".jpeg")
        img.save(out_path + str(row['NAME']).split()[0]+str(row['NO'])+".jpeg")
        print("Generated cert# ",str(row['NO'])) ;  


generate_certificates()