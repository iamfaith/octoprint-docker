cp /etc/systemd/system/octoprint_connect@.service

systemctl daemon-reload

lsusb -v | grep -iE '(^bus|idvendor|idproduct)'

/etc/udev/rules.d/3dprinter.rules


