from pathlib import Path
import json

CUR_DIR = Path(__file__).parent

def extract_route(request):

    first_line = request.split('\n')[0]

    method, path, protocol = first_line.split(' ')
    
    route = path[1:]
    
    return route

def read_file(filepath):
    with open(filepath, 'rb') as file:
        content = file.read()
    return content


def load_template(filename):
    filepath = Path('templates') / filename
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
    return content


def build_response(body='', code=200, reason='OK', headers=''):
    response_line = f'HTTP/1.1 {code} {reason}\n'

    if headers:
        response = (response_line + headers + '\n\n').encode()
    else:
        response = (response_line + '\n').encode()

    if isinstance(body, bytes):
        response += body
    else:
        response += body.encode()

    return response