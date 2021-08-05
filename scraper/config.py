"""configuration module loads from yaml config."""
import logging
import os

import yaml


class Config(object):

  def __init__(self, conf_path: str):
    self.config_path = conf_path
    with open(conf_path) as file:
      self.config = yaml.load(file, Loader=yaml.FullLoader)

    self.log_dir = self.config['logDir']
    self.log_level = self.config['logLevel']

    self.interval = int(self.config['crawler']['intervalSeconds'])
    self.scrapy_settings_module = self.config['crawler']['scrapySettingsModule']
    os.environ['SCRAPY_SETTINGS_MODULE'] = self.scrapy_settings_module
    self.bots = self.config['crawler']['bots']

    self.notification_throttling = int(self.config['notification']['throttling'])
    self.telegram_token = self.config['notification']['telegram']['token']
    self.telegram_chat_id = self.config['notification']['telegram']['chatId']

  def reload(self):
    self.__init__(self.config_path)
