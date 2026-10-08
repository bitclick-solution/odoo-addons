=========================
Bitclick: tema de marca
=========================

Lleva el sistema de diseño 2026 de Bitclick (bitclick.solutions) al backend
y a la pantalla de acceso de Odoo 19 Community.

Qué cambia
==========

* **Color.** Grises con sesgo verde y tinta ``#080A09``. Verde ``#00752F``
  para enlaces, estados activos, foco y éxito (automático y estado).
  Botón principal en amarillo ``#FFDE00`` con texto negro (persona y acción).
  Valores tomados de ``web/src/index.css`` del repo ``bitclick-solution/server``.
* **Barra superior** oscura ``#0A0B0A``, como el pie de la web.
* **Tipografía** autoalojada: Inter (texto), Space Grotesk (titulares) y
  JetBrains Mono (código). Nada se pide a terceros.
* **Forma.** Botones en píldora; diálogos y desplegables con 14 px de radio.
* **Un principal por pantalla.** «Enviar mensaje» del chatter pasa a secundario.
* **Acceso** (``/web/login``): tarjeta blanca con hilo, botón amarillo.

Qué no cambia
=============

* El logo de la empresa, el favicon y el icono de la app: son datos
  (Ajustes → Compañías, ``web_favicon`` y ``web_pwa_customize``).
* El diseño de facturas y presupuestos: Ajustes → Diseño del documento.

Mantenimiento
=============

Casi todo son variables SCSS de Odoo (``static/src/scss/primary_variables.scss``),
que suelen sobrevivir entre versiones. Las pocas reglas CSS de
``backend.scss`` y ``login.scss`` hay que revisarlas al migrar.

Tras actualizar el módulo, **reinicia Odoo**: el paquete de estilos compilado
no siempre se regenera solo.

Fuentes
=======

Inter, Space Grotesk y JetBrains Mono se distribuyen con la SIL Open Font
License 1.1. Son los mismos ficheros que sirve bitclick.solutions.
