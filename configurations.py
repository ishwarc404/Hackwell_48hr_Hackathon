import re
units = ['Kg','N','m3','mm','hr','minutes','pH','bar','RPM','%','°C','Nm3/Kg','Nm3/hr','PCV']

#^N to ignore examples like CONFIGURATIONS
units_regex = re.compile('Kg|^N|m3|mm|Nm3|\/hr|hr$|minutes|pH|bar|RPM|%|°C|PCV')

units_map  = { 'PCV' : '%' }