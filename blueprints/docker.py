
import flask
import docker

blueprint = flask.Blueprint('docker', __name__)

connection = docker.DockerClient()

@blueprint.route('/docker', methods=[ 'GET' ])
def get_docker():    
    
    context = {
        'page': 'docker',
        'route': {
            'is_public': False
        },
        'containers': connection.containers.list(all=True)
    }

    return flask.render_template('docker.html', context=context)

@blueprint.route('/docker/start', methods=[ 'GET' ])
def start_docker():

    return flask.redirect('/docker')

@blueprint.route('/docker/stop', methods=[ 'GET' ])
def stop_docker():

    return flask.redirect('/docker')
