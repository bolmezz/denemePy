import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

mesaj = MIMEMultipart()

mesaj["From"] = "beyza.olmez96@gmail.com"

mesaj["To"] = "byzlmz@gmail.com"

mesaj["Subject"] = "Smtp mail gönderme"

yazi = """Stmp ile mail gönderiyorum

       Beyza Ölmez
       
       """""

mesaj_govdesi = MIMEText(yazi, "plain")

mesaj.attach(mesaj_govdesi)

# GMail server'larına bağlanma

try:
    mail = smtplib.SMTP("smtp.gmail.com",
                        587, )  # hangi smtp serverına bağlanmak istediğimizi ilk değer olarak veriyoruz
    # ikinci değer o serverın hangi portuna bağlanacağımızı veriyoruz
    mail.ehlo()  # smtp serverına bağlanıyoruz (kendimizi tanıtıyoruz)
    mail.starttls()  # kullanıcı adı ve şifrelerin şifrelenmesi için
    mail.login("beyza.olmez96@gmail.com",
               "08040094")  # gönderen mailin kullanıcı adı ve şifresini giriyoruz ve servera bağlanıyoruz
    mail.sendmail(mesaj["From"], mesaj["To"],
                  mesaj.as_string())  # mesaj ilk başta MIMEMultipart olarak tanımlanmıştı bunu stringe çeviriyoruz

    print("Mail başarıyla gönderildi")
    mail.close()
except:
    sys.stderr.write("Bir hata oluştu")
    sys.stderr.flush()  # ekrana hata mesajını yazdırır

