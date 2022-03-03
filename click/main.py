import pandas as pd
import click
import os
import configparser
from datetime import date


@click.group()
def cli():
    """
    A simple command line interface to add and change task on a daily.
    """
    pass


@cli.command()
@click.option('--task_type', type=click.Choice(['Ess', 'NTH', 'BT', 'YNC', 'OGR'], case_sensitive=False),
              help='Type of task', prompt=True)
@click.option('--task', prompt='Task Name', type=str, help='Name of the task')
@click.option('--progress', type=click.Choice(['0', '1']), help='Progress of the task', prompt=True)
def add(task_type, task, progress):
    try:
        new_task_id = int(tmp_current.tail(1).index.values) + 1
    except:
        new_task_id = 0

    data = [
        {
            'task_id': new_task_id,
            'task_type': task_type,
            'task': task,
            'progress': progress,
            'date_created': date.today().strftime("%B %d, %Y")

        }
    ]

    line = pd.DataFrame(data)
    line.set_index('task_id', inplace=True)
    write_file(line, 'a', False)
    print(read_file(f'to-do-list/{date.today().strftime("%Y-%m-%d")}'))


@cli.command()
@click.option('--task_id', help='Task ID', prompt=True)
@click.option('--what', type=click.Choice(['task_type', 'task', 'progress']), help='Progress of the task', prompt=True)
@click.option('--value', help='What you want to change the cell to', prompt=True)
def update(task_id, what, value):
    file = f'to-do-list/{date.today().strftime("%Y-%m-%d")}'
    tmp_current.to_csv(f'{file}_undo.csv', index=True, sep=',', mode='w', header=True)
    tmp_new = tmp_current
    tmp_new.at[int(task_id), what] = value
    print(tmp_new)
    tmp_new.to_csv(f'{file}.csv', index=True, sep=',', mode='w', header=True)


@cli.command()
@click.option('--task_id', help='Task ID', prompt=True)
def remove(task_id):
    tmp_new = tmp_current
    tmp_new = tmp_new[tmp_new.index != int(task_id)]
    print(tmp_new)
    write_file(tmp_new, 'w', True)


# @cli.command()
# @click.argument('PATH', type=click.Path(resolve_path=True))
# def install(path):
#
#     paths = save_location
#
#     try:
#         os.mkdir(paths)
#         print(paths)
#     except OSError as error:
#         print(error)
#
#     filename = date.today().strftime("%Y-%m-%d")
#     with open(f'{path + directory}/{filename}.csv', 'w') as file:
#         file.write('task_id,task_type,task,progress,date_created\n')
#
#     with open(f'setting.txt', 'w') as file:
#         file.write(f'PATH = {paths}')
#
#     config['Folder'] = {'location': f'{path}',
#                         'name': f'{directory}'}
#
#     with open('config.ini', 'w') as configfile:
#         config.write(configfile)
def write_file(dataframe, mode, header):
    file = f'to-do-list/{date.today().strftime("%Y-%m-%d")}'
    dataframe.to_csv(f'{file}.csv', index=True, sep=',', mode=mode, header=header)
    tmp_current.to_csv(f'{file}_undo.csv', index=True, sep=',', mode='w', header=True)


def read_file(file):
    file = pd.read_csv(f'{file}.csv', index_col='task_id')
    return file


def file_check():
    flag = 0
    file_name = os.listdir("to-do-list/")
    for f in file_name:
        if f == f'{date.today().strftime("%Y-%m-%d")}.csv':
            flag = 1
    if flag == 0:
        filename = date.today().strftime("%Y-%m-%d")
        filename = save_location + filename
        with open(f'{filename}.csv', 'w') as file:
            file.write('task_id,task_type,task,progress,date_created\n')


@cli.command()
def test():
    print('This is a test function')
    print(read_file(f'to-do-list/{date.today().strftime("%Y-%m-%d")}'))


@cli.command()
def undo():
    tmp_new = read_file(f'to-do-list/{date.today().strftime("%Y-%m-%d")}_undo')
    print(tmp_new)
    write_file(tmp_new, 'w', True)


if __name__ == '__main__':
    config = configparser.ConfigParser()  # loads config into global variable
    config.read('config.ini')  # sets to read config file
    save_location = config['Folder']['location'] + config['Folder'][
        'name'] + '/'  # loads directory location from config
    file_check()  # checks for today's list and if not then creates one
    tmp_current = read_file(f'to-do-list/{date.today().strftime("%Y-%m-%d")}')  # loads file into a temporary storage
    print(tmp_current)  # prints current file to command line before altering it
    cli()  # starts command line interface command functions
