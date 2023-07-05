from fabric.api import local
from datetime import datetime

def do_pack():
    local("mkdir -p versions")
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = "versions/web_static_{}.tgz".format(time)
    result = local("tar -cvzf {} web_static".format(file_name))
    if result.failed:
        return None
    return file_name
