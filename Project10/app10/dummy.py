
# Image Captcha example

import random

from captcha.image import ImageCaptcha
from captcha.audio import AudioCaptcha

rno = random.randint(69,70)#69 is a start value and 70 is a end value.
rno1=random.randint(1,99)
rno2=random.randint(112,115)
rno3=random.randint(5,45)


captcha_mess = chr(rno)+str(rno1)+chr(rno2)+str(rno3)

#ImageCaptcha().write(captcha_mess,"one.png")

AudioCaptcha().write(str(rno),"one.mp3")

