import dbus
import logging

from gettext import gettext as _

from jarabe.model import notifications


class Alerts(object):

    DBUS_UPDATED_SIGNAL = 'Updated'
    DBUS_UPDATED_REBOOT_SIGNAL = 'UpdatedReboot'
    DBUS_ALERTS_IFACE = 'org.dextrose.updater'

    def __init__(self):
        logging.debug('Alerts.__init__')
        bus = dbus.SystemBus()
        bus.add_signal_receiver(self.__updated_cb,
                                self.DBUS_UPDATED_SIGNAL,
                                self.DBUS_ALERTS_IFACE)
        bus.add_signal_receiver(self.__updated_reboot_cb,
                                self.DBUS_UPDATED_REBOOT_SIGNAL,
                                self.DBUS_ALERTS_IFACE)

    def __updated_cb(self):
        logging.debug('Alerts.__updated_cb')
        self._alert_updated()

    def __updated_reboot_cb(self):
        logging.debug('Alerts.__updated_reboot_cb')
        self._alert_updated(reboot=True)

    def _alert_updated(self, reboot=False):
        name = _('Software Updater')
        summary = _('Software updates installed')
        body = _('Your laptop has been updated with the latest software.')

        if reboot is True:
            body += _(' Please restart your laptop to take advantage of'
                      ' of these updates.')

        hints = {'x-sugar-icon-name': 'module-updater'}

        self._alert(name, summary, body, hints)

    def _alert(self, name, summary, body, hints):
        service = notifications.get_service()
        service.Notify(name, 0, '', summary, body, [], hints, -1)
