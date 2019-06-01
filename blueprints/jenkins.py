
import flask
import jenkins

blueprint = flask.Blueprint('jenkins', __name__)

URL = 'http://localhost:8080'
USER = '4linux'
PASSWD = '123'

connection = jenkins.Jenkins(URL, USER, PASSWD)

@blueprint.route('/jenkins', methods=[ 'GET' ])
def get_jenkins():
	
	context = {
		'page': 'jenkins',
		'route': {
			'is_public': False
		},
		'jobs': [
			connection.get_job_info(j['name'])
				for j in connection.get_jobs()
		]
	}

	return flask.render_template('jenkins.html', context=context)

@blueprint.route('/jenkins', methods=[ 'GET' ])
def post_jenkins():
	pass

@blueprint.route('/jenkins/update/<string:jobname>', methods=[ 'GET' ])
def get_jenkins_update(jobname):
	
	context = {
		'page': 'jenkins-update',
		'route': {
			'is_public': False
		},
		'job': {
		'name': jobname,
		'xml': connection.get_job_config(jobname)
		}
	}

	return flask.render_template('jenkins_update.html', context=context)

@blueprint.route('/jenkins/build/<string:jobname>', methods=[ 'GET' ])
def get_jenkins_build(jobname):
	connection.build_job(jobname)

	return flask.redirect('/jenkins')