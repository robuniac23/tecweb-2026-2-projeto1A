from pathlib import Path

def extract_route(request):

    first_line = request.split('\n')[0]

    method, path, protocol = first_line.split(' ')
    
    route = path[1:]
    
    return route

request = "GET /img/logo-getit.png HTTP/1.1\nHost: 0.0.0.0:8080\nConnection: keep-alive"

print(extract_route(request)) 

def read_file(filepath):
    with open(filepath, 'rb') as file:
        content = file.read()
    return content

filepath = Path('img/logo-getit.png')
conteudo = read_file(filepath)
print(type(conteudo))