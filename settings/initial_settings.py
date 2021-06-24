# Created by Roberto Sanchez at 3/29/2019
# -*- coding: utf-8 -*-
""" Set the initial settings of this application"""
import sys
from logging.handlers import RotatingFileHandler
from logging import StreamHandler
import logging
import os
from .config import config as raw_config

""""
    Created by Roberto Sánchez A :
    Any copy of this code should be notified at rg.sanchez.a@gmail.com; you can redistribute it
    and/or modify it under the terms of the MIT License.

    If you need more information. Please contact the email above: rg.sanchez.a@gmail.com
    "My work is well done to honor God at any time" R Sanchez A.
    Mateo 6:33
"""

""" script path"""
script_path = os.path.dirname(os.path.abspath(__file__))
project_path = os.path.dirname(script_path)
setting_path = script_path
print("Loading configurations from: " + script_path)
""" initial configuration """
config = raw_config

""" configuracion de mail """
mail_server = config["mail_server"]
password = config["password"]
from_email = config["from_email"]
error_account = "noreply@account.com"

""" Log file settings: """
log_name = config["ROTATING_FILE_HANDLER"]["filename"]
log_path = os.path.join(project_path, "logs")
log_file_name = os.path.join(log_path, log_name)
config["ROTATING_FILE_HANDLER"]["filename"] = log_file_name
ROTATING_FILE_HANDLER = config["ROTATING_FILE_HANDLER"]
ROTATING_FILE_HANDLER_LOG_LEVEL = config["ROTATING_FILE_HANDLER_LOG_LEVEL"]

""" SUPPORTED DATES """
SUPPORTED_FORMAT_DATES = config["SUPPORTED_FORMAT_DATES"]
DEFAULT_DATE_FORMAT = config["DEFAULT_DATE_FORMAT"]


""" Production server """
production_path = os.path.join(project_path, "Production_server.txt")
print(production_path, os.path.exists(production_path))
if os.path.exists(production_path):
    DEBUG = False
else:
    DEBUG = config["DEBUG"]

"""" MODULES REPO CONFIGURATION """
# Source repo es una ubicación específica en caso de producción
# pero en caso de pruebas, es una ubicación local llamada "source"
REPORT_REPO = config["REPORT_REPO"]
TEMPLATE_REPO = config["TEMPLATE_REPO"]
REPOS = [REPORT_REPO, TEMPLATE_REPO]

FINAL_REPO = list()
for repo in REPOS:
    this_repo = os.path.join(project_path, repo)
    if not os.path.exists(this_repo):
        os.makedirs(this_repo)
    FINAL_REPO.append(this_repo)

REPORT_REPO, TEMPLATE_REPO = FINAL_REPO

class LogDefaultConfig():
    """
    Default configuration for the logger file:
    """
    rotating_file_handler = None

    def __init__(self, log_name: str = None):
        if log_name is None:
            log_name = "Default.log"

        self.log_file_name = os.path.join(log_path, log_name)
        self.rotating_file_handler = ROTATING_FILE_HANDLER
        self.rotating_file_handler["filename"] = self.log_file_name
        logger = logging.getLogger(log_name)
        formatter = logging.Formatter('%(asctime)s : %(levelname)s - %(message)s')
        # creating rotating and stream Handler
        R_handler = RotatingFileHandler(**self.rotating_file_handler)
        R_handler.setFormatter(formatter)
        S_handler = StreamHandler(sys.stdout)
        # adding handlers:
        logger.addHandler(R_handler)
        logger.addHandler(S_handler)

        # setting logger in class
        self.logger = logger

        self.level = ROTATING_FILE_HANDLER_LOG_LEVEL["value"]
        options = ROTATING_FILE_HANDLER_LOG_LEVEL["options"]
        if self.level in options:
            if self.level == "error":
                self.logger.setLevel(logging.ERROR)
            if self.level == "warning":
                self.logger.setLevel(logging.WARNING)
            if self.level == "debug":
                self.logger.setLevel(logging.DEBUG)
            if self.level == "info":
                self.logger.setLevel(logging.INFO)
            if self.level == "off":
                self.logger.setLevel(logging.NOTSET)
        else:
            self.logger.setLevel(logging.ERROR)


default_log = LogDefaultConfig("mail.log").logger