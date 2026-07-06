class Config:
    def __init__(self):
        pass

    @staticmethod
    def get_trend_analysis_config() -> dict:
        return {
            'interval': 60,
            'threshold': 0.5
        }

    @staticmethod
    def get_red_teaming_config() -> dict:
        return {
            'interval': 60,
            'attacks': ['_attack1', '_attack2']
        }

    @staticmethod
    def get_autonomic_manager_config() -> dict:
        return {
            'interval': 60,
            'threshold': 0.5
        }