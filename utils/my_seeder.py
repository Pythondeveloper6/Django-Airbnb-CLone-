
import os
import django
from django_seed import Seed
from settings.models import FAQ



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.settings')
django.setup()




seeder = Seed.seeder()
seeder.add_entity(FAQ, 5)
inserted_pks = seeder.execute()