
class Config:
    DEBUG = False
    TESTING = False
    
    HOST = '0.0.0.0'
    PORT = 8081

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    HOST = '0.0.0.0'

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}


