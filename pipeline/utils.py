
import pkg_resources

def filepath(path):
    return pkg_resources.resource_filename(__name__, path)

def listdir(path):
    return pkg_resources.resource_listdir(__name__, path)

def subpackages(package):
    if "." in package:
        package, sub_pkg = package.split(".", 1)
    else:
        sub_pkg = "."
    if not pkg_resources.resource_isdir(package, sub_pkg):
        raise ModuleLoadError(f"Undefined package {package}")
    found = {}
    joiner = "" if sub_pkg == "." else f"{sub_pkg}."
    for sub_path in pkg_resources.resource_listdir(package, sub_pkg):
        if pkg_resources.resource_exists(
            package, f"{sub_pkg}/{sub_path}/__init__.py"
        ):
            found[sub_path] = f"{package}.{joiner}{sub_path}"
    return found
