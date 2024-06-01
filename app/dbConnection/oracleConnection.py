import oracledb
import os

config = os.getenv('CONFIG_OF_DB')
location = os.getenv('LOCATION_OF_THE_WALLET')

connection = oracledb.connect(
    user="ferramax", password="Oracle.12345", dsn="databaseduoc_medium",
    config_dir = config,
    wallet_location = location,
    wallet_password="Wallet.Ferramax1"
    )