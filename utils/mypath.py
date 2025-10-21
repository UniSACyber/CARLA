
import os


class MyPath(object):
    @staticmethod
    def db_root_dir(database=''):
        db_names = {'msl', 'smap', 'smd', 'power', 'yahoo', 'kpi', 'swat', 'wadi', 'gecco', 'swan', 'ucr', 's3id'}
        assert(database in db_names)

        if database == 'msl' or database == 'smap':
            return os.path.join(os.getcwd(), 'datasets/MSL_SMAP')
        elif database == 'ucr':
            return os.path.join(os.getcwd(), 'datasets/UCR')
        elif database == 'yahoo':
            return os.path.join(os.getcwd(), 'datasets/Yahoo')
        elif database == 'smd':
            return os.path.join(os.getcwd(), 'datasets/SMD')
        elif database == 'swat':
            return os.path.join(os.getcwd(), 'datasets/SWAT')
        elif database == 'wadi':
            return os.path.join(os.getcwd(), 'datasets/WADI')
        elif database == 'kpi':
            return os.path.join(os.getcwd(), 'datasets/KPI')
        elif database == 'swan':
            return os.path.join(os.getcwd(), 'datasets/Swan')
        elif database == 'gecco':
            return os.path.join(os.getcwd(), 'datasets/GECCO')
        elif database == 's3id':
            return os.path.join(os.getcwd(), 'datasets/S3ID')
        
        else:
            raise NotImplementedError
