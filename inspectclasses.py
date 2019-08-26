import inspect
import pkgutil
import os
import importlib


def find_classes(module_name, package_name=None):
    try:
        module = importlib.import_module(
            name=f'{package_name}.{module_name}' if package_name else module_name,
            package=package_name
        )
    except ImportError:
        print(f'lolwut{module_name} {package_name}')
        raise

    return [member for _, member in inspect.getmembers(module) if inspect.isclass(member)]


def find_module_names(package_path):
    return [modname for importer, modname, ispkg in pkgutil.iter_modules(path=[package_path])]


def main():
    import modularrh
    module_path = str(os.path.dirname(modularrh.__file__))
    module_names = find_module_names(module_path)
    for module_name in module_names:
        print(find_classes(module_name, modularrh.__name__))


if __name__ == '__main__':
    main()
