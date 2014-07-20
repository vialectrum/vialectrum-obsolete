#!/usr/bin/python

# python setup.py sdist --format=zip,gztar

from setuptools import setup
import os
import sys
import platform
import imp


version = imp.load_source('version', 'lib/version.py')
util = imp.load_source('version', 'lib/util.py')

if sys.version_info[:3] < (2, 6, 0):
    sys.exit("Error: Electrum requires Python version >= 2.6.0...")

usr_share = '/usr/share'
if not os.access(usr_share, os.W_OK):
    usr_share = os.getenv("XDG_DATA_HOME", os.path.join(os.getenv("HOME"), ".local", "share"))

data_files = []
if (len(sys.argv) > 1 and (sys.argv[1] == "sdist")) or (platform.system() != 'Windows' and platform.system() != 'Darwin'):
    print "Including all files"
    data_files += [
        (os.path.join(usr_share, 'applications/'), ['vialectrum.desktop']),
        (os.path.join(usr_share, 'app-install', 'icons/'), ['icons/vialectrum.png'])
    ]
    if not os.path.exists('locale'):
        os.mkdir('locale')
    for lang in os.listdir('locale'):
        if os.path.exists('locale/%s/LC_MESSAGES/electrum.mo' % lang):
            data_files.append((os.path.join(usr_share, 'locale/%s/LC_MESSAGES' % lang), ['locale/%s/LC_MESSAGES/electrum.mo' % lang]))

appdata_dir = util.appdata_dir()
if not os.access(appdata_dir, os.W_OK):
    appdata_dir = os.path.join(usr_share, "vialectrum")

data_files += [
    (appdata_dir, ["data/README"]),
    (os.path.join(appdata_dir, "cleanlook"), [
        "data/cleanlook/name.cfg",
        "data/cleanlook/style.css"
    ]),
    (os.path.join(appdata_dir, "sahara"), [
        "data/sahara/name.cfg",
        "data/sahara/style.css"
    ]),
    (os.path.join(appdata_dir, "dark"), [
        "data/dark/name.cfg",
        "data/dark/style.css"
    ])
]


setup(
    name="Vialectrum",
    version=version.ELECTRUM_VERSION,
    install_requires=['slowaes', 'ecdsa>=0.9', 'pbkdf2', 'requests', 'pyasn1', 'pyasn1-modules', 'tlslite>=0.4.5', 'qrcode', 'ltc_scrypt'],
    package_dir={
        'vialectrum': 'lib',
        'vialectrum_gui': 'gui',
        'vialectrum_plugins': 'plugins',
    },
    scripts=['vialectrum'],
    data_files=data_files,
    py_modules=[
        'vialectrum.account',
        'vialectrum.bitcoin',
        'vialectrum.blockchain',
        'vialectrum.bmp',
        'vialectrum.commands',
        'vialectrum.daemon',
        'vialectrum.i18n',
        'vialectrum.interface',
        'vialectrum.mnemonic',
        'vialectrum.msqr',
        'vialectrum.network',
        'vialectrum.paymentrequest',
        'vialectrum.paymentrequest_pb2',
        'vialectrum.plugins',
        'vialectrum.scrypt',
        'vialectrum.simple_config',
        'vialectrum.socks',
        'vialectrum.synchronizer',
        'vialectrum.transaction',
        'vialectrum.util',
        'vialectrum.verifier',
        'vialectrum.version',
        'vialectrum.wallet',
        'vialectrum.wallet_bitkey',
        'vialectrum.x509',
        'vialectrum_gui.gtk',
        'vialectrum_gui.qt.__init__',
        'vialectrum_gui.qt.amountedit',
        'vialectrum_gui.qt.console',
        'vialectrum_gui.qt.history_widget',
        'vialectrum_gui.qt.icons_rc',
        'vialectrum_gui.qt.installwizard',
        'vialectrum_gui.qt.lite_window',
        'vialectrum_gui.qt.main_window',
        'vialectrum_gui.qt.network_dialog',
        'vialectrum_gui.qt.password_dialog',
        'vialectrum_gui.qt.paytoedit',
        'vialectrum_gui.qt.qrcodewidget',
        'vialectrum_gui.qt.qrtextedit',
        'vialectrum_gui.qt.receiving_widget',
        'vialectrum_gui.qt.seed_dialog',
        'vialectrum_gui.qt.transaction_dialog',
        'vialectrum_gui.qt.util',
        'vialectrum_gui.qt.version_getter',
        'vialectrum_gui.stdio',
        'vialectrum_gui.text',
        'vialectrum_plugins.exchange_rate',
        'vialectrum_plugins.labels',
        'vialectrum_plugins.pointofsale',
        'vialectrum_plugins.qrscanner',
        'vialectrum_plugins.virtualkeyboard',
    ],
    description="Lightweight Viacoin Wallet",
    author="Thomas Voegtlin",
    author_email="thomasv1@gmx.de",
    license="GNU GPLv3",
    url="http://vialectrum.org",
    long_description="""Lightweight Viacoin Wallet"""
)
