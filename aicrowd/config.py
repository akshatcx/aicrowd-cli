import os

import yaml

import pkg_resources

# Could be any dot-separated package/module name or a "Requirement"
resource_package = __name__

class Config:
    def __init__(self):
        template = pkg_resources.resource_stream(resource_package, 'default.yaml')
        self.settings = self.load(template)
        self.config_directory = self.settings['home_default']
        self.config_file = os.path.join(self.config_directory, "config.yaml")
        if (os.path.exists(self.config_file)):
            with open(self.config_file, "r") as f:
                self.settings = self.load(f)

    def load(self, stream):
        return yaml.load(stream, Loader=yaml.SafeLoader)

    def dump(self, content, fileobj):
        yaml.dump(content, fileobj, default_flow_style=False)

    def save(self):
        updated_list_doc = self.settings
        with open(self.config_file, "w") as f:
            self.dump(updated_list_doc, f)
            self.settings = updated_list_doc











