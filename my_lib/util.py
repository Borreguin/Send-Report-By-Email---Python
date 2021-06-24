"""
Este script contiene código que es útil para diferentes scripts en este proyecto

"""

import datetime as dt
import pandas as pd
import os, sys
script_path = os.path.dirname(os.path.abspath(__file__))
mylib_path = os.path.dirname(script_path)
project_path = os.path.dirname(mylib_path)

# import custom modules:
sys.path.append(project_path)
from settings import initial_settings as init
yyyy_mm_dd_hh_mm_ss = "%d-%m-%Y %H:%M:%S"
fmt_dd_mm_yyyy_hh_mm = "dd/MMM/yy HH:mm"
fmt_dd_mm_yyyy = "dd/MMM/yyyy"
fmt_dd_mm_yy_ = "dd_MMM_yyyy"

lb_group = "Group"
lb_email = "Email"
lb_report_id = "Report_ID"
lb_file_path = "File_Path"
lb_template_path = "Template_Path"
lb_active = "Active"
lb_subject = "Subject"
lb_from_email = "from_email"

def define_time_range_for_yesterday():
    tdy = dt.datetime.now().strftime(yyyy_mm_dd_hh_mm_ss)
    ytd = dt.datetime.now() - dt.timedelta(days=1)
    return tdy, ytd


def save_html(html_str, path_html_to_save):
    # Guardar el archivo html en la carpeta reportes:
    try:
        Html_file = open(path_html_to_save, "w", encoding='utf-8')
        Html_file.write(html_str)
        Html_file.close()
    except Exception as e:
        print(e)


def read_excel(excel_file, sheet_name):
    try:
        df = pd.read_excel(excel_file, sheet_name=sheet_name, engine='openpyxl')
        return True, df, "Leído exitosamente"
    except Exception as e:
        print(e)
        return False, pd.DataFrame(), "No se ha podido leer el archivo \n" + str(e)


def get_user_list(id_report, group:str):
    file_path = os.path.join(init.setting_path, "file_config.xlsx")
    success, df, msg = read_excel(file_path, "users")
    if success:

        if id_report is None:
            mask = df[lb_group] == group
            df = df[mask]
            users = list()
            for u in list(df[lb_email]):
                users += str(u).split(";")
            from_email = init.error_account
            users = list(set(users))
        else:
            df.set_index(lb_group, inplace=True)
            mask = df[lb_report_id] == id_report
            df = df[mask]
            users = str(df[lb_email].loc[group]).split(";")
            from_email = str(df[lb_email].loc[lb_from_email])
        return True, (users, from_email), "Usuarios leídos"
    return False, "", msg


def get_configurations():
    file_path = os.path.join(init.setting_path, "file_config.xlsx")
    success, df, msg = read_excel(file_path, "configurations")
    if success:
        mask = (df[lb_active] == "x")
        df = df[mask]
        df.set_index(lb_report_id, inplace=True)
        return True, df, msg
    return False, pd.DataFrame(), msg
