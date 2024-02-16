# ----------------
# Creator: Dr. Evil
# Date: 02/16/2024
# Data Reader for Caw Data Set (NOTE: dataset itself is NOT redistributable.
#   users should download it from the owner website: https://github.com/GU-DataLab/stance-detection-KE-MLM?tab=readme-ov-file
# ----------------

from itfc import *; 
import csv;
import re;

class CawDataReader(RawDataReader):
	def __init__(self, data_path):
		self.src_data = data_path;
		print("constructor for CawDataReader");

	def get_raw_data(self, start_date, end_date):	
		s = open(self.src_data).read();
		print(s);
		r1 = re.compile("\"([0-9]+)\",\"(.*?)\".*?(FAVOR|NONE|AGAINST)\"", re.DOTALL|re.MULTILINE);
		arr_matches = r1.findall(s);

		arr_ret = [];
		for m in arr_matches:
			stext = m[1];
			print("---" , stext);
			arr_ret.append( [start_date, stext] ); # should improve.
		# distribute the dates

		return arr_ret;
