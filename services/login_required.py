import functools
import logging
import flask

logging.basicConfig(
	filename='app.log',
	level=logging.DEBUG,
	datefmt='[%d/%m/%Y %H:%M:%S]',
	format='%(asctime)s [%(levelname)s] %(name)s' +
	 '[%(funcName)s] [%(filename)s], %(lineno)s %(message)s'
)

def log_access(function):
	@functools.wraps(function)
	def wrapper(*args, **kwargs):
		message = flask.session.get('email') or 'Não autorizado'
		logging.debug(message)
		return function(*args, **kwargs)
	return wrapper

def login_required(function):
	@functools.wraps(function)
	def wrapper(*args, **kwargs):
		if 'email' not in flask.session:
			flask.flash('Login necessario', 'danger')
			return flask.redirect('/sign-in')
		return function(*args, **kwargs)
	return wrapper