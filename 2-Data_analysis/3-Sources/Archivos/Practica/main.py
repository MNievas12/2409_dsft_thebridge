import utils


ruta = "D:/Bootcamps_DS/24_09_Bootcamp_DS/2409_dsft_thebridge/2-Data_analysis/3-Sources/Archivos/Practica/carpeta_prueba"


categorias = {"Documentos": ('.doc', '.docx', '.txt', '.pdf', '.xls', '.ppt', '.xlsx', '.pptx'),
              "Imagenes": ('.jpg', '.jpeg', '.png', '.svg', '.gif'),
              "Software": ('.exe', '.py'),
              "Notebooks": ('.ipynb'),
              "Otros": ()}

utils.ordenar_carpeta(ruta, categorias)
