from driver import IpoBot
import logging
from user_details import UserDetails
from dotenv import load_dotenv
import os

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    user_details = UserDetails().user_details
    for user in user_details:
        try:
            mero_share = IpoBot()
        except Exception as e:
            logger.error("Error opening meroshare page. Please try again or after a while")
            break
        try:
            mero_share.login(user)
        except Exception as e:
            logger.error(f"Error while trying to login to {user['alias']}", e)
            continue
        mero_share.navigate("asba")
        mero_share.parse_open_issues()
        if os.environ.get("RECURRING_CUSTOMER") == "True":
            logger.info("Checking saved config for recurring customer")
            print(f"Apply all env value: {os.environ.get('APPLY_ALL', default=False)}")
            if os.environ.get("APPLY_ALL") == "True":
                logger.info("Found config to apply all share...")
                indices = mero_share.get_issue_indexes_for(share_type="all")
                mero_share.apply_ipo(user, indices)
            elif os.environ.get("APPLY_FIRST") == "True":
                logger.info("Found config to apply 1st share...")
                mero_share.apply_ipo(user, [1])
            elif os.environ.get("APPLY_ORDINARY_SHARES") == "True":
                logger.info("Found config to apply all ordinary shares...")
                indices = mero_share.get_issue_indexes_for(share_type="Ordinary Shares")
                mero_share.apply_ipo(user, indices)
        else:
            input_indices = input("Enter the index of issue you want to apply. To apply multiple issue, enter the "
                                  "index in comma separated fashion. Eg: 1,2,3 \n")
            indices = input_indices.split(",")
            try:
                indices_new = [int(index) for index in indices]
            except Exception as e:
                logger.error(f"Invalid input", e)
                mero_share.quit()
            mero_share.apply_ipo(user, indices_new)
