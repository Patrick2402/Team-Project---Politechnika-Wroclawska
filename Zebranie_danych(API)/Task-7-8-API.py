import requests
import csv
import json
import time

with open('Zebranie_danych(API)/cve_result.csv', mode='w',newline='') as csv_file:
    fieldnames = ['id', 'published', 'version', 'vectorString', 'baseScore', 'version31', 'vectorString31', 'baseScore31', 'version30', 'vectorString30', 'baseScore30']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for x in range (0,209691,2000):
        url = "https://services.nvd.nist.gov/rest/json/cves/2.0/?resultsPerPage=2000&startIndex="+str(x)
        response = requests.get(url)

        if response.status_code == 200:
            data = json.loads(response.content.decode('utf-8'))
            vulnerabilities = data['vulnerabilities']

            with open(f'Zebranie_danych(API)/json/cve_result_{x}.json', 'w') as json_file:
                json.dump(data, json_file)



            for vulnerability in vulnerabilities:
                cve = vulnerability['cve']
                id = cve['id']
                published = cve.get('published', 'n/a')
                metrics = cve.get('metrics', {})
                cvssMetricV2 = metrics.get('cvssMetricV2', [])
                cvssMetricV31 = metrics.get('cvssMetricV31',[])
                cvssMetricV30 = metrics.get('cvssMetricV30',[])
                if cvssMetricV2:
                    cvss = cvssMetricV2[0]
                    version = cvss['cvssData']['version']
                    vectorString = cvss['cvssData']['vectorString']
                    baseScore = cvss['cvssData']['baseScore']
                else:
                    version = 'n/a'
                    vectorString = 'n/a'
                    baseScore = 'n/a'

                if cvssMetricV31:
                    cvss31 = cvssMetricV31[0]
                    version31 = cvss31['cvssData']['version']
                    vectorString31 = cvss31['cvssData']['vectorString']
                    baseScore31 = cvss31['cvssData']['baseScore']
                else:
                    version31 = 'n/a'
                    vectorString31 = 'n/a'
                    baseScore31 = 'n/a'
                
                if cvssMetricV30:
                    cvss30 = cvssMetricV30[0]
                    version30 = cvss30['cvssData']['version']
                    vectorString30 = cvss30['cvssData']['vectorString']
                    baseScore30 = cvss30['cvssData']['baseScore']
                else:
                    version30 = 'n/a'
                    vectorString30 = 'n/a'
                    baseScore30 = 'n/a'

                writer.writerow({'id': id, 'published': published, 'version': version, 'vectorString': vectorString, 'baseScore': baseScore,'version31': version31, 'vectorString31': vectorString31, 'baseScore31': baseScore31,'version30': version30, 'vectorString30': vectorString30, 'baseScore30': baseScore30})
            print(x,'ok')
        else:
            print("Failed to retrieve CVEs from NIST API", url)
        time.sleep(60)
