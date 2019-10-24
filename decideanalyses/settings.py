from environs import Env

env = Env()
env.read_env()

DATABASE_URL = env('DATABASE_URL')
DATA_SET_ID = env('DATA_SET_ID', default=1)
MODEL_RUN_IDS = env.list('MODEL_RUN_IDS', default=['1', '2'])
