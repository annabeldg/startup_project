industries = ['Advertising', 'Agriculture and Farming', 'Life Sciences', 'Clothing and Apparel',
              'Commerce and Shopping', 'Community and Lifestyle', 'Consumer Electronics', 'Consumer Goods',
              'Content and Publishing', 'Design', 'Education', 'Energy', 'Environment and Sustainability', 'Events',
              'Financial Services', 'Food and Beverage', 'Gaming', 'Government and Military', 'Computer Hardware',
              'Health Care', 'HumanResources', 'Software', 'Legal', 'Logistics', 'Manufacturing', 'Data and Analytics',
              'Media and Entertainment', 'Messaging and Telecommunications', 'Music and Audio', 'Natural Resources',
              'Navigation and Mapping', 'Payments', 'Privacy and Security', 'Professional Services',
              'Real Estate and Construction', 'Sales and Marketing', 'Sports', 'Transportation', 'Travel and Tourism',
              'Video']

technologies = ['Artificial Intelligence', 'Biotechnology', 'Hardware', 'Science and Engineering', 'Software',
                'Sustainability', 'BlockChain', 'AR and VR']

new_codes = {'Other': 'OTHERS', 'China': 'CN', 'United States': 'US', 'Viet Nam': 'VN', 'Colombia': 'CO', 'Canada': 'CA',
             'Denmark': 'DK', 'Japan': 'JP', 'Sweden': 'SE', 'Belgium': 'BE', 'Netherlands': 'NL', 'Italy': 'IT',
             'Australia': 'AU', 'Israel': 'IL', 'Spain': 'ES', 'Germany': 'DE', 'India': 'IN', 'Switzerland': 'CH',
             'Argentina': 'AR', 'United Kingdom': 'GB', 'Korea, Republic of': 'KR', 'Brazil': 'BR', 'Portugal': 'PT',
             'Egypt': 'EG', 'Poland': 'PL', 'France': 'FR', 'Hong Kong': 'HK', 'Taiwan': 'TW', 'Norway': 'NO',
             'Romania': 'RO', 'Bangladesh': 'BD', 'Russian Federation': 'RU', 'South Africa': 'ZA', 'Malaysia': 'MY',
             'Ireland': 'IE', 'Mexico': 'MX', 'Nigeria': 'NG', 'United Arab Emirates': 'AE', 'Estonia': 'EE',
             'Chile': 'CL', 'Pakistan': 'PK', 'Singapore': 'SG', 'Hungary': 'HU', 'Czech Republic': 'CZ',
             'Ukraine': 'UA', 'Luxembourg': 'LU', 'Cyprus': 'CY', 'Indonesia': 'ID', 'Kenya': 'KE', 'Finland': 'FI',
             'Austria': 'AT', 'Uganda': 'UG', 'Turkey': 'TR', 'New Zealand': 'NZ', 'Thailand': 'TH', 'Ghana': 'GH',
             'Saudi Arabia': 'SA', 'Lithuania': 'LT', 'Philippines': 'PH', 'Latvia': 'LV', 'Bulgaria': 'BG', 'Greece': 'GR'}

countries = list(new_codes.keys())
countries = sorted(countries)
countries.insert(0,'bite')
print(countries)
