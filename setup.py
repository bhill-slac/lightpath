import versioneer
from setuptools import (setup, find_packages)


setup(name     = 'lightpath',
      version  = versioneer.get_version(),
      cmdclass = versioneer.get_cmdclass(),
      license  = 'BSD',
      author   = 'SLAC National Accelerator Laboratory',

      packages    = find_packages(),

    )
