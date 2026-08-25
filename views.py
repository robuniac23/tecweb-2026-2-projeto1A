from urllib.parse import unquote_plus
from utils import extract_route, read_file, load_template, build_response
from database import Database, Note

db = Database('banco')

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

        db.add(Note(title=params['titulo'], content=params['detalhes']))

        return build_response(code=303, reason='See Other', headers='Location: /')

    # Monta a lista de anotações
    note_template = load_template('components/note.html')
    notes_li = []
    for nota in db.get_all():
        notes_li.append(note_template.format(id=nota.id, title=nota.title, details=nota.content))
    notes = '\n'.join(notes_li)

    # Monta a página final
    return build_response(load_template('index.html').format(notes=notes))


def deletar(request, note_id):
    db.delete(note_id)
    return build_response(code=303, reason='See Other', headers='Location: /')