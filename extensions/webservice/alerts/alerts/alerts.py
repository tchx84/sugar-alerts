import dbus
import logging

from gettext import gettext as _

from jarabe.model import notifications


class Alerts(object):

    DBUS_UPDATED_SIGNAL = 'Updated'
    DBUS_ALERTS_IFACE = 'org.sugarlabs.alerts'

    def __init__(self):
        logging.debug('Alerts.__init__')
        bus = dbus.SystemBus()
        bus.add_signal_receiver(self.__updated_cb,
                                self.DBUS_UPDATED_SIGNAL,
                                self.DBUS_ALERTS_IFACE)

    def __updated_cb(self):
        logging.debug('Alerts.__updated_cb')

        name = _('Updater')
        summary = _('Software Updates Installed')
        body = _('Important updates have been installed. '
                 'restart your laptop to activate'
                 ' these updates.')
        hints = {'x-sugar-icon-name': 'module-updater'}

        self._alert(name, summary, body, hints)

    def _alert(self, name, summary, body, hints):
        service = notifications.get_service()
        service.Notify(name, 0, '', summary, body, [], hints, -1)
