import click
from cli import clitest
from lib import fileOperations

@click.command()
@click.option('--test', help='print random text for testing.')
@click.option('--file', help='file name to be converted')
def run_cli_interface(test, file):
    if test:
        clitest.print_demo_text(test)

    # check the file
    if fileOperations.check_file_exists(file):
        file_ext = fileOperations.file_ext_type(file)
        if file_ext in ".xlsx" or file_ext in '.xlsm':
            fileOperations.process_xlsm_file(file)
        else:
            fileOperations.process_csv_file(file)
    else:
        click.echo("File not found, please check.")
