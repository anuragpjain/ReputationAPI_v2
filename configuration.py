
"""All global config goes here. """
class constant():
    postgres_cred = {
        "host": "35.223.139.105",
        "port": 5432,
        "dbname": "repdb",
        "username": "postgres",
        "password": "abc@123"
    }

    file_hash_query = "select reputation_score from file_hash where md5_hash='{}'"
    url_hash_query = "select reputation_score from url_hash where md5_hash='{}'"
    digi_hash_query = "select reputation_score from digi_hash where md5_hash='{}'"
    machine_tbl_query = "select machine_id from machineids where machine_id='{}'"
