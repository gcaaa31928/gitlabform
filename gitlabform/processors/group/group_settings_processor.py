import logging

import cli_ui

from gitlabform.gitlab import GitLab
from gitlabform.processors.abstract_processor import AbstractProcessor


class GroupSettingsProcessor(AbstractProcessor):
    def __init__(self, gitlab: GitLab):
        super().__init__("group_settings", gitlab)

    def _process_configuration(self, group: str, configuration: dict):
        group_settings = configuration["group_settings"]
        logging.debug(
            "Group settings BEFORE: %s", self.gitlab.get_group_settings(group)
        )
        cli_ui.debug(f"Setting group settings: {group_settings}")
        self.gitlab.put_group_settings(group, group_settings)
        logging.debug("Group settings AFTER: %s", self.gitlab.get_group_settings(group))
