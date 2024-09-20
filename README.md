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

## How to start
1. Clone repository
   `git clone git clone https://github.com/eugcheban/news_parser`
2. Create environment and install all packages from requirements.txt
   ```
   python -m venv news_parser
   source news_parser/bin/activate
   pip install -r requirements.txt
   ```
3. Create database and username for it, give required privilegies, these data you should type into your .env file, sample of which you can find in the end of README.md.
   ```
   sudo -i -u postgres
   psql
    
   create database test_database;
   CREATE USER username WITH PASSWORD 'password';   
   \с test_database;
   ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL PRIVILEGES ON TABLES TO username;    
   \q
   ```
5. Create db structure by uncomment `create_db_structure(app, db)` function in app.py which located at the end of code. (should be done once)
    
## How to work
1. Type your search request in tab "Scrapper" search box, click button "Search". (at current moment of development, you can see the process of work in chrome dev tools console, press f12) Then work will be done without any issues, table will update with results, you used to transfer them into parse tab by selecting with checkbox and press button "Transfer".
   ![1 step - scrap the info](https://github.com/user-attachments/assets/bf198e57-1c08-4112-a87f-b827a1bd9d0f)
   ![2 step - transfer results for parse](https://github.com/user-attachments/assets/14955103-eaa6-4e7a-9fe6-510c3464c93a)
   
2. On parser tab you should select a link to parse, and type code in editor to parse. "context" variable represents a jQuery object of web-page, so it's possible to apply jQuery and JS methods to it. Parse-code should return a string variable which will be shown in next editor, for further possible edits.
   ![3 step - parse web-page](https://github.com/user-attachments/assets/2bd1f5f3-a1ae-459b-b0f4-3151a4517dfd)
   ![4 step - parsing](https://github.com/user-attachments/assets/a519dad9-e697-4f39-b8bd-eff0c10eac18)


3. Next steps on development, this is posting on Telegram.



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
