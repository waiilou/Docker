from fastapi import FastAPI
from datetime import datetime, timedelta
from modules.parser import getip
app = FastAPI()

@app.get("/")
def get_current_time():

    current_time_utc = datetime.now()
    moscow_time = current_time_utc + timedelta(hours=3)
    utc7_time = current_time_utc + timedelta(hours=7)
    utc7_time_str = utc7_time.strftime("%H:%M")
    moscow_time_str = moscow_time.strftime("%H:%M")

    ip_address = getip()

    return {"Время по Барнаулу": utc7_time_str, "Время по Москве": moscow_time_str, "Текущий IP-Адрес": ip_address}
