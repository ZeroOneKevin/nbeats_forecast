
from setuptools import setup, Extension

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()
    
setup(
  name = 'nbeats_forecast',        
  packages = ['nbeats_forecast'],   
  version = '1.3.1',     
  license='MIT',
  description="This library uses nbeats-pytorch as base and simplifies the task of forecasting using N-BEATS by providing a interface similar to scikit-learn and keras."
  long_description=long_description,
  long_description_content_type='text/markdown' , 
  author = 'Amitesh Sharma',                   
  author_email = 'amitesh863@gmail.com',     
  url = 'https://github.com/amitesh863/nbeats_forecast',   
  download_url = 'https://github.com/amitesh863/nbeats_forecast/archive/v_131.tar.gz',    
  keywords = ['nbeats', 'timeseries', 'forecast', 'nueral beats' , 'univariate timeseries forecast ', 'timeseries forecast', 'univariate timeseries forecast'],   
  install_requires=[
          'nbeats-pytorch',
      ],
  classifiers=[
    'Development Status :: 4 - Beta',          
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
  ],
)
