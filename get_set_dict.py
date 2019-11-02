"""
THis is class reponsible for gettting dict as paramter and setting all value as per the key
But in this context It seems useless to use getter setter
"""
class parse_server_reponse(dict):
    def __init__(self, machine_id=None, product_id=None, file_md5=None, url_md5=None, digisign_md5=None):
        self['machineid'] = machine_id
        self['productid'] = product_id

        self['filemd5'] = file_md5
        self['urlmd5'] = url_md5
        self['digisignmd5'] = digisign_md5

    @property
    def get_machine_id(self):
        return self['machineid']

    @get_machine_id.setter
    def set_machine_id(self, machineid):
        self['machineid'] = machineid

    @property
    def get_product_id(self):
        return self['productid']

    @get_product_id.setter
    def set_product_id(self, productid):
        self['productid'] = productid

    @property
    def get_file_md5(self):
        return self['filemd5']

    @get_file_md5.setter
    def set_machine_id(self, filemd5):
        self['filemd5'] = filemd5

    @property
    def get_url_md5(self):
        return self['urlmd5']

    @get_url_md5.setter
    def set_machine_id(self, urlmd5):
        self['urlmd5'] = urlmd5

    @property
    def get_digi_md5(self):
        return self['digisignmd5']

    @get_digi_md5.setter
    def set_machine_id(self, digisignmd5):
        self['digisignmd5'] = digisignmd5



if __name__ == '__main__':
    print(__doc__)



