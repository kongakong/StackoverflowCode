# https://stackoverflow.com/questions/60256803/australian-bureau-of-statistics-sdmx-timeout-issue

from request import Request
Dataset_Id = 'ABS_ERP_ASGS2016'
ABS = Request(Agency_Code)
data_response = ABS.data(resource_id='ABS_ERP_ASGS2016', params={'startTime': '2018','endTime': '2018'})
def timeout(self, value):
    self.client.config['timeout'] = 10000
ERP2018=data_response.write().unstack().reset_index()

ERP2018 = ERP2018[(ERP2018.REGIONTYPE =='AUS') | (ERP2018.REGIONTYPE =='STE')]

ERP2018.to_csv('c:\\Temp\\erp2018.csv')
