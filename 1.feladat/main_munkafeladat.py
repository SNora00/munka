from fastapi import FastAPI
from datetime import date, datetime
from models_munkafeladat import My_Time
import locale
import sys
import uvicorn

weekdays = {
  0: "Hétfő",
  1: "Kedd",
  2: "Szerda",
  3: "Csütörtök",
  4: "Péntek",
  5: "Szombat",
  6: "Vasárnap"
}

locale.setlocale(locale.LC_ALL, 'hun_hun')
app = FastAPI()

@app.get("/")
async def root():
    d = date.today()
    now = datetime.now()
    day_n = weekdays[d.weekday()]
    dt_string = now.strftime("%d/%m/%Y")
    db = My_Time(
        todays_day= day_n,
        todays_date= dt_string
    )
    return db


if __name__ == '__main__':
    custom_port = int(sys.argv[1])
    uvicorn.run(app, host='0.0.0.0', port=custom_port)