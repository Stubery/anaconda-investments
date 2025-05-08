import os


def fetch_resource_path(resource_path):
    return ("resources/%s" % resource_path) if os.getcwd().endswith("anaconda-investments") else (
            "../resources/%s" % resource_path)