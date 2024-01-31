from fastapi import FastAPI
from data.getData import Get_Data as gd

app = FastAPI()

@app.get("/power_demand")
def index():
    gd_instance = gd()
    datos = gd_instance.get_dataset()
    print (datos)
    return {"data": datos}
  
#Engegar server  
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)