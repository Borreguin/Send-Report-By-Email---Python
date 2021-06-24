# Version: 22 junio 2020
# Roberto Sánchez

import logging
import os, sys
import datetime as dt
import traceback
script_path = os.path.dirname(os.path.abspath(__file__))

# import custom scripts:
sys.path.append(script_path)
from settings import initial_settings as init
import reports


if __name__ == "__main__":

    test = False
    logger = init.default_log
    msg = "Empezando envío de mensaje"
    logger.info(msg)
    # Ejecutando envío de mensajes
    try:
        success, msg = reports.run_all_reports(test=test)
        logger.info(msg)
    except Exception as e:
        msg = f"Problema al correr los reportes \n " + str(e) + "\n" \
              + traceback.format_exc()
        logger.error(msg)
        success, msg = reports.send_error_report(test, None, msg)
        logger.error(msg)


