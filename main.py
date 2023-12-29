
from selenium import webdriver
import time
#Allows you to target specific elements within the html of a webpage(seen within the find_elements function)
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()
#this allows actions to be performed by the mouse on webpages
action = ActionChains(driver)

#Gore Mountain
driver.get("https://goremountain.com")

#gets the information about gore mountain
driver.find_element(By.ID,"hero").click()

#Gore Date
gore_date = driver.find_element(By.CLASS_NAME,"last-update").text

#Gore Weather Data
gore_temp = driver.find_element(By.CLASS_NAME,"report-box.weather-data").find_element(By.CLASS_NAME,"primary").text
gore_forecast= driver.find_element(By.CLASS_NAME,"report-box.weather-data").find_element(By.CLASS_NAME,"secondary").text

#Wind Data
gore_extra_data = driver.find_element(By.CLASS_NAME,"report-box.weather-extra").find_element(By.CLASS_NAME,"label").text
gore_wind_data = driver.find_element(By.CLASS_NAME,"report-box.weather-extra").find_element(By.CLASS_NAME,"value").text

#Snowfall Data
gore_snowfall_measurement_period = driver.find_element(By.CLASS_NAME,"report-box.snow-extra").find_element(By.CLASS_NAME,"label").text
gore_snowfall_last_7days = driver.find_element(By.CLASS_NAME,"report-box.snow-extra").find_element(By.CLASS_NAME,"value").text
gore_base_depth_label = driver.find_element(By.CLASS_NAME,"report-box.snow-extra").find_elements(By.CLASS_NAME,"extra-detail")[1].find_element(By.CLASS_NAME,"label").text
gore_base_depth = driver.find_element(By.CLASS_NAME,"report-box.snow-extra").find_elements(By.CLASS_NAME,"extra-detail")[1].find_element(By.CLASS_NAME,"value").text

#Surface conditions
gore_surface_conditions_primary = driver.find_element(By.CLASS_NAME,"report-box.surface-extra").find_elements(By.CLASS_NAME,"extra-detail")[0].find_element(By.CLASS_NAME,"value").text
gore_surface_conditions_secondary = driver.find_element(By.CLASS_NAME,"report-box.surface-extra").find_elements(By.CLASS_NAME,"extra-detail")[1].find_element(By.CLASS_NAME,"value").text

#Lift Data
gore_lifts_open = driver.find_element(By.CLASS_NAME,"report-box.lifts").find_element(By.CLASS_NAME,"primary").text
gore_lifts_total = driver.find_element(By.CLASS_NAME,"report-box.lifts").find_element(By.CLASS_NAME,"secondary").text
gore_trails_open_primary = driver.find_element(By.CLASS_NAME,"report-box.trails").find_element(By.CLASS_NAME,"main-detail").find_element(By.CLASS_NAME,"primary").text
gore_trails_open_secondary = driver.find_element(By.CLASS_NAME,"report-box.trails").find_element(By.CLASS_NAME,"main-detail").find_element(By.CLASS_NAME,"secondary").text
gore_percent_terrain_open = driver.find_element(By.CLASS_NAME,"report-box.terrain-extra").find_element(By.CLASS_NAME,"value").text

#Ski Message
header = driver.find_element(By.CLASS_NAME,"col.col-right.intro-content-text").find_elements(By.CSS_SELECTOR,'p')[0].text
message1 = driver.find_element(By.CLASS_NAME,"col.col-right.intro-content-text").find_elements(By.CSS_SELECTOR,'p')[1].text
message2 = driver.find_element(By.CLASS_NAME,"col.col-right.intro-content-text").find_elements(By.CSS_SELECTOR,'p')[2].text




#Whiteface website


#this opens new tab and loads whiteface's ski report
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])
driver.get("https://whiteface.com/mountain/conditions/")

#this allows extra information button regarding ski report to be visible to allow action on it
driver.execute_script("window.scrollTo(0,document.body.scrollHeight/3.5)")


#this allows me to see extra ski report info and ensures that the button element is properly loaded onto the page
try:
    more_info_button_element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "view-more")))
    action.move_to_element(more_info_button_element)
    action.click()
    action.perform()
    action.reset_actions()



except TimeoutException:
    print("the \"view more\" button for ski report did not load within 30 seconds, please ensure your internet connection is stable to load the page")

#Note try and execepts statements were needed to ensure that if view more button was not pressed, they will get "error" as their value
    #whiteface weather data
try:
    white_update_time = driver.find_element(By.CLASS_NAME, "conditions-wrapper.conditions-winter").find_element(By.CLASS_NAME, "cr.conditions-report.snow-report").find_element(By.CLASS_NAME,   "last-update").text
except TimeoutException:
    white_update_time  = "error"

try:
    white_forecast = driver.find_element(By.CLASS_NAME, "conditions-wrapper.conditions-winter").find_element(By.CLASS_NAME, "report-box.weather-data").find_element(By.CLASS_NAME, "secondary").text

except TimeoutException:
    white_forecast = "error"

try:
    white_base_temp = driver.find_element(By.CLASS_NAME, "cr.conditions-report.snow-report.view-more-open").find_elements(By.CLASS_NAME,"extra-detail")[0].find_element(By.CLASS_NAME, "value").text

except TimeoutException:
    white_base_temp = "error"

try:
    white_mid_temp = driver.find_element(By.CLASS_NAME,"cr.conditions-report.snow-report.view-more-open").find_elements(By.CLASS_NAME,"extra-detail")[1].find_element(By.CLASS_NAME,"value").text
except TimeoutException:
    white_mid_temp = "error"

try:
    white_summit_temp = driver.find_element(By.CLASS_NAME,"cr.conditions-report.snow-report.view-more-open").find_elements(By.CLASS_NAME,"extra-detail")[2].find_element(By.CLASS_NAME,"value").text
except TimeoutException:
    white_summit_temp = "error"

try:
    white_wind_data = driver.find_element(By.CLASS_NAME,"cr.conditions-report.snow-report.view-more-open").find_elements(By.CLASS_NAME,"extra-detail")[3].find_element(By.CLASS_NAME,"value").text
except TimeoutException:
    white_wind_data = "error"

try:
    white_snowfall_past24hrs = driver.find_element(By.CLASS_NAME,"report-box.snow-extra").find_elements(By.CLASS_NAME,"extra-detail")[0].find_element(By.CLASS_NAME,"value").text
except TimeoutException:
    white_snowfall_past24hrs = "error"

try:
    white_snowfall_past7days = driver.find_element(By.CLASS_NAME, "report-box.snow-extra").find_elements(By.CLASS_NAME, "extra-detail")[1].find_element(By.CLASS_NAME, "value").text
except TimeoutException:
    white_snowfall_past7days = "error"

try:
    white_snowfall_basedepth = driver.find_element(By.CLASS_NAME, "report-box.snow-extra").find_elements(By.CLASS_NAME, "extra-detail")[2].find_element(By.CLASS_NAME, "value").text
except TimeoutException:
    white_snowfall_basedepth = "error"


try:
    white_snowfall_total = driver.find_element(By.CLASS_NAME, "report-box.snow-extra").find_elements(By.CLASS_NAME, "extra-detail")[3].find_element(By.CLASS_NAME, "value").text
except TimeoutException:
    white_snowfall_total = "error"

try:
    white_surfaceconditions_primary = driver.find_element(By.CLASS_NAME, "report-box.surface-extra").find_elements(By.CLASS_NAME, "extra-detail")[0].find_element(By.CLASS_NAME, "value").text
except TimeoutException:
    white_surfaceconditions_primary = "error"

try:
    white_surfaceconditions_secondary = driver.find_element(By.CLASS_NAME, "report-box.surface-extra").find_elements(By.CLASS_NAME, "extra-detail")[1].find_element(By.CLASS_NAME, "value").text
except TimeoutException:
    white_surfaceconditions_secondary = "error"


#General Mountain information
try:
    white_lifts_open_primary = driver.find_element(By.CLASS_NAME, "conditions-wrapper.conditions-winter").find_element(By.CLASS_NAME, "report-box.lifts").find_element(By.CLASS_NAME, "main-detail").find_element(By.CLASS_NAME, "primary").text
except TimeoutException:
    white_lifts_open_primary = "error"

try:
    white_lifts_open_secondary = driver.find_element(By.CLASS_NAME,"conditions-wrapper.conditions-winter").find_element(By.CLASS_NAME, "report-box.lifts").find_element(By.CLASS_NAME, "secondary").text
except TimeoutException:
    white_lifts_open_secondary = "error"

try:
    white_trails_open_primary = driver.find_element(By.CLASS_NAME, "conditions-wrapper.conditions-winter").find_element(By.CLASS_NAME, "report-box.trails").find_element(By.CLASS_NAME, "primary").text
except TimeoutException:
    white_trails_open_primary = "error"

try:
    white_trails_open_secondary = driver.find_element(By.CLASS_NAME, "conditions-wrapper.conditions-winter").find_element(By.CLASS_NAME, "report-box.trails").find_element(By.CLASS_NAME, "secondary").text
except TimeoutException:
    white_trails_open_secondary = "error"

try:
    white_terrain_percent_open = driver.find_element(By.CLASS_NAME, "report-box.terrain-extra").find_element(By.CLASS_NAME, "value").text
except TimeoutException:
    white_terrain_percent_open = "error"

try:
    white_gandola_status = driver.find_element(By.CLASS_NAME, "report-box.x-gondola-rides").find_element(By.CLASS_NAME, "value").text
except TimeoutException:
    white_gandola_status = "error"

#Ski message - note could use for loop to loop through each <p> tag, however only first few paragraphs are important....
try:
    white_message1_reporter = driver.find_element(By.CLASS_NAME, "col.col-right.intro-content-text").find_elements(By.CSS_SELECTOR,  'p')[0].text
except TimeoutException:
    white_message1_reporter = "error"

try:
    white_message2 = driver.find_element(By.CLASS_NAME, "col.col-right.intro-content-text").find_elements(By.CSS_SELECTOR,  'p')[1].text
except TimeoutException:
    white_message2 = "error"

try:
    white_message3 = driver.find_element(By.CLASS_NAME, "col.col-right.intro-content-text").find_elements(By.CSS_SELECTOR, 'p')[2].text
except TimeoutException:
    white_message3 = "error"

try:
    white_message4 = driver.find_element(By.CLASS_NAME, "col.col-right.intro-content-text").find_elements(By.CSS_SELECTOR, 'p')[3].text
except TimeoutException:
    white_message4 = "error"


#Lab Mountain

#opens up lab's website in a new tab
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[2])
driver.get("https://www.skicny.com/labrador/ski-report/")

lab_last_updated = driver.find_element(By.CLASS_NAME,"col-md-6.mb-top-mg").find_element(By.CLASS_NAME,"subtext.time").find_elements(By.CSS_SELECTOR,'b')[1].text



#information about lab mountain
lab_trails_open = driver.find_element(By.CLASS_NAME,"tb").find_elements(By.CSS_SELECTOR,'td')[1].text
lab_lifts_open_night_and_day = driver.find_element(By.CLASS_NAME,"tb").find_elements(By.CSS_SELECTOR,'td')[3].text
lab_lift_hrs = driver.find_element(By.CLASS_NAME,"tb").find_elements(By.CSS_SELECTOR,'td')[5].text
lab_surface_conditions = driver.find_element(By.CLASS_NAME,"tb").find_elements(By.CSS_SELECTOR,'td')[7].text
lab_snowfall_past24hrs = driver.find_element(By.CLASS_NAME,"tb").find_elements(By.CSS_SELECTOR,'td')[9].text
lab_snowmaking_status = driver.find_element(By.CLASS_NAME,"tb").find_elements(By.CSS_SELECTOR,'td')[11].text
lab_snow_base_depth = driver.find_element(By.CLASS_NAME,"tb").find_elements(By.CSS_SELECTOR,'td')[13].text



#display of script
print("--------------------------------------------------------------------------")
print("Gore Mountain\n")
print(gore_date + "\n")
print("Weather: \n\t" + "Temperature:  " + gore_temp + "\n\t" + "Forecast:" + "\t" + gore_forecast + "\n\t" + gore_extra_data + "\t" + gore_wind_data )
print("\t" + "Snowfall:" + "\n\t   " + gore_snowfall_measurement_period + "\t " + gore_snowfall_last_7days + "\n" + "\t   " + gore_base_depth_label + "\t" + gore_base_depth)
print("\t" + "Surface Conditions:\t" + gore_surface_conditions_primary + "/" + gore_surface_conditions_secondary + "\n")
print("Mountain: \n" + "\t" + "Lifts Open:\t" + gore_lifts_open + " " + gore_lifts_total)
print("\t" + "Trails Open: " + gore_trails_open_primary + " " + gore_trails_open_secondary)
print("\t" + "Terrain Open: " + gore_percent_terrain_open + "\n")
print("Ski Message: " + "\n\t" + header)
print(message1 + " " + message2)

print("--------------------------------------------------------------------------")
print("Whiteface Mountain\n")
print(white_update_time + "\n")
print("Weather: \n\t" + "Temperature:\n\t\t" +"Base Temp:  " + white_base_temp + "\n\t\tMid Temp:  " + white_mid_temp + "\n\t\tSummit Temp:  " + white_summit_temp + "\n\tForecast:  " + white_forecast +"\n\tWind:  " + white_wind_data + " mph")
print("\tSnowfall:\n\t\t" + "Past 24hrs:  " + white_snowfall_past24hrs + "\n\t\tLast 7 Days:  " + white_snowfall_past7days + "\n\t\tBase Depth:  " + white_snowfall_basedepth + "\n\t\tSeason Total:  " + white_snowfall_total)
print("\tSurface Conditions:  " + white_surfaceconditions_primary + " / " + white_surfaceconditions_secondary + "\n")
print("Mountain:\n  " + "\tLifts Open:  " + white_lifts_open_primary + " " + white_lifts_open_secondary + "\n\tTrails Open:  " + white_trails_open_primary + " " + white_trails_open_secondary + "\n\tTerrain Open:  " + white_terrain_percent_open)
print("\tGondola Ride Status:  " + white_gandola_status + "\n")
print("Ski Message:\t" + white_message1_reporter + "\n")
print(white_message2)
print(white_message3)
print(white_message4)
print("")
print("--------------------------------------------------------------------------")
print("Labrador Mountain\n")
print("Last Updated:  " + lab_last_updated + "\n")
print("Weather:\n\t" + "Snowfall:\n\t" +"Past 24hrs:  " + lab_snowfall_past24hrs + "\n\tSnow Making Status:  " + lab_snowmaking_status + "\n\tSnow Base Depth:  " + lab_snow_base_depth)
print("\tSurface Conditons:  " + lab_surface_conditions)
print("Mountain:\n\t" + "Lifts Open(Day/Night):  " + lab_lifts_open_night_and_day + "\n\tTrails Open:  " + lab_trails_open + " of 23")
print("--------------------------------------------------------------------------")
driver.quit()





