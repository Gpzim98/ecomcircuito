DB_NAME = "setme"
ARCHIVE_FILES = "setme"
ARCHIVE_FILED_FILES = "setme"

try:
    import local_settings
    DB_NAME = local_settings.DB_NAME
    ARCHIVE_FILES = local_settings.ARCHIVE_FILES
    ARCHIVE_FILED_FILES = local_settings.ARCHIVE_FILED_FILES
except Exception as e:
    print("Failed to import and process local_settings: " + str(e))
