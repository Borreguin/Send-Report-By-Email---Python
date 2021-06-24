
import os
from my_lib import util as u
from my_lib.send_mail import send_mail
from settings import initial_settings as init
import codecs
logger = init.default_log

def send_report(report_id, config:dict, group):
    # Get user configurations:
    success, (users, from_email), msg = u.get_user_list(report_id, group)
    if not success:
        return False, msg
    # Use report info:
    # Usando Templates:
    template_path = config.get(u.lb_template_path, None)
    if template_path is None:
        return False, f"El reporte [{report_id}] no tiene una plantilla a enviar"
    template_path = os.path.join(init.TEMPLATE_REPO, template_path)
    html_str = codecs.open(template_path, 'r', 'utf-8').read()
    # Utilizando adjunto:
    file_path = config.get(u.lb_file_path, None)
    subject = config.get(u.lb_subject, "Sin titulo")
    # si existe algún archivo a anexar:
    if isinstance(file_path, str):
        if not os.path.exists(file_path):
            return False, f"El archivo [{file_path}] del reporte [{report_id}] no existe."
        files = [file_path]
    else:
    # caso contarario
        files = None
    success, msg = send_mail(msg_to_send=html_str, subject=subject, recipients=users, from_email=from_email, files=files)
    return success, msg


def run_all_reports(test=False):
    # Get configurations
    success, df_config, msg = u.get_configurations()
    if not success:
        return False, msg
    n_reports = 0
    for report_id in df_config.index:
        group = "test" if test else "usuarios"
        success, msg = send_report(report_id, df_config.loc[report_id].to_dict(), group)
        if success:
            n_reports += 1
            logger.info(f"Reporte [{report_id}]: {msg}")
        else:
            send_error_report(test, report_id, msg)

    return True, f"Reportes enviados de manera correcta: [{n_reports}]"


def send_error_report(test=False, report_id=None, msg_error=None):
    # Get user configurations:
    if test:
        success, (users, from_email), msg = u.get_user_list(report_id, "test")
    else:
        success, (users, from_email), msg = u.get_user_list(report_id, "administradores")
    template_path = os.path.join(init.TEMPLATE_REPO, "reportar_error.html")
    html_str = codecs.open(template_path, 'r', 'utf-8').read()
    html_str = html_str.replace("#ERROR", msg_error)
    log_path = os.path.join(init.log_path, "mail.log")
    subject = "[Error] Envío de reportes" if report_id is None else f"[Error] Envío del reporte {report_id}"
    success, msg = send_mail(msg_to_send=html_str, subject=subject, recipients=users, from_email=from_email,
                             files=[log_path])
    return success, msg