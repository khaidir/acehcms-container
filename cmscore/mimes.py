import magic


def mimes(path):
    mime = magic.Magic(mime=True)
    mimetype = mime.from_file(path)

    if mimetype == 'text/plain':
        if path.endswith('.css'):
            return 'text/css'
        elif path.endswith('.js'):
            return 'text/javascript'

    return mimetype
