"""
Archivo de configuraciones generales:
Permite configurar el script
Designed by: Roberto Sánchez
Servicios de Tiempo Real - Gerencia de Desarrollo Técnico
Junio 2021
"""

config = dict()

config["name"] = "Send Mail Application"
config["version"] = "0.1"
config["DEBUG"] = False
config["mail_server"] = "Your_IP_mail_server"
config["from_email"] = "my.email.to.send@account.com"
config["password"] = None

# LOG CONFIGURATION
config["ROTATING_FILE_HANDLER_HELP"] = "https://docs.python.org/3.6/library/logging.handlers.html#logging.handlers.RotatingFileHandler.__init__",
config["ROTATING_FILE_HANDLER"] = {"filename": "api.log", "maxBytes": 20000, "backupCount": 5, "mode": "a"}
config["ROTATING_FILE_HANDLER_LOG_LEVEL"] = {"value": "info", "options": ["error", "warning", "info", "debug", "off"]}

# Repositories (folders locales o externos de la aplicación)
config["REPORT_REPO"] = "_reports"
config["TEMPLATE_REPO"] = "templates"

config["SUPPORTED_FORMAT_DATES"] = ["%Y-%m-%d %H:%M:%S", "%Y-%m-%d %H:%M", "%Y-%m-%d", "%Y-%m-%d %H:%M:%S.%f"]
config["DEFAULT_DATE_FORMAT"] = "%Y-%m-%d %H:%M:%S"

