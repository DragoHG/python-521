
import flask
import docker
import services.login_required

blueprint = flask.Blueprint('docker', __name__)

connection = docker.DockerClient()

@blueprint.route('/docker', methods=[ 'GET' ])
@services.login_required.login_required
@services.login_required.log_access
def get_docker():    
	
	context = {
		'page': 'docker',
		'route': {
			'is_public': False
		},
		'containers': connection.containers.list(all=True)
	}

	return flask.render_template('docker.html', context=context)

@blueprint.route('/docker/start/<string:containerid>', methods=[ 'GET' ])
def start_docker(containerid):
	try:
		container = connection.containers.get(containerid)
		container.start()
	except:
		pass
	return flask.redirect('/docker')

@blueprint.route('/docker/stop/<string:containerid>', methods=[ 'GET' ])
def stop_docker(containerid):
	try:
		container = connection.containers.get(containerid)
		container.stop()
	except:
		pass
	return flask.redirect('/docker')
