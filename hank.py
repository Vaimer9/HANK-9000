import click
import math
from googlesearch import search
from datetime import datetime as dater
from tqdm import tqdm
import progressbar
import time
import random

@click.group()
def cli():
    pass

def rander():
    return random.randint(0, 9)

@cli.command()
@click.argument('string', default=None)
@click.argument('repeat', default=1, required=False)
def greet(string, repeat):
    """This Command Greets you"""
    for _ in range(repeat):
        click.echo(message=f"Hello {string}")


@cli.command()
@click.argument('first', type=click.INT,)
@click.argument('second',type=click.INT)
@click.argument("operation",type=click.STRING)
def math(first, second, operation):
    """ This Command can do 2 number maths """
    result = None
    if operation == "add":
        result = first + second
    elif operation == "sub":
        result = first - second
    elif operation == "mul":
        result = first * second
    elif operation == "div":
        result = first / second
    else:
        click.echo(message="Please enter the correct type of data.")
    click.echo(result)
        



@cli.command()
@click.argument('query', type=click.STRING)
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
@click.argument('file', type=click.STRING, default=None)
@click.argument('msg', type=click.STRING, default=None, required=False)
def create(file, msg):
    """Makes a files and writes stuff down in it"""
    f = None
    if msg == None:
        f = open(f'{file}', 'w')
        f.close()
        click.echo(f'{file} sucessfully created')
    else:
        f = open(f'{file}', 'w+')
        f.write(msg)
        f.close()
        click.echo(f'{file} sucessfully created and content written')



@cli.command()
@click.argument('file', type=click.STRING, default=None)
def content(file):
    """Shows content of a file"""
    x = open(f'{file}')
    for line in x:
        click.echo(line)

@cli.command()
@click.argument('name', type=click.STRING, default=None)
def hack(name):
    """Hacks a person"""
    r = f'{rander()}{rander()}.{rander()}{rander()}{rander()}.{rander()}{rander()}{rander()}.{rander()}{rander()}'

    if name == None:
        click.echo("Nobody was hacked")
    else:
        
        print("Commencing hacking protocol")
        time.sleep(1)
        print("Obtaining IP Address")
        for i in tqdm (range (101), desc="Getting IP Address", ascii=False, ncols=75):
            time.sleep(0.01)
        click.echo(f"Obtained IP Address: {r}\n")
        time.sleep(1)
        click.echo("Commencing DDOS attack")
        time.sleep(1)
        for i in tqdm (range (101), desc="Launching attack", ascii=False, ncols=75):
            time.sleep(0.01)
        click.echo(f"DDOS Attack on IP Address {r} was sucessful\n")
        click.echo(f'{name} was hacked sucessfully')
