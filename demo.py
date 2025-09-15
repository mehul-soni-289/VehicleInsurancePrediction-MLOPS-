# below code is to check the logging config
# from src.logger import logging

# logging.debug("This is a debug message.")
# logging.info("This is an info message.")
# logging.warning("This is a warning message.")
# logging.error("This is an error message.")
# logging.critical("This is a critical message.")

# --------------------------------------------------------------------------------

# # below code is to check the exception config
# from src.logger import logging
# from src.exception import MyException
# import sys

# try:
#     a = 1+'Z'
# except Exception as e:
#     logging.info(e)
#     raise MyException(e, sys) from e

# --------------------------------------------------------------------------------

# from src.pipline.training_pipeline import TrainPipeline

# pipline = TrainPipeline()
# pipline.run_pipeline()


from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse, RedirectResponse
from uvicorn import run as app_run

from typing import Optional

# Importing constants and pipeline modules from the project
from src.constants import APP_HOST, APP_PORT
from src.pipline.prediction_pipeline import VehicleData, VehicleDataClassifier
from src.pipline.training_pipeline import TrainPipeline



vehicle_data = VehicleData(
                                Gender= 1,
                                Age = 18,
                                Driving_License = 1,
                                Region_Code = 25,
                                Previously_Insured = 0,
                                Annual_Premium =33000,
                                Policy_Sales_Channel = 152,
                                Vintage = 21,
                                Vehicle_Age_lt_1_Year = 1,
                                Vehicle_Age_gt_2_Years = 0,
                                Vehicle_Damage_Yes = 0
                                )

vehicle_df = vehicle_data.get_vehicle_input_data_frame()

# Initialize the prediction pipeline
model_predictor = VehicleDataClassifier()


# Make a prediction and retrieve the result
value = model_predictor.predict(dataframe=vehicle_df)[0]

# Interpret the prediction result as 'Response-Yes' or 'Response-No'
status = "Response-Yes" if value == 1 else "Response-No"


print(status)
