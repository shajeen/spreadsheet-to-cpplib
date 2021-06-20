import click
from cli import clitest


@click.command()
@click.option('--test', help='print random text for testing.')
def run_cli_interface(test):
    if test:
        clitest.print_demo_text(test)
