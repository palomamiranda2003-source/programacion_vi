EcoCharge es una aplicación desarrollada con Python y Flet, diseñada para simular una estación de carga de vehículos eléctricos. El proyecto busca ofrecer una interfaz moderna, minimalista y ecológica, inspirada en los sistemas de carga reales, priorizando la experiencia del usuario mediante una navegación fluida y visualmente atractiva.
La aplicación está compuesta por varias pantallas (vistas) conectadas entre sí, incluyendo:

* Pantalla de inicio/login: permite el acceso del usuario al sistema.
* Panel principal (Dashboard): punto central de navegación hacia las demás funciones.
* Vista de perfil: donde el usuario puede ver y editar su información.
* Simulador de carga: un flujo guiado dividido en pasos, donde el usuario selecciona el tipo de carga y el método de pago.

El diseño se basa en un esquema de colores verdes y blancos, con íconos grandes y componentes contrastantes para mejorar la legibilidad. La arquitectura modular separa cada pantalla en archivos independientes (login.py, dashboard.py, perfil.py, etc.), lo que facilita la mantenibilidad y escalabilidad del código.
El sistema utiliza los componentes visuales de Flet (Container, Column, Row, ElevatedButton, IconButton, Text, etc.) para construir una interfaz adaptable, estética y funcional, pensada tanto para escritorio como para dispositivos móviles.

