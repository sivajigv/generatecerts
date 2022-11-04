### New template-3.jpeg Certificate of Acheivement - NAME, AGE, PLACE, ACTIVITY
### template-2.jpeg is Certificate of Appreciation. --- NAME,AGE
### 2022-09-06 - Sivaji - integrate email sending program
### Generates certificates with the new template given by iskcon
### 2022-09-29 updated with revised email body
### Oct2nd. tried adding email validation, but got a few errors.

#importing the PIL library
import pandas as pd
import os 
import yagmail
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from fontTools.ttLib import TTFont
 
path = r'./'
out_path = r'./out/'

user = 'iskconnellorefest@gmail.com'
#app_password = 'trlrdcnlzwobqlys' # a token for sgv gmail
app_password =  'rgetyapiajhathkm'
#to = 'learningdse@gmail.com'
subject = 'Winners Certificate'
emailbody = """Hare Krishna,
Please find the attached Winners Certificate ( Certificate of Achievement) for Online Cultural Fest.

Prizes can be collected personally from the ISKCON Nellore center or will be couriered to your communication address against payment for courier charges for  (Packing, Handling, Forwarding) Per partcipant are as follows. 

For Indian address - Rs 250 
For Foreign Address - $ 15 

 Note : For BPL ( Below poverty line) partcipants will be sent freely 

Phone pe / Paytm to +91 8919717982 . 

 Each Gift pack contains 
1. Specially designed Gold Antique Medal. 
2. Srila Prabhupada book. 
3. 108 beads Japa Mala. 
4. Mantra Card. 
5. Maha Prasadam 

If you wish to receive Giftpack , please submit your Full communication address with land mark, pincode & mobile number, Email & attach your pay screen shot. 

Tentatively , Prizes will be available for dispatch from October 1 onwards. 

For any queries please Whatsapp +91 8919717982 or +91 8977637108 (Chinmaya Krishna Dasa) 

iskconnellorefest@gmail.com

Thanking you,

In the Service of Humanity & Mankind

Chinmaya Krishna Dasa
+91 8919717982
+91 8977637108
https://www.iskconnellore.com/"""




try:
	os.makedirs (out_path) 
except OSError as error:
	print ()

def generate_certificates():
    name_list = pd.read_csv(path + 'inputfile.csv', sep=';')
    f = open(out_path + 'log_noemail.txt', 'w')
    
    for index, row in name_list.iterrows():
        #Open an image
        img=Image.open(path + 'cert-template3-winner.jpeg')
        
        #call draw Method to add 2D graphics in an image
        i1=ImageDraw.Draw(img)

        #Add Text to an image
        fnt = ImageFont.truetype(path + 'lucida-sans/Lucida Sans Demibold Italic.ttf', 35)
        i1.text((250,420), str(row['NAME']), font=fnt,fill=(0,0,0))
        i1.text((250,470), str(row['AGE']), font=fnt,fill=(0,0,0))
       
        i1.text((590,470), row['PLACE'], font=fnt,fill=(0,0,0))
        i1.text((289,537), row['ACTIVITY'], font=fnt,fill=(0,0,0))
        
        to = row['EMAIL'] 
 
        #save edited image
        #img.save(out_path + str(row['NO']) + "_" + str(row['NAME']).split()[0]+".jpeg")
        outfilename = out_path + str(row['NO']) + "_" + str(row['NAME']).split()[0]+".jpeg"
        img.save(outfilename)
        print("Generated cert# ", out_path, str(row['NO'])) ;  
        content = [emailbody,outfilename]
        with yagmail.SMTP(user, app_password) as yag:
            if (to != ' '):
                yag.send(to, subject, content)
                print('Sent email successfully', outfilename)
            else:
                f.write('Email not available: '+ outfilename + '\n')



generate_certificates()