import datetime
import os
from plaid import Client


class PlaidClient:
    """
    Wrapper class around the Plaid API client.
    """

    def __init__(self):
        """
        Initializes an instance.
        NOTE: We don't use the Lazy pattern here because the Plaid Client caches access tokens between method calls.
        """
        self._client = Client(
            client_id=os.environ["PLAID_CLIENT_ID"],
            secret=os.environ["PLAID_SECRET"],
            public_key=os.environ["PLAID_CLIENT_ID"],
            environment=os.environ["PLAID_ENV"],
        )

    def __format_date(self, date):
        return f"{date:%Y-%m-%d}"

    def get_access_token(self, public_token):
        """
        Exchanges a public token for an access token.
        Args:
            public_token: Token created by plaid link
        Returns:
            access_token
            item_id
        """
        response = self._client.Item.public_token.exchange(public_token)
        return response["access_token"], response["item_id"]

    def delete_item(self, access_token):
        """
        Exchanges a public token for an access token.
        Args:
            access_token: Token created by plaid link
        Returns:
            removed
        """
        response = self._client.Item.remove(access_token)
        return response["removed"]

    def get_transactions(
        self,
        access_token,
        start: datetime.datetime = datetime.datetime.utcnow()
        - datetime.timedelta(days=30),
        end: datetime.datetime = datetime.datetime.utcnow(),
    ):
        """
        Retrieves transactions from the institution specified by the stored access token.
        Args:
            access_token: Plaid token for accessing users account
            start: Start date for the transaction history set. Default one month before today.
            end: End date for the transaction history set. Default today.
        Returns:
            transactions
        """
        start_date = self.__format_date(start)
        end_date = self.__format_date(end)
        response = self._client.Transactions.get(
            access_token, start_date=start_date, end_date=end_date
        )
        return response["transactions"]
