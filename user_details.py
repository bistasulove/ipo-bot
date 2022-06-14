import csv


class UserDetails:
    def __init__(self):
        self.filename = "user_details.csv"
        self.headers = ["alias", "dp_id", "username", "password", "crn", "txn_pin", "apply_unit"]
        self.user_details = self.__parse()

    def __parse(self):
        with open(self.filename, mode='r') as infile:
            # only read the data, ignoring the headers in CSV file
            next(infile)
            reader = csv.reader(infile)
            user_details = []
            for row in reader:
                user_detail = dict(zip(self.headers, row))
                user_details.append(user_detail)
            return user_details


