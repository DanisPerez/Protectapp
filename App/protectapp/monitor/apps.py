<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 7c9c8fce799681b798ac83cabdaf1af962be551a
<<<<<<< HEAD
>>>>>>> 140297cf9450a6de7652b1265e43fff63f4f0b04
=======
=======
>>>>>>> 8e18bd6d3b44f892c4e048fb7e4e553c2d8fe619
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29

from django.apps import AppConfig

class MonitorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'monitor'

    def ready(self):
        import monitor.signals  # Importar señales
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
=======
=======
<<<<<<< HEAD
=======
=======
>>>>>>> 8e18bd6d3b44f892c4e048fb7e4e553c2d8fe619
=======
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
from django.apps import AppConfig


class MonitorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'monitor'
<<<<<<< HEAD


class TuAppConfig(AppConfig):
    name = 'monitor'
    def ready(self):
        import monitor.signals  # Importar señales
=======
>>>>>>> afc917d1d14c3730d6946130d053056968a08dc6
>>>>>>> 6ed65ad7429d47b5a2bed51bfa4f1a8fd6c2a470
<<<<<<< HEAD
>>>>>>> 7c9c8fce799681b798ac83cabdaf1af962be551a
>>>>>>> 140297cf9450a6de7652b1265e43fff63f4f0b04
=======
<<<<<<< HEAD
>>>>>>> 7c9c8fce799681b798ac83cabdaf1af962be551a
=======
>>>>>>> 8e18bd6d3b44f892c4e048fb7e4e553c2d8fe619
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
