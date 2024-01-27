#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers
"""
from fabric.api import env, put, run, local
from os.path import exists
from datetime import datetime

env.hosts = ['<IP web-01>', 'IP web-02']
env.user = '<your_username>'
env.key_filename = ['<your_ssh_key>']


def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        # Upload the archive to /tmp/ directory on the web server
        put(archive_path, '/tmp/')

        # Get the base filename of the archive without extension
        archive_filename = archive_path.split('/')[-1]
        archive_name = archive_filename.split('.')[0]

        # Create the release folder
        run('mkdir -p /data/web_static/releases/{}'.format(archive_name))

        # Uncompress the archive to the release folder
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'
            .format(archive_filename, archive_name))

        # Remove the uploaded archive
        run('rm /tmp/{}'.format(archive_filename))

        # Move the contents of the archive to the release folder
        run('''mv /data/web_static/releases/{}/
    web_static/* /data/web_static/releases/{}/'''
            .format(archive_name, archive_name))

        # Remove the web_static directory within the release folder
        run('rm -rf /data/web_static/releases/{}/web_static'.format(
            archive_name))

        # Remove the current symbolic link
        run('rm -rf /data/web_static/current')

        # Create a new symbolic link to the new version
        run('ln -s /data/web_static/releases/{}/ /data/web_static/current'
            .format(archive_name))

        print('New version deployed!')
        return True

    except Exception as e:
        print(e)
        return False


if __name__ == "__main__":
    # Example usage:
    archive_path = local("python3 1-pack_web_static.py", capture=True)
    result = do_deploy(archive_path)
    if not result:
        print("Deployment failed.")
