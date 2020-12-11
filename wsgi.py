import os, sys
from werkzeug.exceptions import NotFound
from werkzeug.middleware.dispatcher import DispatcherMiddleware

basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.append(basedir + '/warch/apps')

from apps.warch_decision.wsgi import application as decision_app
from apps.warch_registry.wsgi import application as registry_app

application = DispatcherMiddleware(NotFound(), {
    '/_decision': decision_app,
    '/_registry': registry_app
})
