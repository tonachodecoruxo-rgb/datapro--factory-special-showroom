Markdown# Thermal-BMS 2025: Independent Battery Health & Thermal Management Dataset

![Status](https://img.shields.io/badge/Status-Project_Live-brightgreen)
![Sector](https://img.shields.io/badge/Sector-Automotive_Intelligence-blue)
![Format](https://img.shields.io/badge/Format-JSON%20%7C%20CSV%20%7C%20Parquet-orange)
![License](https://img.shields.io/badge/License-Commercial_Restricted-red)

## 📋 Resumen Ejecutivo
**Thermal-BMS 2025** es un repositorio de datos de alta fidelidad centrado en la lógica de gestión térmica y degradación de baterías de vehículos **PHEV (Híbridos Enchufables)** y **MHEV (Microhíbridos)** de última generación (2022-2025). 

Este activo resuelve la **asimetría de información** entre fabricantes y compradores (B2B/B2C), proporcionando transparencia radical sobre cómo el software de gestión (BMS) protege o limita la vida útil de la batería en condiciones de uso real.

---

## 🛠 Metodología RSR (powered by datapro+)
Este dataset ha sido construido siguiendo el proceso crítico de procesamiento de cuatro fases:

1.  **Escaneo:** Minado de datos desestructurados de ingeniería inversa de firmware, boletines técnicos oficiales y telemetría crowdsourced de comunidades de usuarios.
2.  **Target Lock (Bloqueo):** Aislamiento de variables críticas, correlacionando la temperatura de batería con la activación de flags de limitación de carga (Thermal Throttling).
3.  **Inyección:** Normalización, anonimización (cumplimiento RGPD) y estructuración en JSON puro para su uso inmediato en modelos de IA y análisis predictivo.
4.  **Entrega:** Distribución en formatos optimizados para Big Data.

---

## 📂 Estructura del Repositorio
```text
/Thermal-BMS-2025
├── /data        # Datasets procesados (JSON/CSV) listos para análisis.
├── /scripts     # Lógica de limpieza y algoritmos predictivos.
├── /docs        # Dossiers Técnicos, ROI y Estrategia de Marketing.
└── /meta        # Glosario técnico, fuentes de evidencia y metadatos.
📊 Especificaciones del Dataset (Sample Key)CampoDescripciónValor Ejemplovehicle_id_hashIdentificador anonimizado (HASH)8f2d4a1...BMS_firmwareVersión del software de batería detectadaBMS_v4.2.0_STThermal_Throttling_ActiveFlag de limitación de carga por calorTrueSoH_Prediction_5YProyección de salud de batería a 5 años84.2%⚖️ Licencia y AccesoEste dataset se distribuye bajo una Licencia Comercial Restringida (ver archivo LICENSE).Uso Educativo/Demo: Acceso a la documentación y muestra de datos limitada.Uso Profesional: Requiere la adquisición de una licencia de explotación para acceso completo a la API y actualizaciones.✍️ Autoría y CréditosProject Lead: Antonio Rodriguez Martinez (gmant system)Intelligence Architect: Tonhy (CIH - Capsule Intelligence Hybrid)Fecha: 14 de marzo de 2026