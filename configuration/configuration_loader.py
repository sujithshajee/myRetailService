import os
import logging
import yaml


def app_config(existing_config):
    try:
        config_path = os.path.join(os.path.dirname(
            os.path.realpath(__file__)), "application_config.yaml")
        with open(config_path) as f:
            config = yaml.load(f, Loader=yaml.FullLoader)
    except IOError:
        raise ValueError(
            "Failed to load Configuration File from {0}".format(config_path))
    except Exception as e:
        raise ValueError("Invalid YAML configuration file format.")
    existing_config.update(config)


def app(flask_app):
    app_config(flask_app.config)
