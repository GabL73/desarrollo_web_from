<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Recomendaciones para tu Pelo</title>
    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background-color: #fff5f8;
            display: flex;
        }

        /* Barra lateral izquierda - Sugerencias */
        .sugerencias {
            width: 180px;
            background-color: #ffffff;
            border-right: 3px solid #333;
            padding: 20px;
            min-height: 100vh;
            writing-mode: vertical-rl;
            transform: rotate(180deg);
            text-align: center;
            font-size: 22px;
            font-weight: bold;
            letter-spacing: 2px;
        }

        /* Contenedor principal */
        .contenido {
            flex: 1;
            padding: 30px;
            border: 3px solid #333;
            margin: 20px;
            background: white;
        }

        /* TÍTULO EN ROSA */
        .titulo {
            text-align: center;
            color: #ff4da6; /* rosa */
            font-size: 42px;
            border: 2px solid #333;
            padding: 15px;
            margin-bottom: 25px;
        }

        /* Parte de abajo: imagen + lado derecho */
        .abajo {
            display: flex;
            gap: 20px;
        }

        .imagen-box {
            width: 35%;
            border: 2px solid #333;
            padding: 10px;
            text-align: center;
        }

        .imagen-box img {
            width: 100%;
            border-radius: 10px;
        }

        .derecha {
            width: 65%;
            display: flex;
            flex-direction: column;
            gap: 20px;
        }

        /* ENCABEZADO CAMBIADO POR TIPS */
        .tips {
            border: 2px solid #333;
            padding: 20px;
        }

        .tips h2 {
            color: #ff4da6;
            margin-top: 0;
        }

        .tips ul {
            font-size: 18px;
            line-height: 1.6;
        }
    </style>
</head>
<body>

    <!-- LADO IZQUIERDO -->
    <div class="sugerencias">
        SUGERENCIAS
    </div>

    <!-- CONTENIDO PRINCIPAL -->
    <div class="contenido">

        <!-- TÍTULO -->
        <div class="titulo">
            ¿Qué le queda a tu pelo?
        </div>

        <div class="abajo">

            <!-- IMAGEN - MUJER DE ESPALDAS -->
            <div class="imagen-box">
                <img src="pelo.jpg" alt="Mujer de espaldas mostrando su pelo">
                <p><b>Ella busca recomendación para su pelo</b><br>
                De espaldas, de cintura para arriba, para ver solo su cabello.</p>
            </div>

            <!-- LADO DERECHO -->
            <div class="derecha">

                <!-- ANTES ERA ENCABEZADO, AHORA ES TIPS -->
                <div class="tips">
                    <h2>Tips - Recomendación según tu pelo</h2>
                    <ul>
                        <li><b>Color:</b> Balayage caramelo si lo quieres natural, o cobrizo si lo quieres llamativo.</li>
                        <li><b>Estilo:</b> Chino, Ondulado o Lacio - el ondulado le queda a casi todo tipo de cara.</li>
                        <li><b>Corte:</b> En capas para dar volumen, o corte recto si lo quieres más largo y sano.</li>
                        <li><b>Tratado:</b> Hidratación profunda 1 vez por semana, no plancha diario.</li>
                        <li><b>Producto recomendado:</b> Shampoo sin sulfatos + mascarilla con keratina.</li>
                    </ul>
                </div>

                <div class="tips">
                    <h2>Tips extra</h2>
                    <p>Si tu pelo es chino, no lo peines en seco. Si es lacio, usa protector de calor. Si es ondulado, defínelo con crema para peinar.</p>
                </div>

            </div>
        </div>
    </div>

</body>
</html>