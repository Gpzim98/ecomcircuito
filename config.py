DB_NAME = "setme"
ARCHIVE_FILES = "setme"
ARCHIVE_FILED_FILES = "setme"
DIRECTORY_TO_WATCH = "setme"

ECOM_DB_HOST = "setme"
ECOM_DB_NAME = "setme"
ECOM_DB_USER = "setme"
ECOM_DB_PASSWORD = "setme"


try:
    import local_settings
    DB_NAME = local_settings.DB_NAME
    ARCHIVE_FILES = local_settings.ARCHIVE_FILES
    ARCHIVE_FILED_FILES = local_settings.ARCHIVE_FILED_FILES
    DIRECTORY_TO_WATCH = local_settings.DIRECTORY_TO_WATCH

    ECOM_DB_HOST = local_settings.ECOM_DB_HOST
    ECOM_DB_NAME = local_settings.ECOM_DB_NAME
    ECOM_DB_USER = local_settings.ECOM_DB_USER
    ECOM_DB_PASSWORD = local_settings.ECOM_DB_PASSWORD
except Exception as e:
    print("Failed to import and process local_settings: " + str(e))
