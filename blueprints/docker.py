
import flask
import docker

blueprint = flask.Blueprint('docker', __name__)

connection = docker.DockerClient()

@blueprint.route('/docker', methods=[ 'GET' ])
def get_docker():

	'''for container in connection.containers.list(all=True):
		print(container.id, container.name)'''

	container = connection.containers.get('c615b9b861c3')

	context = {
		'page': 'docker',
		'route': {
			'is_public': False
		},
		'container': container
	}

	return flask.render_template('docker.html', context=context)

@blueprint.route('/docker/start', methods=[ 'GET' ])
def start_docker():

	container = connection.containers.get('c615b9b861c3')

	if not container:
		flask.flash('Container nao encontrado', 'danger')

	elif container.status != 'running':
		container.start()
		flask.flash('Container iniciado', 'success')
	else:
		flask.flash('Container ja esta iniciado', 'info')

	return flask.redirect('/docker')

@blueprint.route('/docker/stop', methods=[ 'GET' ])
def stop_docker():

	container = connection.containers.get('c615b9b861c3')

	if not container:
		flask.flash('Container nao encontrado', 'danger')

	elif container.status != 'exited':
		container.stop()
		flask.flash('Container parado', 'success')
	else:
		flask.flash('Container ja esta parado', 'info')

	return flask.redirect('/docker')