from slackstatus import get_cat_fact, update_status
import time
import schedule

# schedule.every(5).minutes.do(update_status_emoji)
def do_all_the_things():
    fact = get_cat_fact()
    update_status(fact)

schedule.every(1).minutes.do(do_all_the_things)

while True:
    schedule.run_pending()
    time.sleep(1)
