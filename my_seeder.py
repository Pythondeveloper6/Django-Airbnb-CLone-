
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()


#######

from django_seed import Seed
from settings.models import FAQ


seeder = Seed.seeder()
seeder.add_entity(FAQ, 5)
inserted_pks = seeder.execute()



'''
    - external file
    - django management commands 

'''