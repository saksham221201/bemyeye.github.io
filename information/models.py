from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image
from gtts import gTTS
import os
# import gtts

class Information(models.Model):
    product_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=50)
    product_category = models.CharField(max_length=50, default=None)
    product_description = models.TextField(max_length=400)
    product_cost = models.IntegerField()
    manu_date = models.DateField()
    exp_date = models.DateField()
    # product_image = models.FileField(upload_to = "products", max_length = 250, null = True, default = None)
    qr_code = models.ImageField(upload_to = "qr_codes", blank = True)

    def __str__(self):
        return str(self.product_name)

    def save(self, *args, **kwargs):
        summary = "The name of the product is " + str(self.product_name) + ". The name of the company is " + str(self.company_name) + ". The category of the product is " + str(self.product_category) + ". " + str(self.product_description) + " The cost of the product is " + str(self.product_cost) + ". The manufacturing date is " + str(self.manu_date) + ". The expiry date is " + str(self.exp_date)
        # print(summary)

        language="en"
        myobj=gTTS(text=summary,lang=language,slow=False)
        myobj.save("static/audio/"+self.product_name+".mp3") 
        os.system("static/audio/"+self.product_name+".mp3") 

        qrcode_img = qrcode.make("https://helpothers-bemyeye.herokuapp.com/static/audio/"+self.product_name+".mp3")
        canvas = Image.new('RGB', (450, 450), 'white')
        # draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname = f'qr_code-{self.product_name}.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close()
        # myobj = gtts.gTTS(text=summary, lang='en', slow=False)
        # myobj.save("static/speech.mp3")
        super().save(*args, **kwargs)

# Create your models here.
