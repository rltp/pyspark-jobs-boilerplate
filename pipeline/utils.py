
import pkg_resources

def filepath(path):
    return pkg_resources.resource_filename(__name__, path)

def listdir(path):
    return pkg_resources.resource_listdir(__name__, path)