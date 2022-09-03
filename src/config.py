
class Config(object):
    """The base config class
    Contains the default config
    """
    DEBUG = False
    TESTING = False

class ProductionConfig(Config):
    """Production Config class
    Necessary configuration for production
    """

class DevelopmentConfig(Config):
    """Developement Config class
    Necessary configuration for development
    """
    DEBUG = True

class TestingConfig(Config):
    """Testing Config class
    Necessary configuration for Testing
    """
    TESTING = True