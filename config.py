DB_NAME = "setme"
ARCHIVE_FILES = "setme"
ARCHIVE_FILED_FILES = "setme"
DIRECTORY_TO_WATCH = "setme"

try:
    import local_settings
    DB_NAME = local_settings.DB_NAME
    ARCHIVE_FILES = local_settings.ARCHIVE_FILES
    ARCHIVE_FILED_FILES = local_settings.ARCHIVE_FILED_FILES
    DIRECTORY_TO_WATCH = local_settings.DIRECTORY_TO_WATCH
except Exception as e:
    print("Failed to import and process local_settings: " + str(e))
