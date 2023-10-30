import gspread
import os
import gdown    
from mathpix import extract_text
sa = gspread.service_account(filename='serivce_creds.json')
sh = sa.open("Figma_swe")

wks = sh.worksheet("Sheet1")
data = wks.get_all_values()
link=data[1][3]
id=link.split('=')[-1]
print(data[0])

# destination_path = os.path.join(os.getcwd(), id)
for i in range(1, len(data)):
    print(data[i])



gdown.download(id=id, quiet=True, use_cookies=False, output='tmp.pdf')


# print(extract_text('tmp.pdf'))







