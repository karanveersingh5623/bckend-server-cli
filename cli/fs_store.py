import click
import requests
import os

SERVER_URL = 'http://127.0.0.1:5000'

@click.group()
def cli():
    """File Storage CLI"""
    pass

@cli.command()
@click.argument('file_path', type=click.Path(exists=True))
def upload_file(file_path):
    """Upload a file to the server"""
    filename = os.path.basename(file_path)
    with open(file_path, 'rb') as f:
        files = {'file': (filename, f)}
        response = requests.post(f'{SERVER_URL}/files/{filename}',
                                 files=files)
    click.echo(response.text)

@cli.command()
@click.argument('filename')
def delete_file(filename):
    """Delete a file from the server"""
    response = requests.delete(f'{SERVER_URL}/files/{filename}')
    click.echo(response.text)

@cli.command()
def list_files():
    """List all files on the server"""
    response = requests.get(f'{SERVER_URL}/files')
    if response.status_code == 200:
        files = response.json()
        for f in files:
            click.echo(f)
    else:
        click.echo('Failed to retrieve file list')
