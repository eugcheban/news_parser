**Parser News**

This is a program for collecting news articles based on Google search queries, processing them, and publishing them on Telegram. Its features include:

✔️ Ready: 
+ Searching for news based on a query
+ Saving news articles (links, page content)
+ Parsing the content of the news using JQuery syntax
+ Saving parsing templates for each domain, with variations
+ Editing the news text

⏲️ On Development:
- Publishing the news to Telegram
- 

## How to start
1. Clone repository
2. Create environment and install all packages from requirements.txt
3. Create database and username for it, give required privilegies.
4. Create db structure by uncomment `create_db_structure(app, db)` function in app.py which located at the end of code
    
## How to work
1. Type your search request in tab "Scrapper" search box, click button "Search". (at current moment of development, you can see the process of work in chrome dev tools console, press f12) Then work will be done without any issues, table will update with results, you used to transfer them into parse tab by selecting with checkbox and press button "Transfer".
   
3. On parser tab you should select a link to parse, and type code in editor to parse. "context" variable represents a jQuery object of web-page, so it's possible to apply jQuery and JS methods to it. Parse-code should return a string variable which will be show in next editor, for further possible edits.
4. Next steps on development, this is posting on Telegram.



## Sample of .env file
```
# Database configuration
DATABASE_URL_TESTING=postgresql://username:password@localhost:5432/db_name

# Flask configuration
FLASK_APP=app.py
FLASK_ENV=testing

# Secret key for session management
SECRET_KEY=my_secret_key

# API Key
API_KEY=your_api_key_here
TELEGRA_API = ""
```
