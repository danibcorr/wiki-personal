---
authors: Daniel Bazo Correa
description: Ejercicios típicos de entrevistas de trabajo.
title: Ejercicios SQL
---

## Ejercicios básicos

A continuación se presenta un conjunto de tablas de ejemplo que pueden ser utilizadas
para practicar consultas SQL fundamentales, tales como selección, agregación, joins y
filtrado de datos.

### Tablas de ejemplo

`job_posting_fact`

Esta tabla contiene información sobre ofertas de trabajo, incluyendo el título del
puesto, salario promedio anual y ubicación.

| job_id | job_title_short  | job_title               | salary_year_avg | job_location |
| ------ | ---------------- | ----------------------- | --------------- | ------------ |
| 1      | Data Analyst     | Junior Data Analyst     | 95,000          | Boston, MA   |
| 2      | Business Analyst | Senior Business Analyst | 120,000         | Anywhere     |
| 3      | Data Analyst     | Data Analyst            | 105,000         | Boston, MA   |
| 4      | Business Analyst | Business Analyst        | 75,000          | Anywhere     |

`invoices_fact`

Esta tabla registra facturas asociadas a proyectos, indicando las horas trabajadas y la
tarifa por hora.

| invoice_id | project_id | hours_spent | hours_rate |
| ---------- | ---------- | ----------- | ---------- |
| 101        | 1          | 10          | 50         |
| 102        | 2          | 20          | 60         |
| 103        | 1          | 15          | 55         |
| 104        | 3          | 25          | 65         |

`skills_dim`

Contiene el listado de habilidades disponibles, cada una con un identificador único.

| skill_id | skills            |
| -------- | ----------------- |
| 1        | SQL               |
| 2        | Data Analysis     |
| 3        | Business Analysis |

`skills_job_dim`

Relaciona las habilidades con los trabajos correspondientes, funcionando como una tabla
de asociación en un modelo de datos tipo estrella.

| skill_id | job_id |
| -------- | ------ |
| 1        | 1      |
| 2        | 1      |
| 2        | 3      |
| 3        | 2      |
| 3        | 4      |

Estas tablas permiten realizar ejercicios prácticos de SQL, tales como consultar el
salario promedio de ciertos roles, identificar qué habilidades están asociadas a cada
trabajo o calcular el costo total de horas facturadas por proyecto.

### Obtener detalles de trabajos para 'Data Analyst' o 'Business Analyst'

Obtener detalles de trabajos para las posiciones de 'Data Analyst' o 'Business Analyst'.
Para 'Data Analyst', solo quiero trabajos con salario > \$100k, y para 'Business
Analyst', solo quiero trabajos con salario > \$70k. Incluir solo trabajos ubicados en
'Boston, MA' o 'Anywhere'.

??? info "Solución"

    ```sql  linenums="1"
    SELECT
        job_posting_fact.job_title_short,
        job_posting_fact.salary_year_avg,
        job_posting_fact.job_location
    FROM
        job_posting_fact
    WHERE
        job_location IN ('Boston, MA', 'Anywhere') AND
        (
            (job_title_short = 'Data Analyst' AND salary_year_avg > 100000) OR
            (job_title_short = 'Business Analyst' AND salary_year_avg > 70000)
        );
    ```

### Buscar roles de analista no senior

Buscar roles de 'Data Analyst' o 'Business Analyst' que no sean senior. Obtener el
título del trabajo, la ubicación y el salario promedio anual.

??? info "Solución"

    ```sql  linenums="1"
    SELECT
        job_posting_fact.job_title,
        job_posting_fact.job_location,
        job_posting_fact.salary_year_avg
    FROM
        job_posting_fact
    WHERE
        job_title NOT LIKE '%Senior%' AND
        (job_title LIKE '%Data%' OR job_title LIKE '%Business%') AND
        job_title LIKE '%Analyst%';
    ```

### Calcular ganancias totales del mes actual por proyecto

Calcular las ganancias totales del mes actual por proyecto. Calcular un escenario donde
la tarifa por hora aumenta en \$5.

??? info "Solución"

    ```sql  linenums="1"
    SELECT
        invoices_fact.project_id AS Proyecto,
        SUM(invoices_fact.hours_spent * invoices_fact.hours_rate) AS Coste_original,
        SUM(invoices_fact.hours_spent * (invoices_fact.hours_rate + 5)) AS Coste_incremento
    FROM
        invoices_fact
    GROUP BY
        Proyecto
    ORDER BY
        project_id;
    ```

### Encontrar el salario promedio y el número de ofertas de trabajo por habilidad

Encontrar el salario promedio y el número de ofertas de trabajo para cada habilidad.

??? info "Solución"

    ```sql  linenums="1"
    SELECT
        skills_dim.skills AS skill_name,
        COUNT(job_postings_fact.job_title) AS number_of_job_posting,
        AVG(job_postings_fact.salary_year_avg) AS average_salary_for_skill
    FROM
        skills_dim
    LEFT JOIN skills_job_dim ON skills_dim.skill_id = skills_job_dim.skill_id
    LEFT JOIN job_postings_fact ON skills_job_dim.job_id = job_postings_fact.job_id
    GROUP BY
        skill_name
    ORDER BY
        average_salary_for_skill DESC;
    ```
