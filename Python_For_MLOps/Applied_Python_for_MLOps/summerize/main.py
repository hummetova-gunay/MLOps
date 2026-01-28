import click
from transformers import pipeline
import urllib.request
from bs4 import BeautifulSoup

def extract_from_url(url):
    text = ""
    req = urllib.request.Request(
        url, data=None,
        headers={
            'User=Agent': 'Mozilla/5.0.............'
        }
    )
    html = urllib.request.urlopen(req)
    parser = BeautifulSoup(html, 'html.parser')
    for paragraph in parser.find_all('p'):
        print(paragraph.text)
        text+=paragraph.text
    return text


def process(text):
    summerizer = pipeline('summerization', model = 't5-small')
    result = summerizer(text, max_length = 180)
    click.echo('Summerization process complete')
    click.echo('='*80)
    return result[0]['summary_text']

@click.command()
@click.option('--url')
@click.option('--file')
def main(url, file):
    if url:
        text = extract_from_url(url)
    elif file:
        with open(file, 'r') as _f:
            text = _f.read()
        
    click.echo(f'Summarized text from -> {url or file}')
    click.echo(process(text))