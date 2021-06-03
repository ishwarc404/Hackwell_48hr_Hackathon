import re

units = ['Kg','g','mg','N','m3','Nm3','mm','hr','Log hr','minutes','pH','bar','RPM','%','°C','° C','Nm3/Kg','Nm3/hr','Nm3/ hr','PCV']

#^N to ignore examples like CONFIGURATIONS
units_regex = re.compile('Kg|^N|m3|mm$|Nm3|\/[ ]*hr|Log hr|hr$|mg$|g$|minutes|pH|bar|RPM|%|°C|° C|PCV')

units_map  = { 'PCV' : '%' }

keyword_map = { 'date': 'dd/mm/yy',
                'signature':'short_text',
                'age':'hrs',
                'temperature':'°C',
                'time':'hrs',
                'quantity':'Kgs',
                'code':'short_text',
                'no.': 'short_text',
                'pressure':'bar',
                'details':'long_text'
                }