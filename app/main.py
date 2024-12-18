from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import sqlite3
import pandas as pd

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/plot-data")
def get_plot_data():
    conn = sqlite3.connect('epl.db')
    df = pd.read_sql_query("SELECT Season, Pos, Team, GD, Pts FROM premier_league", conn)
    data = df.to_dict('records')
    conn.close()
    return {"data": data}