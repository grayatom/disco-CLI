import click
import requests
from .helper import generate_table, print_timeline, viewlog
import json
import asyncio
from .query_builder import get_filter_list, get_field_str
from .config import USER_EMAIL
from .__init__ import __version__
# USER_EMAIL = 'bhargav@hyperverge.co'

@click.group()
@click.version_option(__version__)
def cli():
    """WELCOME TO DISCO!"""


@cli.command()
def whoami():
    click.echo(USER_EMAIL)


@cli.command()
@click.option('--filter','job_filters', type=str, default=(), \
    multiple=True, help='accepted value of a filter is A=B')
@click.option('--attributes', type=str, default=None, help='accepted input format = attr1,attr2,attr3'\
    ' i.e. comma separated values without space')
@click.option('--json', 'print_in_json', is_flag=True, help='use this flag to print list in JSON format')
def list(job_filters, attributes, print_in_json):
    filter_list_for_api = get_filter_list(job_filters)
    fields_str_for_api = get_field_str(attributes)
    if filter_list_for_api == False or fields_str_for_api == False:
        return
    payload = {
        'filter': filter_list_for_api,
        'fields': fields_str_for_api
    }
    try:
        response = requests.get('http://disco-dbface.dev.hyperverge.org:5000/job',\
            params=payload, timeout=100)
        jobs = response.json().get('result')
        # print(jobs)
        if not jobs:
            click.echo('no jobs found')
        else:
            if print_in_json:
                click.echo(json.dumps(jobs, indent=4))
            # print in tabular format (default)
            else:
                table = generate_table(jobs, attributes)
                click.echo(table)
            
    except Exception as e:
        print(f'{e.__class__.__name__}: {e}')


@cli.command()
@click.argument('job_id', type=str, required=True)
def describe(job_id):
    payload = {
        'filter': [f'UserDetails.Email:{USER_EMAIL}', f'_id:{job_id}']
    }
    try:
        response = requests.get('http://disco-dbface.dev.hyperverge.org:5000/job',\
            params=payload, timeout=100)
        job = response.json().get('result')
        if not job:
            click.echo(f'no job found for job_id "{job_id}"')
        else:
            click.echo(json.dumps(job, indent=4))
    except Exception as e:
        print(f'{e.__class__.__name__}: {e}')


@cli.command()
@click.argument('job_id', type=str, required=True)
def status(job_id):
    payload = {
        'filter': [f'UserDetails.Email:{USER_EMAIL}', f'_id:{job_id}'],
    }
    try:
        response = requests.get('http://disco-dbface.dev.hyperverge.org:5000/job',\
            params=payload, timeout=100)
        job = response.json().get('result')
        if not job:
            click.echo(f'no job found for job_id "{job_id}"')
        else:
            click.echo(print_timeline(job[0]))
    except Exception as e:
        print(f'{e.__class__.__name__}: {e}')


@cli.command()
@click.argument('job_id', type=str, required=True)
@click.option('--tail', is_flag=True)
def log(job_id, tail):
    tail_val = '1' if tail else '0'
    asyncio.get_event_loop().run_until_complete(viewlog(job_id, tail_val))







