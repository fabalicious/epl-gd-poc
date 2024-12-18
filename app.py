from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sqlite3
import pandas as pd

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins for now (you might want to restrict this in production)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/plot-data")
def get_plot_data():
    # Connect to SQLite database
    conn = sqlite3.connect('epl.db')
    
    # Query the database
    df = pd.read_sql_query("SELECT Pos, GD FROM premier_league", conn)
    
    # Convert to list of dictionaries for JSON response
    data = df.to_dict('records')
    
    # Close connection
    conn.close()
    
    return {"data": data}