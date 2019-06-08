
import flask
import requests

blueprint = flask.Blueprint('gitlab', __name__)

BITOKEN = 'qVa7oJn9z_79hHM7CzAB'
DOMAIN = 'https://gitlab.com/api/v4'
PROJECTS_URL = DOMAIN + '/projects?owned=true&private_token=' + BITOKEN

@blueprint.route('/gitlab', methods=[ 'GET' ])
def get_gitlab():
	
	context = {
		'page': 'gitlab',
		'current_tab': flask.request.args.get('current_tab') or 'users',
		'route': {
			'is_public': False
		},
		'projects': requests.get(PROJECTS_URL).json()
	}

	return flask.render_template('gitlab.html', context=context)

@blueprint.route('/gitlab/<int:projectid>/commits', methods=[ 'GET' ])
def get_commits(projectid):

	REPOCOMMITS = DOMAIN + '/projects/' + str(projectid) + '/repository/commits?private_token=' + BITOKEN
	
	context = {
		'page': 'gitlab',
		'current_tab': flask.request.args.get('current_tab') or 'projects',
		'route': {
			'is_public': False
		},
		'repocommits': requests.get(REPOCOMMITS).json()
	}

	return flask.render_template('gitlab.html', context=context)