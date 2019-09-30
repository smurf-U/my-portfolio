from app import app
from socket import gethostname

if __name__ == '__main__':
    db.create_all()
    if 'liveconsole' not in gethostname():
        app.run(host='0.0.0.0', port=8080)
