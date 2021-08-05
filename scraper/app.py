import logging
import os
import time
from typing import Callable, Iterator, List, Optional, Union

import coloredlogs
import yaml
from scraper import config
from scrapy.crawler import CrawlerProcess, CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
from twisted.internet import defer, reactor
from twisted.internet.task import deferLater

from scraper import notification

coloredlogs.install()

os.environ['SCRAPY_SETTINGS_MODULE'] = 'ps5.ps5.settings'

process = CrawlerProcess(get_project_settings())

_DEFAULT_CONFIG_FILE = 'conf/scraper.yaml'


def sleep(*_, seconds):
  """Non blocking sleep callback"""
  return deferLater(reactor, seconds, lambda: None)


def run_crawlers(_, bot_list: List[str], interval: int):
  for bot in bot_list:
    deferred = process.crawl(bot)

  deferred.addCallback(lambda results: print(
      f'waiting {interval} seconds before next crawl...'))
  deferred.addCallback(sleep, seconds=interval)
  deferred.addCallback(run_crawlers, bot_list, interval)

  return deferred


def main():
  conf = config.Config(_DEFAULT_CONFIG_FILE)

  notif = notification.Notification(conf)
  # Need better impl instead of module patching
  notification.update_status = notif.update_status
  notif.send_message('Scraper started')

  run_crawlers(None, conf.bots, conf.interval)
  process.start()


if __name__ == "__main__":
  main()
