from driver import IpoBot
import logging
from user_details import UserDetails

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    user_details = UserDetails().user_details
    for user in user_details:
        meroshare = IpoBot()
        meroshare.login(user)
        meroshare.navigate("asba")
        meroshare.parse_open_issues()