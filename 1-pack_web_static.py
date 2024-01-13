#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the web_static
folder of your AirBnB Clone repo using the function do_pack.
"""

from fabric.api import local
from datetime import datetime
import os


@task
def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.

    Returns:
        str: Archive path if the archive has been correctly generated, None otherwise.
    """
    # Create the 'versions' folder if it doesn't exist
    local("mkdir -p versions")

    # Create the name of the archive
    archive_name = "web_static_{}.tgz".format(
        datetime.now().strftime('%Y%m%d%H%M%S'))

    # Compress files into the archive using tar
    result = local("tar -cvzf versions/{} web_static".format(archive_name))

    if result.succeeded:
        return "versions/{}".format(archive_name)
    else:
        return None
