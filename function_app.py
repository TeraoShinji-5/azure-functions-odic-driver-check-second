import azure.functions as func
# import datetime
# import json
# import logging

# import pandas as pd
# import numpy as np
import pyodbc
# import requests


# ------ローカルファイルパス追加-----
# import os
# import sys
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# if BASE_DIR not in sys.path:
#     sys.path.insert(0, BASE_DIR) # 優先度上げる
# ------ローカルファイル読み込み-----
# from index_search_update import index_search_update

# ------azure function関数-----
app = func.FunctionApp()
# cron_schedule = "0 0 0 1 1 *"
# cron_schedule = "0 */5 * * * *" #5分ごと
cron_schedule = "0 */1 * * * *" #1分ごと
# cron_schedule = "0 0 18 * * *" # 毎日 JST 03:00 → UTC 18:00
# cron_schedule = "0 0 18 * * 6" # 毎週日曜 JST 03:00 → UTC 土曜 18:00

@app.timer_trigger(schedule=cron_schedule, arg_name="myTimer", run_on_startup=False,use_monitor=False) 
def CrudTimerTrigger3(myTimer: func.TimerRequest) -> None:

    # import requests
    # import os
    # import pyodbc
    # import pandas as pd
    # import numpy as np
    # import time
    # import logging

    # is_late_for_schedule = myTimer.past_due
    # if is_late_for_schedule:
    #     logging.info('The timer is past due!') # 指定した時間よりも遅れて実行の場合

    # logging.info('Python timer trigger function executed.')
    # index_search_update()


    # LOG_URL = os.environ.get("LOG_URL","")
    # logging.info('Python timer trigger function executed.aaaaaaaaaaaaaaaaaaa')
    # print('ppppppppppppppppprint')
    # print(LOG_URL)
    # print('ppppppppppppppppprint2')
    # url = LOG_URL
    
    # headers = {'content-type': 'application/json'}
    # data = {
    #     "col_1":"log送信テスト",
    #     "col_2":"log送信テスト",
    #     "col_3":"log送信テスト",
    #     "col_4":"log送信テスト",
    #     "col_5":"log送信テスト",
    #     "col_6":"log送信テスト",
    #     "col_7":"log送信テスト",
    # }
    # res_auth = requests.post(url=url,headers=headers,json=data)
    # res_auth.text

    pass
