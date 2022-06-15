# IPO Bot

This is selenium based bot made in Python to automate the IPO application process

## Getting up and running ( Installation )

1. **Check out the repository from Github**

   ```sh
   git clone git@github.com:bistasulove/ipo-bot.git
   cd ipo-bot
   ```

2. **Install Python (if not already)**

   _Note:_ This project is running **Python 3.9.10**. 

3. **Install Dependencies**

   Use pip to install all the dependencies listed in requirements.txt file

   ```sh
   pip install -r requirements.txt
   ```

4. **Service Configuration**

    You are supposed to create a `.env` file if you want to harness the feature of the bot:

    - Create a `.env` file inside the project root directory (ipo-bot)
    - Following environment variables are being used currently:
      - `RECURRING_CUSTOMER` - if value is set to True `(RECURRING_CUSTOMER='True')`, it checks the saved config from env file. Otherwise, it will ask the user input for which share to apply.
      - `APPLY_ORDINARY_SHARES` - if set to True `(APPLY_ORDINARY_SHARES='True')`, it will apply only Ordinary Shares and not Debentures
      - `APPLY_ALL` - if set to True `(APPLY_ALL='True')`, it will apply all of the shares
      - `APPLY_FIRST` - if set to True `(APPLY_FIRST='True')`, it will apply only the first share in the Open issues page

5. **Demat configuration**

    You are supposed to add the details of yours and others demat accounts in `user_details.csv` file.
    
    **Sample user_details.csv file**
    
   | alias  | dp_id | username | password    | crn     | txn_pin | apply_unit |
   |--------|-------|----------|-------------|---------|---------|------------|
   | Sulove | 10900 | 1234567  | password123 | 1233y84 | 1111    | 10         |
   | Bista  | 10900 | 1235664  | pass123     | 12314   | 2222    | 20         |

6. **Running program**

    ```sh
     python main.py
     ```
