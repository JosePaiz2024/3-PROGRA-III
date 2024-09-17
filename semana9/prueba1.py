import smtplib

servidor = "smtp.gmail.com"
puerto = 587
correo = "josepaiz168@gmail.com"
passwd = "mxtk lzar doic aof"

try:
    conec = smtplib.SMTP(servidor, puerto)
    conec.starttls()
    conec.login(correo,passwd)
    conec.sendmail(correo, correo, "Subject: Este es un asunto" + "\n\nEsta es una prueba" )

    conec.quit
except smtplib.SMTPException as e:
    print("Error al enviar el correo " (e))
finally:
    print("Se ha enviado exitosamente")
