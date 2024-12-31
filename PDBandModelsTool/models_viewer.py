import py3Dmol
import os
import webbrowser

# Crear la vista con una cuadrícula de 1 fila y 2 columnas
view = py3Dmol.view(width=2000, height=600, viewergrid=(1, 2))

# Cargar dos estructuras PDB
view.addModel('pdb:1dc9', "pdb")  # Cargar la primera estructura
view.addModel('pdb:2d3k', "pdb")  # Cargar la segunda estructura

# Estilos para la primera estructura (modelo 0)
view.setStyle({'model': 0, 'stick': {}})
view.setStyle({'model': 0, 'cartoon': {'arrows': True, 'tubes': True, 'style': 'oval', 'color': 'white'}})

# Estilos para la segunda estructura (modelo 1)
view.setStyle({'model': 1, 'stick': {'colorscheme': 'greenCarbon'}})
view.setStyle({'model': 1, 'cartoon': {'color': 'spectrum'}})

# Ajustar el zoom y mostrar la visualización
view.zoomTo()

# Obtener el HTML de la visualización
html_output = view.get_html()

# Guardar en un archivo HTML
html_file = "visualizacion.html"
with open(html_file, "w") as file:
    file.write(html_output)

# Abrir el archivo HTML en el navegador
webbrowser.open(f"file://{os.path.abspath(html_file)}")

