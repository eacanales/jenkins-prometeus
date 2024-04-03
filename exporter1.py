import pandas as pd

# Leer los datos del archivo de Excel
df = pd.read_excel('/home/bdu/projects/jenkins_prometheus/excel1.xls')

print()
print()

# Leer el contenido del archivo prometheus1.yml
with open('prometheus1.yml', 'r') as file:
    prometheus_content = file.read()
    
# Generar las configuraciones para los nuevos objetivos
new_targets = ''
for index, row in df.iterrows():
    location = row['location']
    target = row['target']
   
    new_targets += f'  - job_name: {location}\n'
    new_targets += '    static_configs:\n'
    new_targets += f'   - targets: ["{target}"]\n'
    
    new_targets += '\n'

# Insertar las nuevas configuraciones en el archivo prometheus.yml
modified_content = prometheus_content.replace('# INSERT NEW TARGETS HERE', new_targets)

# Escribir el contenido modificado de vuelta al archivo prometheus.yml
with open('prometheus1.yml', 'w') as file:
    file.write(modified_content)
    
