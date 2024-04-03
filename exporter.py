# To develop this code, you need to install pip3, pandas and xlrd
import pandas as pd

df = pd.read_excel('/home/bdu/projects/jenkins_prometheus/excel1.xls')

print(df.head(30))

# Abrir el archivo prometheus.yml para escritura
with open('prome.yml', 'w') as file:
    file.write('scrape_configs:\n')
    
    # Iterar sobre las filas del DataFrame
    for index, row in df.iterrows():
        location = row['location']
        target = row['target']
        labels = row['labels']
        
        # Escribir la configuración de scrape para cada objetivo
        file.write(f'  - job_name: {location}\n')
        file.write('    static_configs:\n')
        file.write('      - targets: [' + f'"{target}"' + ']\n')
        
        # Escribir las etiquetas si están disponibles
        #if pd.notna(labels):
        #    file.write(f'    labels:\n')
        #    for label in labels.split(','):
        #        key, value = label.split(':')
        #        file.write(f'      {key.strip()}: {value.strip()}\n')


