### cert-template3-winner.jpeg  --- Certificate of Acheivement - NO, NAME, AGE, PLACE, ACTIVITY
### cert-template2-participant.jpeg   -- Certificate of Appreciation. --- NO,NAME,AGE,EMAIL
### 2022-09-06 - Sivaji - integrate email sending program
### Generates certificates with the new template given by iskcon

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
subject = 'Participants Certificate'
emailbody = """Hare Krishna,
Please find the attached Participation Certificate for Online Cultural Fest.

Old images, Videos wouldn't be considered for competitions. 

No calls are encouraged for knowing the results.

We got many thousands of participants, 

So, the results will be announced in two/ three phases, 

Please Visit https://www.iskconnellore.com/ on August 31 for Phase 1 .
September 7th  for Phase 2 
September 15 th for Phase 3 Balance after  September 22.

https://m.facebook.com/groups/165368158397896/permalink/ 
In the above link we are uploadeding all the partcipants content. 
Note : Still, we have to upload thousands of partcipants content. 

Please be patient & co-operate.

Prizes can be collected personally from the ISKCON Nellore center or will be couriered to your communication address against payment for courier charges (Packing, Handling, Forwarding).

Tentatively, Prizes will be available for dispatch from September 22 nd onwards. 

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
    
    for index, row in name_list.iterrows():
        #Open an image
        img=Image.open(path + 'cert-template2-participant.jpeg')
        
        #call draw Method to add 2D graphics in an image
        i1=ImageDraw.Draw(img)

        #Add Text to an image
        fnt = ImageFont.truetype(path + 'lucida-sans/Lucida Sans Demibold Italic.ttf', 30)
        i1.text((250,420), str(row['NAME']), font=fnt,fill=(0,0,0))
        i1.text((953,420), str(row['AGE']), font=fnt,fill=(0,0,0))
       
        
        to = row['EMAIL'] 
        #save edited image
        #img.save(out_path + str(row['NO']) + "_" + str(row['NAME']).split()[0]+".jpeg")
        outfilename = out_path + str(row['NO']) + "_" + str(row['NAME']).split()[0]+".jpeg"
        img.save(outfilename)
        print("Generated cert: ", outfilename) ;  
        content = [emailbody,outfilename]
        #with yagmail.SMTP(user, app_password) as yag:
        #    yag.send(to, subject, content)
        #    print('Sent email successfully:', outfilename,to)



generate_certificates()