# Cruzar-No-Llames-Argentina

Script en Python que permite comparar una base de números telefónicos en Excel contra el **Registro No Llame Nacional** de Argentina, para detectar qué números se encuentran registrados y retirarlos de la base antes de realizar llamadas.

Pensado para uso simple dentro de empresas, call centers o cualquier persona que necesite validar bases telefónicas sin conocimientos técnicos avanzados.

---

# ¿Para qué sirve?

Si tenés una base de teléfonos para contactar clientes, este sistema permite revisar automáticamente cuáles números figuran en el **Registro No Llame**.

De esa forma podés limpiar tu base y evitar llamar a números registrados.

---

# Requisitos

Antes de usarlo, necesitás tener instalado en la computadora:

## 1. Python 3

Descargar desde:

https://www.python.org/downloads/

Durante la instalación, marcar la opción:

```text id="py11aa"
Add Python to PATH
```

---

## 2. Librerías necesarias

**Pandas no viene incluido por defecto con Python**, por lo tanto hay que instalarlo manualmente.

Abrir **CMD** o **Símbolo del sistema** y ejecutar:

```bash id="py22bb"
pip install pandas openpyxl
```

---

# Preparación de carpetas

El archivo `.bat` busca el proyecto dentro de una carpeta llamada exactamente:

```text id="py33cc"
Cruzar-No-Llames-Argentina
```

Por lo tanto, se recomienda:

1. Descargar o clonar el repositorio.
2. Copiar todos los archivos dentro de una carpeta con ese nombre:

```text id="py44dd"
Cruzar-No-Llames-Argentina
```

3. Mantener todos los archivos dentro de esa misma carpeta.

---

# Archivos del proyecto

Dentro de la carpeta vas a encontrar:

* `Repetidos.py` → Script principal
* `.bat` → Archivo para ejecutar fácilmente
* `números-template.xlsx` → Plantilla para cargar números
* `duplicados.xlsx` → Se genera automáticamente al finalizar

---

# Cómo usarlo (Paso a paso)

## Paso 1 - Descargar el padrón Registro No Llame

Descargar el archivo oficial del Registro No Llame en formato `.txt`.

Luego copiarlo dentro de la carpeta del proyecto con este nombre exacto:

```text id="py55ee"
Registro_No_Llame.txt
```

> Si viene con fecha en el nombre, renombrarlo.

Ejemplo:

```text id="py66ff"
Registro_No_Llame_20260112.txt
```

Renombrar a:

```text id="py77gg"
Registro_No_Llame.txt
```

---

## Paso 2 - Preparar la base de números propia

Abrir el archivo:

```text id="py88hh"
números-template.xlsx
```

En la primera columna pegar todos los números que se desean verificar.

Ejemplo:

| Numero     |
| ---------- |
| 3511234567 |
| 3519876543 |
| 1134567890 |

Luego guardar el archivo como:

```text id="py99ii"
números.xlsx
```

Dentro de la misma carpeta del proyecto.

---

## Paso 3 - Ejecutar el proceso

Hacer doble clic en el archivo:

```text id="py10jj"
.bat
```

Se abrirá una ventana negra (CMD).

Presionar una tecla cuando lo solicite y esperar a que finalice el proceso.

---

# Resultado final

Cuando termina, se genera automáticamente el archivo:

```text id="py20kk"
duplicados.xlsx
```

Ese archivo contiene **todos los números encontrados dentro del Registro No Llame**.

Esos números son los que conviene eliminar o excluir de la base original.

---

# Cómo filtrar la base original con BUSCARV

Una vez generado `duplicados.xlsx`, podés usar **BUSCARV** en Excel para marcar o identificar esos números dentro de tu base original.

Ejemplo:

```excel id="py30ll"
=BUSCARV(A2,[duplicados.xlsx]Hoja1!A:A,1,FALSO)
```

Si encuentra coincidencia, ese número figura en el Registro No Llame.

Luego podés filtrar y eliminar esos registros.

---

# Recomendaciones

* Colocar todos los archivos dentro de la carpeta `Cruzar-No-Llames-Argentina`
* No modificar nombres de archivos excepto lo indicado.
* Esperar a que termine el proceso antes de cerrar la ventana.
* Si la base es grande, puede tardar algunos segundos.

---

# Solución de problemas

## No abre el .bat

Verificar que Windows permita ejecutar archivos `.bat`.

---

## Dice que Python no está instalado

Reinstalar Python marcando:

```text id="py40mm"
Add Python to PATH
```

---

## No genera duplicados.xlsx

Verificar que existan:

* `Registro_No_Llame.txt`
* `números.xlsx`

---

# Licencia

Uso libre.
