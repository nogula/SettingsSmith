import os
from SettingsSmith import Settings

settings_file = os.path.join(os.path.dirname(__file__), "default_settings.json")
settings = Settings(
    default_settings=settings_file,
    app_name="TestApp",
    app_version="1.0",
    overwrite=True,
)

print(settings.get())

settings.set("new_value", "key1", "key2")
print(settings.get())

settings.set(123)
print(settings.get())

print(settings.config_file)