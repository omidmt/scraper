import logging
import os
import sys
from collections import defaultdict

from scrapy.http import Response

from scraper import telegram_bot
from scraper import config


class Notification(object):
  """Notification and status check class."""

  def __init__(self, config: config.Config):
    self.config = config
    self._providers_sent_count = defaultdict(int)

  def update_status(self,
                    provider: str,
                    in_stock: bool,
                    page: str = None,
                    response: Response = None):
    """Updates internal status of the provider and send notification."""

    logging.debug(
        f'>>>> Update status of {provider}/{page} inStock: {in_stock}')

    if in_stock:
      filename = f'{self.config.log_dir}/stock-{provider}-{page}.html'

      if self._providers_sent_count[provider] < self.config.notification_throttling:
        print('******************************')
        self.notify(f'In Stock @ {provider}\n{response.url}')
      else:
        logging.info('throttling notification for %s', provider)

      self._providers_sent_count[provider] += 1

    else:
      filename = f'{self.config.log_dir}/{provider}-{page}.html'

      if self._providers_sent_count[provider] > 0:
        self.notify(f'Stockout {provider}')
      self._providers_sent_count[provider] = 0

    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'wb') as f:
      f.write(response.body)
    logging.info('Saved file %s', filename)

  def notify(self, msg: str):
    try:
      telegram_bot.send(messages=[msg],
                        token=self.config.telegram_token,
                        chat_id=self.config.telegram_chat_id)
    # pylint: disable-broad-except
    except Exception as ex:
      # ex = sys.exc_info()[0]
      logging.error('sending telegram message failed: %s', str(ex))

  def send_message(self, msg: str):
    telegram_bot.send(messages=[msg],
                      token=self.config.telegram_token,
                      chat_id=self.config.telegram_chat_id)
