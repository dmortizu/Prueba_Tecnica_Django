import csv
import re
from django.shortcuts import render
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .forms import CSVUploadForm

# Create your views here.

def validate_csv(file):
    errors = []
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
    try:
        decoded_file = file.read().decode('utf-8').splitlines()
        reader = csv.reader(decoded_file)
        
        for row_num, row in enumerate(reader, 1):
            if len(row) != 5:
                errors.append(f"Fila {row_num}: Número incorrecto de columnas ({len(row)})")
                continue
                
            for col_num, value in enumerate(row, 1):
                # Columna 1
                if col_num == 1:
                    if not value.isdigit():
                        errors.append(f"Fila {row_num}, Columna 1: No es un número entero")
                    elif not (3 <= len(value) <= 10):
                        errors.append(f"Fila {row_num}, Columna 1: Longitud inválida ({len(value)})")
                
                # Columna 2
                elif col_num == 2:
                    if not re.match(email_regex, value):
                        errors.append(f"Fila {row_num}, Columna 2: Email inválido")
                
                # Columna 3
                elif col_num == 3:
                    if value not in ['CC', 'TI']:
                        errors.append(f"Fila {row_num}, Columna 3: Valor inválido ({value})")
                
                # Columna 4
                elif col_num == 4:
                    try:
                        num = int(value)
                        if not (500000 <= num <= 1500000):
                            errors.append(f"Fila {row_num}, Columna 4: Valor fuera de rango ({num})")
                    except ValueError:
                        errors.append(f"Fila {row_num}, Columna 4: No es un número válido")
                
    except Exception as e:
        errors.append(f"Error al leer el archivo: {str(e)}")
    
    return errors


def upload_csv(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['file']
            if not csv_file.name.endswith('.txt'):
                return render(request, 'error.html', {'error': 'El archivo debe ser TXT'})
            
            errors = validate_csv(csv_file)
            
            if errors:
                return render(request, 'results.html', {'errors': errors})
            else:
                return render(request, 'success.html')
    else:
        form = CSVUploadForm()
    
    return render(request, 'upload.html', {'form': form})