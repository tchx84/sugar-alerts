from jarabe.webservice import account

from alerts.alerts import Alerts


class Account(account.Account):

    def __init__(self):
        self._alerts_manager = Alerts()

    def get_token_state(self):
        return self.STATE_VALID


def get_account():
    return Account()
