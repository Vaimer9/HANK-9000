import click
import math
from googlesearch import search
from datetime import datetime as dater

@click.group()
def cli():
    pass


@cli.command()
@click.option('--string', default = None ,help="This is what will get greeted")
@click.option('--repeat', default=1, help="No. of times to be greeted default is 1")
def greet(string, repeat, color):
    """This Command Greets you"""
    for x in range(repeat):
        if string == None:
            click.echo(message="Please specify the --string argument")
            #print("Please specify the --string argument")
        else:
            click.echo(message=f"Hello {string}")
            #click.echo(message=f"Hello {string}")
            #print(f'Hello {string}')


@cli.command()
@click.option('--first', type=click.INT, default=None, prompt="First Number" ,help="First Number")
@click.option('--second',type=click.INT,default=None, prompt="Second Number" ,help="Second Number")
@click.option("--operation",type=click.STRING,  default="None")
def math(first, second, operation):
    """ This Command can do 2 number maths """
    first = int(first)
    result = None
    second = int(second)
    if first and second == None:
        click.echo(message="Please enter at least two numbers")
    else:
        if operation == "+":
            result = first + second
        elif operation == "-":
            result = first - second
        elif operation == "m":
            result = first * second
        elif operation == "/":
            result = first / second
        elif operation == "None":
            click.echo(message="I am pretty sure this error will never be displayed :/")
        else:
            click.echo(message="Please enter the correct type of data.")
        click.echo(result)

@cli.command()
@click.option('--query', type=click.STRING, default=None, prompt="What is your search query", help="The string to be searched")
def google(query):
    """Google stuff on the internet"""
    
    for x in search(query, tld="co.in", num=10, stop=10, pause=2):
        click.echo(message=x)

@cli.command()
def datetime():
    """ Prints out the current date and time """
    now = dater.now()
    dt = now.strftime("%B %m %Y")
    timer = now.strftime("%H:%M:%S")
    click.echo(dt)
    click.echo(timer)




@cli.command()
@click.option('--file', type=click.STRING, default=None)
@click.option('--msg', type=click.STRING, default=None)
def create(file, msg):
    """Makes a files and writes stuff down in it"""
    if file == None:
        click.echo(message="Please enter the --file argument")
    else:
        f = None
        if msg == None:
            f = open(f'{file}', 'w')
        else:
            f = open(f'{file}', 'w+')
            f.write(msg)
        