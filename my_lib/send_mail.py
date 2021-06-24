import os, sys
import traceback

reader_path = os.path.dirname(os.path.abspath(__file__))
my_lib_path = os.path.dirname(reader_path)
project_path = os.path.dirname(my_lib_path)
sys.path.append(project_path)
from settings import initial_settings as init
from email.mime.image import MIMEImage


script_path = os.path.dirname(os.path.abspath(__file__))
im_path = os.path.join(init.project_path, "_reports")
template_path = os.path.join(init.project_path, "templates")
html_error_template_path = os.path.join(template_path, "reportar_error.html")
html_report_template_path = os.path.join(template_path, "supervision_servidores_sps.html")
log_path = os.path.join(init.project_path, "logs")
log = init.default_log


def send_mail(msg_to_send:str, subject, recipients: list, from_email, image_list: list = None, files=None):
    from email.mime.multipart import MIMEMultipart
    from email.mime.application import MIMEApplication
    from email.mime.text import MIMEText
    from os.path import basename
    import smtplib

    try:
        im_to_append = list()
        # configure images if is needed
        if image_list is not None and isinstance(image_list, list):
            # This assumes the images are in "templates" folder
            for ix, image in enumerate(image_list):
                if "/" in image:
                    image_l = image.replace("./", "")
                    image_l = image_l.split("/")
                    to_check = os.path.join(im_path, *image_l)
                else:
                    to_check = os.path.join(im_path, image)

                if os.path.exists(to_check):
                    # redefine src= in html file (cid:image1)
                    msg_to_send = msg_to_send.replace(image, f"cid:image{ix}")
                    im_to_append.append(to_check)

        # server configuration:
        SERVER = init.mail_server

        # create message object instance
        msg = MIMEMultipart('related')

        # setup the parameters of the message
        msg['From'] = from_email
        msg['To'] = ", ".join(recipients)
        msg['Subject'] = subject
        msg.preamble = """"""

        # add in the message body as HTML content
        HTML_BODY = MIMEText(msg_to_send, 'html')
        msg.attach(HTML_BODY)

        # adding messages to the mail (only the ones that where found)
        for ix, image in enumerate(im_to_append):
            try:
                fp = open(os.path.join(im_path, image), 'rb')
                msgImage = MIMEImage(fp.read())
                fp.close()
                # Define the image's ID as referenced above
                msgImage.add_header('Content-ID', f'<image{ix}>')
                msg.attach(msgImage)
            except:
                pass

        # Add files if is needed:
        for f in files or []:
            with open(f, "rb") as fil:
                part = MIMEApplication(
                    fil.read(),
                    Name=basename(f)
                )
            # After the file is closed
            part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
            msg.attach(part)

        # create server
        server = smtplib.SMTP(SERVER)

        server.starttls()

        # Login Credentials for sending the mail
        # server.login(msg['From'], password)

        # send the message via the server.
        server.sendmail(msg['From'], recipients, msg.as_string())

        server.quit()
        return True, f"Correo enviado correctamente. Detalles enviados a: {msg['To']}"
    except Exception as e:
        tb = traceback.format_exc()
        log.error(tb)
        return False, f"Error al enviar el correo electrónico: {str(e)}"




