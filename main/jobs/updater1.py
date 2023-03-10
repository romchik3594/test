from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .job1 import scheduler_api
from .job2 import scheduler_api2

def start():
    scheduler = BackgroundScheduler()
    #scheduler.add_job(scheduler_api, 'interval', seconds = 10, max_instances=100)
    #scheduler.add_job(scheduler_api2, 'interval', seconds = 10, max_instances=100)
    scheduler.start()