dep_airport_delay_plot.png – Graph shows randomly selected ten rows from the data frame., Departure delay vs Scheduled Departure Airport
flights_fet_sel.csv -This file contains flight arrival and departure data for the airports obtained from https://www.transtats.bts.gov/OT_Delay/OT_DelayCause1.asp. Many data that are not relevant for predicting flight delay is removed.
ACTL_ARR_ARPT_CD – Actual Arrival Airport. This is the airport actually the flight landed.
ACTL_DPRT_ARPT_CD - Actual Departure Airport. This is the airport actually the flight departed.

DOM_INTL_TYP_CD – Tells if the flight is Domestic or International Flight
FLT_LEG_ADD_RSN_CD – Reason the flight was added.
FLT_ORIG_DT – Date of the flight from Departure Airport
SCH_ARR_ARPT_CD – Originally Scheduled Arrival Airport 
SCH_DPRT_ARPT_CD – Originally Scheduled Departure Airport
DPRT_TIME_DELAY – Time Delay in Departure Airport. This is calculated subtracting Scheduled Departure Time from Actual Departure Time in Departure Airport.
ARR_TIME_DELAY - Time Delay in Departure Airport. This is calculated subtracting Scheduled Departure Time from Actual Departure Time in Arrival Airport.
