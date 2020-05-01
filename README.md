dep_airport_delay_plot.png – Graph shows randomly selected ten rows from the data frame., Departure delay vs Scheduled Departure Airport

flights_fet_sel.csv -This file contains flight arrival and departure data for the airports obtained from https://www.transtats.bts.gov/OT_Delay/OT_DelayCause1.asp. Many data that are not relevant for predicting flight delay is removed. 

ACTL_ARR_ARPT_CD – Actual Arrival Airport. This is the airport actually the flight landed.

ACTL_DPRT_ARPT_CD - Actual Departure Airport. This is the airport actually the flight departed.

DOM_INTL_TYP_CD – Tells if the flight is Domestic or International Flight

FLT_ORIG_DT – Date of the flight from Departure Airport

SCH_ARR_ARPT_CD – Originally Scheduled Arrival Airport 

SCH_DPRT_ARPT_CD – Originally Scheduled Departure Airport

DPRT_TIME_DELAY – Time Delay in Departure Airport. This is calculated subtracting Scheduled Departure Time from Actual Departure Time in Departure Airport.

ARR_TIME_DELAY - Time Delay in Departure Airport. This is calculated subtracting Scheduled Departure Time from Actual Departure Time in Arrival Airport.

FLT_LEG_ADD_RSN_CD – Reason the flight was added, if everything goes well then, you’ll see only scheduled (SCH) value in this column. But in reality, various reasons like weather, equipment failure, and other operational issues can cause a flight to be added. Following are the unique values for this column.

* ADO - Flight added due to operational issues like weather, cancellation, etc.
* ADT - Flight added at the end of the flight before the flight departs from the airport.	
* CDD – Flight added due to diversion, instead of going to originally planned destination airport, flight will land in a new airport. 	
* CDF – Flight changed Destination after the departure from the airport	
* CHO – Flight changed in the Origin airport	
* DIV – Flight added due to diversion, generally in the mid-air	
* FLG - Flight added due to diversion before the departure	
* OVF – Flight added due to cancellation of portion of the flight	
* RTB – Flight added due to gate return to departure airport from runway	
* RTF – Flight added due to gate return to departure airport after the take-of	
* SCH – Scheduled flight, this is the flight passengers book when they want to travel.	
* STB – Flight added due to operation issues.	
* UNK – Flight added due to unknown issues.	

flt_count_plt.png – Number of flight in an airport, randomly selected 10 rows from the dataset.


ridge_flt_data.py –Regression model using Ridge Regression. After dummy encoding I tried with Linear Regression but the model was overfitting the test data. I tried varying various parameters but couldn’t fix the overfitting in the model. After dummy encoding many features are with 0s and 1s in the data, this caused multicollinearity in the regression model. For e.g. there are 359 unique airport codes exist in the data set, when you apply dummy encoding you get 358 (n-1) new columns added to the data set. Similarly, all other categorial variables added new columns to the data set. Many of these features are highly correlated with each other, not adding much value to generalize the model and overfitting the model. I tried Ridge Regression and that fixed the overfitting in the model. The right approach is to remove the unnecessary features from the data set and train the model. 

ridge_reg_plot.png – Plot of the Ridge Regression model

plot_flt_data.py -  Code that plots many graphs from the data set. Since the data set is large, it randomly selects 10 samples from the data set to plot the graphs.

mean_org_airport_delay_plt.png – Graph shows mean delay at the departure airport. 

