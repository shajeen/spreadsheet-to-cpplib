import os.path

import click

from lib import xlsmToCpp
from lib import csvToCpp

def check_file_exists(file_name):
    return os.path.isfile(file_name)


def file_ext_type(file_name):
    return os.path.splitext(file_name)[-1]


def process_xlsm_file(file_name):
    loaded_excel_file = xlsmToCpp.xlsm.load_excel_file(file_name)
    list_of_sheet = xlsmToCpp.xlsm.get_excel_file_sheet_names()
    click.echo("Select which sheet you want ?")
    for i in range(1,len(list_of_sheet)):
        click.echo("{0}. [{1}]".format(i,list_of_sheet[i-1]))
    click.echo("{0}. All SHEETS ?".format(len(list_of_sheet)))
    sheet = click.prompt(':', type=int)
    click.echo("you have select: {0}".format(sheet))
    pass


def process_csv_file(file_name):
    pass
