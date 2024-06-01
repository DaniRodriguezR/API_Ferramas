from app import connection
from flask import current_app
from .to_dolar_api.to_dolar import fetch_dolar_data


def fetch_all_tools():
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT h.id_herramienta, h.nombre, c.categoria, h.valor, h.imagen FROM herramientas h JOIN categorias c on h.id_categoria = c.id_categoria order by h.nombre, c.categoria, h.valor, h.imagen")
        rows = cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        dolar_value = fetch_dolar_data()

        data = []

        for row in rows:
            tool_info = dict(zip(columns, row))
            value = tool_info.get('VALOR')
            tool_info['VALOR_EN_DOLAR'] = round(value/dolar_value, 2)
            data.append(tool_info)
        return data
    except Exception as e:
        current_app.logger.error(f"Error al buscar herramientas: {e}")
        return []
    finally:
        cursor.close()

def fetch_tools_by_code(id):
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM herramientas WHERE id_herramienta=%s", (id,))
        data = cursor.fetchone()
        return data
    except Exception as e:
        current_app.logger.error(f"Error al buscar herramienta por id {id}: {e}")
        return None
    finally:
        cursor.close()
