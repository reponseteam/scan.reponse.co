from pathlib import Path
import time
from subprocess import Popen
from app import app

if __name__ == '__main__':
    from app import db
    from utils.producer_insert_from_json import insert_producer
    # db.drop_all()
    db.create_all()
    insert_producer()
    db.session.commit()
    app.run(host='0.0.0.0', port=8080, debug=True)
