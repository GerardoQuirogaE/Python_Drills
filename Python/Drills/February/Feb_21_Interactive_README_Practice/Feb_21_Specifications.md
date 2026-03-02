# Interactive README files!

This folder contains a simple system to make your read me files interactive. It works by having a three file system: 
* The **Update Script** ------- `Interactive_README_Practice.py`
* The **Variable Template**--- `TEMPLATE.md`
* The **Target README** ----- `Test_me_README.md`

This folder contains Python scripts for calculating energy transitions in atoms using the Rydberg formula. It allows users to compute the wavelength of emitted or absorbed light and the corresponding initial or final energy levels.

## Dependencies
The project requires the following dependencies:
* `datetime`
* `pathlib`
* `random`
* `requests`
* `yfinance`

You can run this line to install all the dependencies:

    pip install requests yfinance
##
<br>

## Interactive_README_Practice.py

This file has the function of updating the information on the target file by using a template with variables, and then replacing the variables with their actual values. These are the specifications of each of the functions or variables of the script.

| Function/Variable | Description | How its used |
|------|-------------|--|
| `ROOT` | This variable uses `Path(__file__)` and then applys to it `.parent` to figure out what path the project's folder is.| ```ROOT = Path(__file__).resolve().parent``` |
| `TEMPLATE_PATH` and `OUTPUT_PATH`| These variables are the paths to the template file, and to the variable README.md file. |`TEMPLATE_PATH = ROOT / "TEMPLATE.md"` <br><br> `OUTPUT_PATH = ROOT / "Test_me_README.md"`|
| `START_DATE` | This constant uses the function `datetime()` to format the day I started this challenge. | `START_DATE = datetime(2026, 2, 11)` |
|`today` | This variable uses the function `datetime().now` to determine today's date.|`today = datetime.now()` |
| `day_number` | This variable makes an opperation to determine how many days have past since the challenge started. It is one of the values that gets added to content.| `day_number = (today - START_DATE).days + 1` |
| `today_str` | This is a variable that gets todays date from `today` and formats it in "Month, Day, Year". This is also added to content. | `today_str = today.strftime("%m/%d/%Y")` |
| `random_number` | This variable uses the function `random` and adds a random interval from 1 - 5. | `random_number = random.randint(1,5)` |  
| `random_image` | This variable gets asigned the name of one of 5 different pictures named 'Image_' and a number from 1 - 5. This image will later be added to content. | `random_image = f"images/Image_{random_number}.jpg"` |
| `Acapulco_weather` | This variable uses a free api with no authentication requirements to request acapulco's weather information. This variable is later used as content. | `Acapulco_weather = requests.get("https://wttr.in/Acapulco?format=3").text` |
| `msft` | This variable uses yahoo finance's library to get the MSFT ticker information (to avoid using an auth key with other APIs). | `msft = yf.Ticker("MSFT")` |
| `MSFT_price` | This variable only saves the ticker's price from the `msft` ticker information. | `MSFT_price = msft.history(period="1d")["Close"][-1]` |
| `MSFT_output` | This formats the output from `MSFT_price` into a 2f string. This variable is later used as content. | `MSFT_output = f"${MSFT_price:.2f}"` |
| `content`| This is initially asigned all of the information from the `TEMPLATE_PATH`. <br><br> Later, the variable information is added by using the `.replace()` function. <br> Here we replaced: <br> - `{{DAY}}` &rarr; `day_number` <br> - `{{DATE}}` &rarr; `today_str` <br> - `{{STREAK}}` &rarr; `Active` <br> - `{{RANDOM_IMG}}` &rarr; `random_image` <br> - `{{ACAPULCO_WEATHER}}` &rarr; `Acapulco_weather` <br> - `{{MSFT_PRICE}}` &rarr; `MSFT_output` <br><br> Lastly, `content` is used to write its information on `OUTPUT_PATH` |`with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:` <br><br>`content = f.read()` <br><br><br><br> `with open(OUTPUT_PATH, "w", encoding="utf-8") as f:` <br><br> `f.write(content)` |
##
<br>

## TEMPLATE.md

This file has the function of being the template for the actual readme. It contains content with special values that are changed by applying the python script. These are the specifications of each of the functions or variables of the script.

| Function/Variable | Description | How its used |
|------|-------------|--|
| `{{DAY}}` | This is a placeholder text that will be replaced with the day in the form of a badge from shields.io. | `<img align="center" src="https://img.shields.io/badge/Day-{{DAY}}%2F365-blue" />` |
| `{{STREAK}}` | This placeholder text will be replaced with a badge from shields.io with the stats of my streak. | `<img align="center" src="https://img.shields.io/badge/Streak-{{STREAK}}-brightgreen" />` |
| `{{DATE}}` | This placeholder text will be replaced with a badge from shields.io with the date from my script. | `<img align="center" src="https://img.shields.io/badge/Last_Commit-{{DATE}}-orange" />` |
| `{{RANDOM_IMG}}` | This placeholder text will be replaced with 1 of 5 random cat images. | `<img src="{{RANDOM_IMG}}" width="150" height="150" style="display:block; margin:0 auto;" alt="Random image">` |
| `{{ACAPULCO_WEATHER}}` | This placeholder text will be replaced with info on acapulcos weather. | `<p>{{ACAPULCO_WEATHER}}</p>` |
| `{{MSFT_PRICE}}` | This placeholder text will be replaced with info on microsoft's stock price. | `<p>{{MSFT_PRICE}}</p>` |

##
<br>

## Target README

This file can actually be blank. The entirety of this file will be replaced with the template and the updated values of the variables. Make sure to run the code multiple times to be able to see [Image_5](./images/Image_5.jpg).