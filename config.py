from enum import Enum

# const
class Engine(Enum):
    SQLITE = 'sqlite'
    MYSQL = 'mysql'
    POSTGRESQL = 'postgresql'

# Database settings

DATABASE = {
    'DB_ENGINE': Engine.SQLITE,
    'DB_NAME': 'db.sqlite',
}


# theme settings

THEMES = {
    'THEME_CMS': 'default',
    'THEME_ADMIN': 'default',
}
