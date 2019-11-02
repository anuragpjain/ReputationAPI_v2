"""This class handle all business logics for reputation api"""
from configuration import constant
from connection_loader import connection_cls
from logger import RepLogger


class response(dict):
    """This   initialise the all parameter from the request body"""

    def __init__(self, machine_id=None, product_id=None, file_md5=None, url_md5=None, digisign_md5=None):
        self.machine_id = machine_id
        self.product_id = product_id
        self.file_md5 = file_md5
        self.url_md5 = url_md5
        self.digisign_md5 = digisign_md5
        self.logged = RepLogger()
        self.obj_con = connection_cls(**constant.postgres_cred)

    """Validate the response for mendotory paramter"""
    def validate_reposnse(self):
        try:

            if self.machine_id is None or  self.product_id is None or self.file_md5 is None:
                self.logged.error("'Error':'Machine Id or product Id or File md5 hash is not Present.Plese check the request'")
                return {'Error': 'Machine Id or product Id or File md5 hash is not Present.Plese check the request'}


        except Exception as e:
            print(str(e))

    """Check authenticity with machine ID  """
    def authenticate_reponse(self):
        if self.machine_id is not None:
            machine_tbl_query = constant.machine_tbl_query.format(self.machine_id)
            con = self.obj_con.connet_to_postgresdb()
            rep = self.obj_con.excute_sql_on_postgresdb(con, machine_tbl_query)
            if not rep:
                self.logged.error("'unauthorize request':'Invalid Machine Id'")
                return {'Error':'This Machine Id is not a subscriber.Please Buy a product.'}
            return True

    """Get Reputation score from database"""
    def get_reputation_score(self):
        list_reputation = list()
        if self.file_md5 is not None:
            file_rep_score_query = constant.file_hash_query.format(
                self.file_md5)
            con = self.obj_con.connet_to_postgresdb()
            rep = self.obj_con.excute_sql_on_postgresdb(con, file_rep_score_query)
            list_reputation.append(rep[0])

        if self.url_md5 is not None:
            url_rep_score_query = constant.url_hash_query.format(
                self.url_md5)
            con = self.obj_con.connet_to_postgresdb()
            rep = self.obj_con.excute_sql_on_postgresdb(con, url_rep_score_query)
            list_reputation.append(rep[0])

        if self.digisign_md5 is not None:
            url_rep_score_query = constant.digi_hash_query.format(
                self.digisign_md5)
            con = self.obj_con.connet_to_postgresdb()
            rep = self.obj_con.excute_sql_on_postgresdb(con, url_rep_score_query)
            list_reputation.append(rep[0])

        return list_reputation

    """Calculate Reputation score """
    def calculate_reputation_score(self, list_of_score):
        reputation_score = self.average(list_of_score)
        print(reputation_score)
        return reputation_score

    """Calculate Avarage from list """
    def average(self, lst):
        return sum(lst) / len(lst)

    """Prepare Return reponse"""
    def preapare_response(self, reputation_score):
        details = {'machine_id': self.machine_id,
                   'product_id': self.product_id,
                   'reputation_score': reputation_score
                   }
        return details
