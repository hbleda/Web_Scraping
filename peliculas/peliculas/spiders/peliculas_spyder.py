import scrapy
import pandas as pd

class PeliculasSpider(scrapy.Spider):
    # Nombre de la araña
    name = "peliculas"
    
    # Dominios permitidos
    allowed_domains = ['es.wikipedia.org']
    
    # URLs para comenzar a rastrear
    start_urls = ['https://es.wikipedia.org/wiki/Anexo:Pel%C3%ADculas_con_las_mayores_recaudaciones']
    
    def parse(self, response):
        peliculas = []
        distribuidoras = []
        taquillas_EEUU = []
        taquillas_fuera_EEUU = []
        recaudaciones_mundial = []
        presupuestos = []
        anyos_estreno = []
        directores = []
        
        # Extraemos el nombre del producto, la descripcion y su precio
        table = response.css(".wikitable")
        filas = table.xpath(".//tr")[1:]     
    
        for fila in filas:
            celda = fila.xpath(".//td")
            # Verificar si hay suficientes celdas en la fila

            if len(celda) >= 8:
               pelicula = celda[0].xpath(".//i/a/text()").get()
               distribuidora = celda[1].xpath(".//a/text()").get()
               taquilla_EEUU = celda[2].xpath(".//text()").get().replace('\n', '')
               taquilla_fuera_EEUU = celda[3].xpath(".//text()").get().replace('\n', '')
               recaudacion_mundial = celda[4].xpath(".//text()").get()
               presupuesto = celda[5].xpath(".//text()").get().replace('\n', '')
               anyo_estreno = celda[6].xpath(".//a/text()").get()
               director = celda[7].xpath(".//a/text()").get()
    
               peliculas.append(pelicula)
               distribuidoras.append(distribuidora)
               taquillas_EEUU.append(taquilla_EEUU)
               taquillas_fuera_EEUU.append(taquilla_fuera_EEUU)
               recaudaciones_mundial.append(recaudacion_mundial)
               presupuestos.append(presupuesto)
               anyos_estreno.append(anyo_estreno)
               directores.append(director)
        data = {"Pelicula": peliculas, "Distribuidora": distribuidoras, "Taquilla en EEUU": taquillas_EEUU,
        "Taquilla fuera EEUU": taquillas_fuera_EEUU, "Recaudacion Mundial": recaudaciones_mundial,
        "Presupuesto": presupuestos,"Anyo Estreno": anyos_estreno,"Director": directores}

        df_taquilleras_scrapy = pd.DataFrame(data)
        df_taquilleras_scrapy.to_csv("mas_taquilleras_scrapy.csv", index=False, mode='w')