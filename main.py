import time

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

bot = Bot(token='<you_token>')
dp = Dispatcher(bot)

answers = []

op_1 = KeyboardButton('Metodos Anticonceptivos 🛡')
op_2 = KeyboardButton('Cuidado intimo ❤🤷‍♂️')
lang3 = KeyboardButton('Otros 🤝')
menu_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(op_1).add(op_2).add(lang3)


@dp.message_handler(commands=['start', 'help'])
async def welcome(message: types.Message):
        await message.answer('Hola!, Bienvenida/o a FemiBot, por favor selecciona una opcion del menu', reply_markup=menu_kb)

#-------------------------------------------------------------------------------------
method_op_1 = KeyboardButton('Condon masculino')
method_op_2 = KeyboardButton('Condon Femenino')
method_op_3 = KeyboardButton('Pilora anticonceptivas')
method_op_4 = KeyboardButton('Anillo hormonal')
method_op_5 = KeyboardButton('Inyeccion anticonceptiva')
method_op_6 = KeyboardButton('Calendario de dias fertiles')
method_op_7 = KeyboardButton('Parche Anticonceptiva')
method_op_8 = KeyboardButton('DIU')
method_op_menu = KeyboardButton('Volver al menu principal 🏠')
method_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)\
    .add(method_op_1)\
    .add(method_op_2)\
    .add(method_op_3)\
    .add(method_op_4)\
    .add(method_op_5)\
    .add(method_op_6)\
    .add(method_op_7)\
    .add(method_op_8)\
    .add(method_op_menu)


@dp.message_handler(regexp='Metodos Anticonceptivos 🛡')
async def english(message: types.Message):
    answers.append(message.text)
    await message.answer('Elige el metodo que mas te interasa', reply_markup=method_kb)


#CONDON MASCULINO
cm_op_1 = KeyboardButton('CÓMO?')
cm_op_2 = KeyboardButton('PROS Y CONTRAS ✔|❌')
cm_op_volver = KeyboardButton('VOLVER 🔙')
cm_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)\
    .add(cm_op_1)\
    .add(cm_op_2)\
    .add(cm_op_volver)\

@dp.message_handler(regexp='Condon masculino')
async def welcome(message: types.Message):
        await message.answer_photo(photo=open('./img/condon.png', 'rb'),
                                   caption='El condón, uno de los métodos anticonceptivos más populares, es una forma simple y barata de prevenir embarazos no planeados y ETS. El condón actúa capturando los espermatozoides a medida que éstos se liberan e impidiendo que entren a la vagina. La punta tiene un reservorio que colecta el semen del hombre e impide que entre a la vagina durante la eyaculación. Junto con los condones femeninos, son el único método anticonceptivo que te protege contra ETS y contra el embarazo. Lo más importante es que uses un condón cada vez que tengas sexo.')

        await message.answer("""
CÓMO? 🤷‍♀

Usar el condón es fácil, solo desenrolla el condón sobre el pene erecto justo antes del sexo y ya está. Una vez que hayas terminado y el condón haya cumplido con su función, quítalo antes de que el pene se ablande. Se debe sujetar contra la base del pene tan pronto como haya ocurrido la eyaculación para asegurarse de que no se deslice y para prevenir que el semen se escape al retirar el pene. Úsalo una vez y después tíralo Es importante revisar qué tipo de lubricante es apropiado para usar con cada uno de los materiales de los condones ya que algunos pueden tener efectos adversos sobre el material. Por ejemplo, los lubricantes a base de aceite no se llevan bien con el látex y el ponerlos juntos puede hacer que el condón se rompa o se deslice, solo para que sepas.
        """)

        await message.answer("""
PROS Y CONTRAS ✔|❌

Pros ✔
✔ Se puede usar a libre demanda
✔ Puedes llevarlo contigo fácilmente
✔ No se afecta por el uso de otros medicamentos
✔ Se puede usar cuando se está amamantando
✔ Sin hormonas
✔ Es fácil de usar
✔ Es la mejor protección contra VIH/SIDA y otras enfermedades de transmisión sexual (ETS)

Contras ❌
❌ Interrumpe el sexo
❌ Se puede romper o salir durante el sexo si no se usa correctamente
❌ Algunas personas son alérgicas a los condones de látex
❌ Puede producir irritación o reacciones alérgicas (si eres alérgico al látex puedes probar condones de poliuretano)
        """)



#CONDON FEMENINO
@dp.message_handler(regexp='Condon Femenino', )
async def welcome(message: types.Message):
        await message.answer_photo(photo=open('./img/condon_femenino.png', 'rb'),
                                   caption='El condón masculino bien podría ser el método anticonceptivo más conocido y, para no quedarse atrás, las mujeres también tienen el suyo. Lo práctico del condón masculino que “simplemente se pone” es comparable a la técnica del condón femenino que “simplemente se pone” y los resultados son idénticos. Independientemente de quién esté usando el condón, hay una delgada funda de poliuretano que crea una barrera entre el lugar de donde vienen los espermatozoides y el lugar al cual quieren llegar. Lo más importante es que uses un condón cada vez que tengas sexo.')
        await message.answer("""
CÓMO? 🤷‍♀️

Como dijimos antes, los condones masculino y femenino actúan exactamente de la misma manera, la única diferencia es quién se lo pone, por fuera o por dentro. Coloca el condón femenino dentro de la vagina inmediatamente antes del sexo. Toma la funda e identifica el anillo del extremo cerrado que sostiene el condón femenino en su lugar. Aprieta este anillo flexible e introduce el condón como lo harías con un tampón, tanto como puedas hacia el cérvix. El extremo cerrado del condón femenino cubre el cérvix y el extremo abierto debe sobresalir una pulgada (2.5 cm) de tu vagina. Una vez que has terminado, simplemente toma el extremo abierto, gíralo para cerrarlo, jálalo suavemente y no derrames el contenido. Úsalo solo una vez y tíralo.
        """)

        await message.answer("""
PROS Y CONTRAS ✔|❌

Pros ✔
✔ Se puede usar a libre demanda
✔ Puedes llevarlo contigo fácilmente
✔ No se afecta por el uso de otros medicamentos
✔ Se puede usar cuando se está amamantando
✔ Sin hormonas
✔ Es fácil de usar
✔ Es la mejor protección contra VIH/SIDA y otras enfermedades de transmisión sexual (ETS)

Contras ❌
❌ Interrumpe el sexo
❌ Su uso puede requerir práctica
❌ No es tan efectivo como el condón masculino de látex
❌ Se puede rasgar si no se usa correctamente
❌ Puede producir irritación o reacciones alérgicas
        """)


# PILDORA ANTICONCEPTIVA

@dp.message_handler(regexp='Pilora anticonceptivas')
async def welcome(message: types.Message):
        await message.answer_photo(photo=open('./img/pildora.png', 'rb'),
                                   caption='La Píldora es una tableta que tomas una vez al día – existen unos cuantos tipos diferentes de píldoras. La píldora combinada contiene estrógeno y progestina, que impiden que los ovarios liberen óvulos. También hacen que el moco cervical sea más espeso, lo que no permite que los espermatozoides lleguen al óvulo. La llamada mini-píldora contiene solo una hormona, una progestina, lo que ofrece una alternativa a aquellas mujeres a las que los estrógenos les afectan.')
        await message.answer("""
CÓMO? 🤷‍♀️

Tomar la píldora es igual que tomar otras tabletas, solo ponte una en la boca y trágala. Debes tomar la píldora todos los días a la misma hora, tanto si tienes sexo como si no. Si olvidas tomar la píldora, ésta no será tan efectiva como debería y podrías embarazarte. Si te olvidas de tomar 1 o más píldoras, o empiezas un paquete demasiado tarde, revisa el Folleto de Información para Pacientes que se incluye en el empaque de la píldora. En caso de duda, pregunta a tu profesional médico.

Diferentes píldoras tienen diferentes ciclos, con algunos tipos de píldoras durante los descansos tienes que tomar píldoras sin hormonas para mantener la toma en forma continua. Baja nuestra aplicación de recordatorio de la píldora para que tengas tu rutina bajo control y estés protegida.
        """)

        await message.answer("""
PROS Y CONTRAS ✔|❌

Pros ✔
✔ Altamente efectiva cuando se usa como se indica
✔ Es fácil de usar
✔ Permite la espontaneidad sexual y no interrumpe el sexo
✔ Algunas píldoras pueden mejorar las menstruaciones abundantes y dolorosas
✔ Algunas píldoras pueden tener efecto positivo sobre el acné
✔ Se pueden tomar durante un largo período de tiempo

Contras ❌
❌ Puede hacer que algunas mujeres tengas dolores de cabeza y cambios del estado de ánimo
❌ Se debe estar al pendiente del número de días que se ha tomado
❌ Puede causar molestias mamarias, náusea, dolor de cabeza, aumento de peso
❌ Puede provocar cambios en tu ciclo menstrual
❌ No es frecuente, pero algunas mujeres que toman la píldora desarrollan presión alta
❌ Es raro, pero algunas mujeres pueden tener coágulos sanguíneos, ataques cardiacos y apoplejía
❌ No protege contra la infección por VIH (SIDA) ni contra otras enfermedades de transmisión sexual (ETS)
                """)

# ANILLO HORMONAL
@dp.message_handler(regexp='Anillo Hormonal')
async def welcome(message: types.Message):
        await message.answer_photo(photo=open('./img/anillo.png', 'rb'),
                                   caption='El anillo anticonceptivo se parece mucho a una mezcla entre pulsera y banda elástica, simple y práctico – pero es mucho más listo que eso. Es un anillo claro y flexible de polietileno acetato de vinilo que, una vez colocado en la vagina, libera lentamente en tu cuerpo las hormonas progestina y estrógeno para impedir que los ovarios liberen óvulos. También hace que el moco cervical sea más espeso, lo que no permite que los espermatozoides lleguen al óvulo. Lo mantienes puesto durante 3 semanas y después lo sacas, descansas una semana y después te pones otro.')

        await message.answer("""
CÓMO? 🤷‍♀️

El anillo se asienta en la pared de tu vagina por lo que ponerlo es igual que usar un tampón, debido a su forma podría parecerte un poco complicado, pero a la mayoría de las usuarias les funciona la técnica de apretar y girar. Empieza lavándote las manos, después aprieta el anillo entre tu dedo y el pulgar y empújalo hacia adentro de ti hasta que se asiente sobre uno de los lados de la pared de tu vagina. Una vez que lo coloques, asegúrate de que estás cómoda con su ubicación. No debes sacarlo para tener sexo. Déjalo allí durante 3 semanas y después sácalo, una semana después reemplázalo por uno nuevo. Tu período menstrual iniciará durante esta semana en la que no tienes puesto el anillo. Si el anillo se sale y permanece fuera por más de 3 horas, reemplázalo pero usa otro método anticonceptivo, como el condón, hasta que el anillo haya estado en su sitio por 7 días seguidos. Asegúrate de leer las instrucciones y habla con tu profesional médico sobre lo que debes hacer.
        """)

        await message.answer("""
PROS Y CONTRAS ✔|❌

Pros ✔
✔ Altamente efectivo
✔ Es fácil de colocar y de quitar
✔ No requiere atención diaria
✔ Permite la espontaneidad sexual y no interrumpe el sexo

Contras ❌
❌ Se debe estar al pendiente del número de semanas desde su colocación
❌ Puede producir flujo vaginal, molestias en la vagina e irritación
❌ Puede hacer que algunas personas sufran dolores de cabeza y cambios del estado de ánimo
❌ Puede causar alteraciones menstruales
❌ Puede causar aumento de peso
❌ Otros riesgos son similares a los de los anticonceptivos orales (píldora combinada)
❌ o protege contra la infección por VIH (SIDA) ni contra otras enfermedades de transmisión sexual (ETS)
                """)


# INYECCION ANTICONCEPTIVA
@dp.message_handler(regexp='Inyeccion Anticonceptiva')
async def welcome(message: types.Message):
        await message.answer_photo(photo=open('./img/inyeccion.png', 'rb'),
                                   caption='La inyección anticonceptiva es una inyección que contiene hormonas, ya sea una progestina sola o una progestina y un estrógeno juntos, y hace que tu cuerpo deje de liberar óvulos y que el moco del cérvix sea más espeso. Necesitas que un profesional médico te ponga una inyección una vez al mes, una vez cada dos meses o una vez cada tres meses. Sin embargo, el efecto de la inyección no se puede revertir una vez que se ha aplicado, lo que significa que en caso de tener efectos colaterales, éstos no se pueden detener. La forma cómo actúa es similar a la píldora o al anillo, excepto que no tienes que recordar tomarla diariamente o aplicarlo cada semana, pero probablemente no es la mejor opción para las que le tienen miedo a las agujas.')

        await message.answer("""
CÓMO? 🤷‍♀️

La inyección anticonceptiva se administra cada 1, 2 a 3 meses (cada 4 , cada 8 o cada 12 semanas), según el tipo. El momento de las inyecciones no depende de la menstruación.

Su funcionamiento es similar al de la píldora o el anillo, con la diferencia de que no tienes que acordarte de tomarlo cada día o cada semana.

Como ocurre con la mayoría de los anticonceptivos, no para todos resultan ideales, así que siempre recomendamos asesorarse con un profesional.

Hay diferentes tipos de anticonceptivos inyectables. Algunas inyecciones deben aplicar un profesional de la salud, preferentemente.
        """)

        await message.answer("""
PROS Y CONTRAS ✔|❌

Pros ✔
✔ Altamente efectiva
✔ Dura de 1, 2, o 3 meses dependiendo el tipo
✔ Permite la espontaneidad sexual y no interrumpe el sexo
✔ No requiere atención diaria o semanal
✔ Puede ofrecer una alternativa a aquellas a las que los estrógenos les afectan (solo válido para los Inyecciones que contienen solo progestágenos)
✔ Se puede usar durante la lactancia (solo válido para Inyecciones que contienen solo progestágenos)
✔ Puede disminuir las menstruaciones abundantes y dolorosas en algunas mujeres
✔ Fácil de ocultar

Contras ❌
❌ Se debe estar al pendiente de los meses que se ha usado
❌ Puede hacer que algunas mujeres tengan dolores de cabeza y cambios del estado de ánimo
❌ Puede causar dolor de cabeza, aumento de peso, molestias abdominales
❌ Después de suspender la inyección la menstruación y la fertilidad pueden tardar hasta un año en regresar
❌ Puede producir alteraciones menstruales
❌ Si te aplicas la inyección por más de 2 años seguidos puedes perder densidad ósea (solo válidad si la inyección utilizada contiene solo progestágenos)
❌ No protege contra la infección por VIH (SIDA) ni contra otras enfermedades de transmisión sexual (ETS)
                """)

# CALENDARIO
@dp.message_handler(regexp='Calendario de dias fertiles')
async def welcome(message: types.Message):
        await message.answer_photo(photo=open('./img/calendario.png', 'rb'),
                                   caption='La Conciencia de la Fertilidad es una técnica en la que se calcula exactamente en qué etapa del ciclo menstrual estás, en qué etapas no eres fértil, y se tiene sexo en esos momentos. El Método de Conciencia de la Fertilidad requiere que la mujer observe los signos de fertilidad. Existen varios métodos diferentes, como por ejemplo: ir contando los días de tu ciclo, poner atención a las fluctuaciones de la temperatura corporal y seguir muy de cerca los cambios de tu moco cervical. Existen varias técnicas más, pero todas se pueden ir al traste debido a pequeños cambios en tu ciclo, un error de cálculo, un estilo de vida espontáneo sin horarios regulares de sueño o una multitud de otras variables. Definitivamente no es recomendable para las olvidadizas, las desorganizadas o las espontáneas.')
        await message.answer("""
CÓMO? 🤷‍♀️

Cada técnica es compleja y se basa en el conocimiento íntimo y profundo de tu propio ciclo menstrual. Las técnicas se basan en el hecho de que hay días específicos durante cada ciclo menstrual, los días antes y poco después de la ovulación, en los que te puedes embarazar y otros en los que no, y allí es donde entran en juego el conocimiento íntimo y los cálculos. Si te interesa la conciencia de la fertilidad, se recomienda que uses un método de barrera, p. ej. diafragma, capuchón cervical o condón, o que no tengas sexo los días fértiles. Si te quieres embarazar, la conciencia de la fertilidad te puede ayudar a saber qué días deberías tener sexo para embarazarte.
        """)

        await message.answer("""
PROS Y CONTRAS ✔|❌

Pros ✔
✔ Se puede usar cuando se está amamantando
✔ Sin hormonas
✔ Si te quieres embarazar, te puede ayudar a saber qué días deberías tener sexo

Contras ❌
❌ Su uso puede requerir práctica
❌ Se debe estar al pendiente del ciclo menstrual todo el tiempo
❌ Requiere un estilo de vida muy regular
❌ Está abierto a errores
❌ Puede interferir con la espontaneidad
❌ No es confiable y no toma en cuenta variaciones de tu ciclo
❌ No protege contra la infección por VIH (SIDA) ni contra otras enfermedades de transmisión sexual (ETS)
                """)

# PARCHE ANTICONCEPTIVO
@dp.message_handler(regexp='Parche Anticonceptiva')
async def welcome(message: types.Message):
        await message.answer_photo(photo=open('./img/parche.png', 'rb'),
                                   caption='El parche anticonceptivo es justamente eso, un parche que parece una curita brillante que se pega a la piel, al liberar hormonas resulta altamente efectivo para impedir que te embaraces. El parche libera constantemente las hormonas estrógeno y progestina que entran a la circulación a través de la piel e impiden que los ovarios liberen óvulos y también hacen que el moco cervical sea más espeso, lo que no permite que los espermatozoides lleguen el óvulo. El parche no es transparente, por lo que este método anticonceptivo es visible.')

        await message.answer("""
CÓMO? 🤷‍♀️

Desprende la parte posterior y aplica el parche directamente sobre tu piel en la parte baja del abdomen, las nalgas, la parte superior del brazo o la espalda. Deja el parche en su sitio durante una semana y luego reemplázalo con uno nuevo. Ponte un nuevo parche y quita el anterior una vez por semana durante 3 semanas, 21 días en total. Cada 4ª semana te quedas sin parche. Tu período menstrual empezará durante esta semana sin parche. Después repite nuevamente el mismo proceso. Si el parche se afloja o se desprende, revisa el Folleto de Información para el Paciente que se incluye en el empaque del parche. En caso de duda pregunta a tu médico.
        """)

        await message.answer("""
PROS Y CONTRAS ✔|❌

Pros ✔
✔ Altamente efectivo
✔ Es fácil de poner y de quitar
✔ No requiere atención diaria
✔ Permite la espontaneidad sexual y no interrumpe el sexo
✔ No tienes que recordar tomarlo cada día

Contras ❌
❌ Es visible y puede aflojarse o caerse
❌ Se debe estar al pendiente del número de semanas que se ha usado
❌ Puede causar algo de comezón y enrojecimiento en el sitio de aplicación
❌ Puede hacer que algunas personas sufran dolores de cabeza y cambios del estado de ánimo
❌ Puede causar dolores de cabeza, aumento de peso
❌ Puede causar alteraciones menstruales
❌ Es raro, pero algunas mujeres pueden tener coágulos sanguíneos, ataques cardiacos y apoplejía
❌ No protege contra la infección por VIH (SIDA) ni contra otras enfermedades de transmisión sexual (ETS)
                """)

@dp.message_handler(regexp='DIU')
async def welcome(message: types.Message):
        await message.answer_photo(photo=open('./img/calendario.png', 'rb'),
                                   caption='DIU podría sonar un poco a la era especial pero solo significa Dispositivo Intrauterino, intrauterino significa dentro del útero. Podría parecer extraño pero es un pequeño dispositivo en forma de T altamente efectivo que contiene un hilo o cilindros de cobre que un profesional médico coloca dentro del útero. El DIU libera iones de cobre que inmovilizan a los espermatozoides y les hace difícil moverse dentro de la matriz, pero no impide que los ovarios formen un óvulo cada mes. El DIU, una vez colocado dentro de la matriz, puede permanecer en su sitio hasta por 5 ó 10 años (dependiendo del tipo) o hasta que decidas extraerlo. Nada de era espacial – solo sentido común.')

        await message.answer("""
CÓMO? 🤷‍♀️

Una vez que tu profesional médico, basándose en tus antecedentes médicos, se ha asegurado de que el DIU es un método adecuado para ti y que tú has decidido usarlo, en realidad no hay mucho más que hacer.
Un profesional médico capacitado coloca el DIU a través de la vagina dentro de la matriz de la mujer donde permanece hasta por 5 ó 10 años, dependiendo del tipo. Por supuesto, puedes cambiar de opinión en cualquier momento y tu profesional médico simplemente te lo quitará. Después de que el DIU es extraído, el efecto anticonceptivo desaparece rápidamente y te puedes embarazar tan rápidamente como las mujeres que no han usado anticonceptivos.

El DIU de cobre es altamente efectivo, sin embargo, no es un método adecuado para todas. Es por ello que, para estar segura, es mejor que hables previamente con tu médico para asegurarte de que es adecuado para ti.
        """)

        await message.answer("""
PROS Y CONTRAS ✔|❌

Pros ✔
✔ Puede permanecer en su sitio hasta por 5 ó 10 años (dependiendo del tipo), pero se puede extraer en cualquier momento
✔ Con 99%, es uno de los métodos anticonceptivos más efectivos
✔ Adecuado para mujeres que desean anticoncepción reversible de larga duración hasta por 5 ó 10 años y quieren evitar un régimen de aplicación diaria, semanal o mensual
✔ No interrumpe el sexo
✔ No se afecta por el uso de otros medicamentos
✔ También se puede usar como anticonceptivo de emergencia si se coloca dentro de los cinco días posteriores a haber tenido sexo sin protección
✔ Puede ofrecer una alternativa a aquellas a las que los estrógenos les afectan
✔ Se puede usar cuando se está amamantando
✔ La fertilidad regresa a los niveles previos cuando se extrae el DIU

Contras ❌
❌ Se necesita un profesional médico capacitado para colocarlo y extraerlo
❌ Puede producir cólicos y/o sangrado irregular
❌ Algunas mujeres presentan dolores de cabeza, sensibilidad mamaria y acné después de que se les coloca un DIU
❌ Pequeño riesgo de infección durante la colocación y de expulsión
❌ No protege contra la infección por VIH (SIDA) ni contra otras enfermedades de transmisión sexual (ETS)
                """)
# Volver al menu princial
@dp.message_handler(regexp='Volver al menu principal 🏠')
async def welcome(message: types.Message):
        await message.answer('Hola!, Bienvenida/o a FemiBot, por favor selecciona una opcion del menu',reply_markup=menu_kb)
#--------------------------------------------------------------------------------

@dp.message_handler()
async def welcome(message: types.Message):
    await message.answer('Comando no reconocido 🤷‍♀️')
    time.sleep(1)
    await message.answer('Hola!, Bienvenida/o a FemiBot, por favor selecciona una opcion del menu',
                         reply_markup=menu_kb)


executor.start_polling(dp)