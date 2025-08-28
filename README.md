# Silent Data Thieves: Investigating Malicious Data Exfiltration Packages in PyPI
This paper presents the first comprehensive empirical study of malicious PyPI data exfiltration packages. 

We investigate five research questions to understand their prevalence, attack patterns, disguise techniques, exfiltration objectives, and the effectiveness of current detection tools. 

## You can reproduce our research according to the following steps:
`record_list_all_pkg.xlsx` records 617 randomly selected malware from the database, of which 83 data exfiltration packages were filtered out.  The document provides a detailed record of their malicious behavior, and subsequent conclusions for RQ2-RQ4 are based on this document. 
## RQ1
We use [Bigquery](https://cloud.google.com) to obtain the download count of malware. We have confirmed that the earliest release time of the data exfiltration package was in 2017, so the time interval for searching download counts is from 2017 to 2024.
`download_count_data_exfiltration_all.xlsx` records the download count of the selected data exfiltration package.
`download_count_malware_all.xlsx` records the download count of the 83 * 3 generic malware.
You can run the following file to get figure 2:
```
python line_chart.py
```
## RQ2
`classification_of_attack_patterns.xlsx` records the attack patterns of each data exfiltration package.
## RQ3
`Disguise_Targets.xlsx` records the disguise targets of each data exfiltration package. 
`Disguise_Techniques.xlsx` records the disguise techniques. 
`metadata_data_exfiltration.xlsx` records the metadata. 
You can run the following file to get figure 7:
```
python Disguise_Targets_figure.py
```
## RQ4
`Objective.xlsx` records the objects of each package and the malicious behavior used to determine the objects.
## RQ5
The results of all five detecting tools are recorded in the file `final_result.xlsx`. 
File `A-xx` represents the list of xx benign packages under Benchmark A, and `B-xx` represents Benchmark B. 
`data_exfiltration.xlsx` is the list of data exfiltration packages, and `malware.xlsx` is the list of generic malware.  
The detailed detection results of the four tools are stored in four subfolders, and EA4MP only has the final results. 
