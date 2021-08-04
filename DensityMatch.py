import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# CSV Files for functions below

archive_csv = 'C:/WRDensityExport101ran7.14.21.csv'
pink_csv = 'C:/WHAPinkCSV.csv'

# Read CSV, parse specific column as date64.
# Reassign StudyDate as string for concat function.
# Reassign PatientsBirthDate as string for concat function.
# Concat into new column twice.

def archive_data(csv):
	archive_data = pd.read_csv(csv, parse_dates=['PatientsBirthDate'])
	archive_data['StudyDate'] = archive_data['StudyDate'].astype(str)
	archive_data['PatientsBirthDate'] = archive_data['PatientsBirthDate'].astype(str)
	archive_data['PatientId'] = archive_data['PatientId'].str.replace("_FIX1_", "")
	archive_data['a_concat_1'] = archive_data['PatientsName'] + archive_data['PatientsBirthDate'] + archive_data['StudyDate']
	archive_data['a_concat_2'] = archive_data['PatientId'] + archive_data['PatientsBirthDate'] + archive_data['StudyDate']
	return archive_data

# Read CSV, parse specific column as date64.
# Reassign StudyDate as string for concat function.
# Reassign PatientsBirthDate as string for concat function.
# Concat into new column twice.

def pink_data(csv):
	pink_data = pd.read_csv(csv, parse_dates=['DOB'])
	pink_data['DOB'] = pink_data['DOB'].astype(str)
	pink_data['examdate'] = pink_data['examdate'].astype(str)
	pink_data['p_concat_1'] =  pink_data['LName'] + "^" + pink_data['FName'] + pink_data['DOB'] + pink_data['DOB']
	pink_data['p_concat_2'] = pink_data['mrn'] + pink_data['DOB'] + pink_data['examdate']
	return pink_data

# Plot out density using seaborn

def show_density(df, csv):
	df = pink_data(csv)
	df = df.groupby(by="densityid").count()
	df = pd.DataFrame(df)
	graph = sns.barplot(x = df.index, y = 'mrn', data=df)
	graph = plt.show()
	return graph

pink = pink_data(pink_csv)
archive = archive_data(archive_csv)

a = pd.concat([pink, archive], axis=0, ignore_index=True)

print(test)

#pink = pink_data(pink_csv)

#show_density(pink, pink_csv)