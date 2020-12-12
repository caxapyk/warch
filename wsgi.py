import os, sys
from werkzeug.exceptions import NotFound
from werkzeug.middleware.dispatcher import DispatcherMiddleware

basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.append(basedir)

activate_this = "%s/warch/venv/bin/activate_this.py" % basedir
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

sys.path.append(basedir + '/warch/apps')

from warch_decision import app as decision_app
from warch_registry import app as registry_app

application = DispatcherMiddleware(NotFound(), {
    '/_decision': decision_app.create_app(),
    '/_registry': registry_app.create_app()
})
