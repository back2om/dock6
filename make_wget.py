
file_O = open("./ZINC-downloader-3D-db2.gz.wget","w")
file_O2= open("./ZINC15.uri","w")

with open("./ZINC-downloader-3D-db2.gz.uri") as fp:
	for line in fp:
		line = str(line)
		Source_dir = line[28:35]
		db2_name = line[36::]

		dest_line = 'mkdir -pv ' +  Source_dir + ' && wget ' + line[0:-1] + ' -O ' + Source_dir + '/' + db2_name
		file_O.writelines(dest_line)

                dest_line2 = '/net/bornem/home/chakra/omchoudhary/Energy_calc/lig_db2/' + Source_dir + '/' + db2_name
                file_O2.writelines(dest_line2)

file_O.close()
file_O2.close()

