import os, sys

basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
activate_this = ("%s/warch/venv/Scripts/activate_this.py" if os.name == 'nt' else "%s/warch/venv/bin/activate_this.py") % basedir
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

sys.path.append(basedir)
sys.path.append(basedir + '/warch/apps')

from werkzeug.exceptions import NotFound
from werkzeug.middleware.dispatcher import DispatcherMiddleware

from warch_decision import app as decision_app
from warch_registry import app as registry_app
from warch_personalities import app as personalities_app

application = DispatcherMiddleware(NotFound(), {
    '/_decision': decision_app.create_app(),
    '/_registry': registry_app.create_app(),
    '/_personalities': personalities_app.create_app()
})
