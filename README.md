# Air-quality-Management-System

This Project is just a small chunk in Air Quality Management System
Since I was low on budget I could only get budget-friendly sensors - MQ135 gas sensor(needs calibration), Sharp GP2Y dust sensor and DHT22 Temperature and humidity sensor
Assembling these sensors with a Arduino Wemos board.
The arduino code is File# AQMS(Arduino) Final Code (Enter you WiFi details and a thingsboard api)
Then we ca begin with data collection.
I have used Thingsboard to store my data into dashboards.
Since I was not able to collect data for a longer period I had to import data via APIs and other means.
If you can collect data over a longer period of time then you can proceed onto the next phase i.e., Predictive Analytics.

The python file predict.py will get you started on ML section of this project.
The code is pretty basic, it is referenced from other similar ML models.
Well the fun part is that, we can predict temperature for a specfic day/s of your choice.
I used .csv files to store the data. And you replace the keywords if necessary.
*Most important part is that you must use the same keywords both in the .py code and .csv file otherwise we will get errors because the code won't have any means to retrieve the data.
Now, in order to show you output i.e., Predicted value I needed a basic but decent looking Webpage.
For that I created a basic webpage and incorporated the predictions and dashboards into it.

This is the link - https://conceptive.co.in/aqms/index.html (Open in chrome and don't forget to enable unsecure contents from chrome browser setting.)
By the time you see the html, I might have stopped collecting data, but still you can run the prediction in the forecast page which workd just fine.
There may sometimes large differences or small differences i the predictions outputs but again, 
I couldn't train the model well meaning I had less data and also less expertise considerably.

Have Fun!
