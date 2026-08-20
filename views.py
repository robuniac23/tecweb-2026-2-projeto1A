from urllib.parse import unquote_plus
from utils import extract_route, read_file, load_data, load_template, save_note, build_response


def index(request):
    # A string de request sempre começa com o tipo da requisição (ex: GET, POST)
    if request.startswith('POST'):
        request = request.replace('\r', '')  # Remove caracteres indesejados
        partes = request.split('\n\n')
        corpo = partes[1]
        params = {}
        for chave_valor in corpo.split('&'):
            chave, valor = chave_valor.split('=', 1)
            params[chave] = unquote_plus(valor)

        save_note(params['titulo'], params['detalhes'])

        return build_response(code=303, reason='See Other', headers='Location: /')

    # Monta a lista de anotações
    note_template = load_template('components/note.html')
    notes_li = []
    for dados in load_data('notes.json'):
        notes_li.append(note_template.format(title=dados['titulo'], details=dados['detalhes']))
    notes = '\n'.join(notes_li)

    # Monta a página final
    return build_response(load_template('index.html').format(notes=notes))