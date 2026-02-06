import asyncio
from aiogram import Bot, Dispatcher, types, Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from numpy.ma.core import resize

normal_text = ""
router = Router()
API_TOKEN = '7247367657:AAH1kJCfIwsQZ7cboyWuqRHt9ZdD9sZdGpo'

# Клавиатуры инициализация
kb = [[types.KeyboardButton(text="Начать обучение")]]

kb_start = [[types.KeyboardButton(text="О безопасности в интернете")],
            [types.KeyboardButton(text="О безопасности со звонками")],
            [types.KeyboardButton(text="О безопасности в мессенджерах")],
            [types.KeyboardButton(text="Назад")]]

kb_start_end = [[types.KeyboardButton(text="Кража персональных данных")],
                [types.KeyboardButton(text="Утечки данных")],
                [types.KeyboardButton(text="Вредоносные программы и вирусы")],
                [types.KeyboardButton(text="Фишинговые электронные письма")],
                [types.KeyboardButton(text="Поддельные сайты")],
                [types.KeyboardButton(text="Неприемлемый контент")],
                [types.KeyboardButton(text="Кибербуллинг")],
                [types.KeyboardButton(text="Неверные настройки конфиденциальности")],
                [types.KeyboardButton(text="Назад")]]

kb_end_start = [[types.KeyboardButton(text = "Как избежать проблемы?")],[types.KeyboardButton(text="Назад")]]

kb_end_end = [[types.KeyboardButton(text="Назад")]]

#Кнопки
PO_button = InlineKeyboardButton(text="ПО", callback_data="send_alert")
danns_button = InlineKeyboardButton(text="Персональные данные", callback_data="send_alert")
FISH_button = InlineKeyboardButton(text="Фишинг", callback_data="send_alert")
virus_button = InlineKeyboardButton(text="Вирус", callback_data="send_alert")
account_button = InlineKeyboardButton(text="Аккаунт", callback_data="send_alert")
meneger_pas_button = InlineKeyboardButton(text="Менеджер паролей", callback_data="send_alert")
one_rang_system_button = InlineKeyboardButton(text="Одноранговые сети")
dom_button = InlineKeyboardButton(text="Доменные имена",callback_data="send_alert")
anti_virus_button = InlineKeyboardButton(text="Антивирусные программы", callback_data="send_alert")

#Клавиатуры
PO_and_danns = [[PO_button, danns_button, meneger_pas_button]]
PO_and_one_system = [[PO_button, one_rang_system_button]]
fish_virus_and_account = [[FISH_button, virus_button, account_button]]
dom_and_all = [[dom_button]]
anti_virus_all = [[anti_virus_button]]

# Класс состояний
class Survey(StatesGroup):
    question1 = State()
    question2 = State()
    question3 = State()


class SurveySecurity(StatesGroup):
    question1 = State()
    question3 = State()


# Создание клавиатур
def keyboard1():
    return ReplyKeyboardMarkup(resize_keyboard=True, keyboard=kb)


def keyboard2():
    return ReplyKeyboardMarkup(resize_keyboard=True, keyboard=kb_start)


def keyboard3():
    return ReplyKeyboardMarkup(resize_keyboard=True, keyboard=kb_start_end)


def keyboard4():
    return ReplyKeyboardMarkup(resize_keyboard=True, keyboard=kb_end_end)

def PO_and_danns_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=PO_and_danns, row_width=2)

def fish_virus_and_account_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=fish_virus_and_account, row_width=3)

def anti_virus_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=anti_virus_all,row_width=1)

def dom_and_all_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=dom_and_all, row_width=1)

def PO_and_sety_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=PO_and_one_system, row_width=2)

def keyboard5():
    return ReplyKeyboardMarkup(resize_keyboard=True, keyboard=kb_end_start)


# await message.answer("[Привет](www.google.com) всё работает", reply_markup=keyboard4(),parse_mode='MarkdownV2')
# Инициализация бота и диспетчера
async def main():
    bot = Bot(token=API_TOKEN)
    dp = Dispatcher(storage=MemoryStorage())

    # Команда start
    @dp.message(Command("start"))
    async def send_first_question(message: types.Message, state: FSMContext):
        await state.set_state(Survey.question1)
        await message.answer("Привет! Я бот по обучению КиберБезопасности. Начнём обучение?",
                             reply_markup=keyboard1())

    # Команда help
    @dp.message(Command("help"))
    async def send_help(message: types.Message):
        help_text = (
            "Вот список команд:\n"
            "/start - начать работу с ботом\n"
            "/help - получить помощь\n"
            "/info - узнать информацию о боте"
        )
        await message.answer(help_text)

    # Обработчик команды /info
    @dp.message(Command('info'))
    async def send_info(message: types.Message):
        await message.answer("Я простой бот, написанный на aiogram.")

    @dp.message(SurveySecurity.question1)
    # Тут 2 возвратные с других кнопок

    async def smarthone_hung(message: types.Message, state: FSMContext):
        global normal_text
        if normal_text == "Кража персональных данных":
            if message.text == "Назад":
                await state.set_state(SurveySecurity.question3)
                await message.answer("О чём бы ты хотел узнать получше?", reply_markup=keyboard3())
            else:
                await message.answer("Чтобы предотвратить кражу данных злоумышленниками, можно предпринять следующие действия:\n"
                                    "\n1. Используйте надежные пароли\n Надежный пароль состоит не менее чем из 12 символов: заглавных и строчных букв, специальных символов и цифр."
                                    "\n2.	Не записывайте пароли\n Если нужно запоминать слишком много данных, используйте менеджер паролей."
                                    "\n3.	Удалите неиспользуемые учетные записи\n Чтобы сохранить конфиденциальность, удаляйте личные данные из неиспользуемых сервисов.",reply_markup=keyboard4())

                await message.answer("Выбери слово которое тебе было непонятно", reply_markup=PO_and_danns_keyboard())
                if message.text == "Назад":
                    await state.set_state(SurveySecurity.question3)
                    await message.answer("О чём бы ты хотел узнать получше?", reply_markup=keyboard3())

        elif normal_text == "Утечки данных":
            if message.text == "Назад":
                await state.set_state(SurveySecurity.question3)
                await message.answer("О чём бы ты хотел узнать получше?", reply_markup=keyboard3())
            else:
                await message.answer("1.	Не заходите на незащищенные веб-сайты"
                                     "\n2.	Покупая товары в интернете, оформляя подписку на очередной цифровой сервис или регистрируясь на новом веб-сайте, "
                                     "не используйте старый пароль и не делитесь без необходимости личными сведениями.",reply_markup=keyboard4())

                if message.text == "Назад":
                    await state.set_state(SurveySecurity.question3)
                    await message.answer("О чём бы ты хотел узнать получше?", reply_markup=keyboard3())

        elif normal_text == "Вредоносные программы и вирусы":
            if message.text == "Назад":
                await state.set_state(SurveySecurity.question3)
                await message.answer("О чём бы ты хотел узнать получше?", reply_markup=keyboard3())
            else:
                await message.answer("1.	Установите на вашем компьютере надежное защитное ПО."
                                     "\n2.	Избегайте действий, которые могут поставить под угрозу ваш компьютер. "
                                     "\n К ним относятся открытие незапрошенных вложений в электронной почте, посещение неизвестных веб-страниц, скачивание программ с "
                                     "недоверенных сайтов или одноранговых сетей передачи файлов.",reply_markup=keyboard4())

                await message.answer("Выбери слово которое тебе было непонятно", reply_markup=PO_and_danns_keyboard())
                if message.text == "Назад":
                    await state.set_state(SurveySecurity.question3)
                    await message.answer("О чём бы ты хотел узнать получше?", reply_markup=keyboard3())

        elif normal_text == "Фишинговые электронные письма":
            if message.text == "Назад":
                await state.set_state(SurveySecurity.question3)
                await message.answer("О чём бы ты хотел узнать получше?", reply_markup=keyboard3())
            else:
                await message.answer("1.	Не раскрывайте свои учетные данные третьим лицам, даже если они представляются сотрудниками известных организаций."
                                     "\n 2.	Не переходите по ссылкам в письме от неизвестного вам отправителя."
                                     "\n 3.	Избегайте спешки и панической реакции. "
                                     "\n Мошенники рассчитывают на них, чтобы заставить вас перейти по ссылке или открыть вложение.",reply_markup=keyboard4())

                # await message.answer("Выбери слово которое тебе было непонятно", reply_markup=inline_keyboard1())
                if message.text == "Назад":
                    await state.set_state(SurveySecurity.question3)
                    await message.answer("О чём бы ты хотел узнать получше?", reply_markup=keyboard3())

        elif normal_text == "Поддельные сайты":
            if message.text == "Назад":
                await state.set_state(SurveySecurity.question3)
                await message.answer("О чём бы ты хотел узнать получше?", reply_markup=keyboard3())
            else:
                await message.answer("1.	Проверяйте доменные имена"
                                     "\n Доменные имена поддельных сайтов, маскирующихся под легитимные, по написанию или по звучанию бывают очень похожи на настоящие."
                                     "\n 2.	Не верьте уловкам мошенников, предлагающих слишком низкие цены или внезапное богатство"
                                     "\n Спросите себя: а не слишком ли это хорошо, чтобы быть правдой?",reply_markup=keyboard4())

                await message.answer("Выбери слово которое тебе было непонятно", reply_markup=dom_and_all_keyboard())
                if message.text == "Назад":
                    await state.set_state(SurveySecurity.question3)
                    await message.answer("О чём бы ты хотел узнать получше?", reply_markup=keyboard3())

        elif normal_text == "Неприемлемый контент":
            if message.text == "Назад":
                await state.set_state(SurveySecurity.question3)
                await message.answer("О чём бы ты хотел узнать получше?", reply_markup=keyboard3())
            else:
                await message.answer("1.	Периодически меняйте пароли"
                                     "\n 2.	Используйте антивирусные программы"
                                     "\n 3.	Будьте внимательны в социальных сетях"
                                     "\n Действия детей и подростков в социальных сетях требуют особой осторожности и внимания.",reply_markup=keyboard4())

                await message.answer("Выбери слово которое тебе было непонятно", reply_markup=anti_virus_keyboard())
                if message.text == "Назад":
                    await state.set_state(SurveySecurity.question3)
                    await message.answer("О чём бы ты хотел узнать получше?", reply_markup=keyboard3())

        elif normal_text == "Кибербуллинг":
            if message.text == "Назад":
                await state.set_state(SurveySecurity.question3)
                await message.answer("О чём бы ты хотел узнать получше?", reply_markup=keyboard3())
            else:
                await message.answer("1.	Прервите общение, если оно стало неприятным для вас."
                                     "\n Лучше всего не отвечать на провокации и уходить от контакта с агрессором. Если вы ребенок, сразу же сообщите о ситуации взрослым."
                                     "\n 2.	Сами не становитесь агрессором"
                                     "\n Относитесь бережно к чувствам других людей и уважайте их право на свое мнение.",reply_markup=keyboard4())

                # await message.answer("Выбери слово которое тебе было непонятно", reply_markup=inline_keyboard1())
                if message.text == "Назад":
                    await state.set_state(SurveySecurity.question3)
                    await message.answer("О чём бы ты хотел узнать получше?", reply_markup=keyboard3())

        elif normal_text == "О безопасности со звонками":
            if message.text == "Назад":
                await state.set_state(Survey.question2)
                await message.answer("О чём бы ты хотел узнать поподробнее?", reply_markup=keyboard2())
            else:
                await message.answer("1. Сохранять бдительность при любых звонках и сообщениях, даже от знакомых: если есть сомнение, лучше перепроверить и уточнить по другому каналу связи; "
                                     "\n2. Никому не сообщать данные из СМС и push-уведомлений; "
                                     "\n3. Подключить специальные защитные функции, которые предлагает ваш мобильный оператор.",reply_markup=keyboard4())

                # await message.answer("Выбери слово которое тебе было непонятно", reply_markup=inline_keyboard1())
                if message.text == "Назад":
                    await state.set_state(Survey.question2)
                    await message.answer("О чём бы ты хотел узнать поподробнее?", reply_markup=keyboard2())

        elif normal_text == "О безопасности в мессенджерах":
            if message.text == "Назад":
                await state.set_state(Survey.question2)
                await message.answer("О чём бы ты хотел узнать поподробнее?", reply_markup=keyboard2())
            else:
                await message.answer("Привет", reply_markup=keyboard4())
                if message.text == "Назад":
                    await state.set_state(Survey.question2)
                    await message.answer("О чём бы ты хотел узнать поподробнее?", reply_markup=keyboard2())


        elif normal_text == "Неверные настройки конфиденциальности":
            if message.text == "Назад":
                await state.set_state(SurveySecurity.question3)
                await message.answer("О чём бы ты хотел узнать получше?", reply_markup=keyboard3())
            else:
                await message.answer("1.	Проверьте настройки приватности и ознакомьтесь с политиками конфиденциальности."
                                     "\n Ознакомьтесь с политиками конфиденциальности используемых веб-сайтов и приложений и поймите, как осуществляется сбор и анализ данных"
                                     "\n 2.	Убедитесь, что ваши устройства защищены."
                                     "\n Используйте пароли, секретные коды и другие средства безопасности, такие как считывание отпечатков пальцев или технологию распознавания лица.",reply_markup=keyboard4())

                # await message.answer("Выбери слово которое тебе было непонятно", reply_markup=())
                if message.text == "Назад":
                    await state.set_state(SurveySecurity.question3)
                    await message.answer("О чём бы ты хотел узнать получше?", reply_markup=keyboard3())

        else:
            if normal_text != "О безопасности со звонками" and normal_text != "О безопасности в мессенджерах":
                await state.set_state(SurveySecurity.question3)
                await message.answer("О чём бы ты хотел узнать получше?", reply_markup=keyboard3())
                return
            else:
                await state.set_state(Survey.question2)
                await message.answer("О чём бы ты хотел узнать поподробнее?", reply_markup=keyboard2())
                return

    @dp.callback_query(F.data == "send_alert")
    async def process_callback(callback: types.CallbackQuery):
        # Или отправить новое сообщение в чат
        await callback.message.answer("Вы нажали на кнопку и вызвали это сообщение.")


    @dp.message(SurveySecurity.question3)
    async def continue_survey(message: types.Message, state: FSMContext):
        global normal_text
        if message.text == "Кража персональных данных":
            normal_text = "Кража персональных данных"
            await state.set_state(SurveySecurity.question1)
            await message.answer(
                "Кража данных – это кража цифровой информации, хранящейся на компьютерах, серверах и электронных устройствах, с целью получения не подлежащих разглашению данных или нарушения конфиденциальности. \n Украденные данные могут включать информацию"
                " о банковском счете, пароли от онлайн-сервисов, номера паспортов и прочее. \n Получив доступ к личной или финансовой информации, неавторизованные пользователи могут удалять и изменять ее без разрешения владельца, "
                "или даже запретить к ней доступ.",
                reply_markup=keyboard5())

            # await message.answer("Выбери слово которое тебе было непонятно", reply_markup=)

        elif message.text == "Утечки данных":
            normal_text = "Утечки данных"
            await state.set_state(SurveySecurity.question1)
            await message.answer(
                "Утечка персональных данных происходит, когда компания подверглась атаке, что привело к потере, изменению или несанкционированному раскрытию персональных данных пользователей."
                "\n Личная информация и учетные данные множества людей могут быть использованы для хищения их личных документов и паролей, проведения незаконных финансовых операций и кражи цифровой личности целиком.",
                reply_markup=keyboard5())

            # await message.answer("Выбери слово которое тебе было непонятно", reply_markup=)

        elif message.text == "Вредоносные программы и вирусы":
            normal_text = "Вредоносные программы и вирусы"
            await state.set_state(SurveySecurity.question1)
            await message.answer(
                "Под вредоносной программой подразумевается любая программа, созданная для выполнения любого несанкционированного — и, как правило, вредоносного — действия на устройстве пользователя (например, вирусы)."
                , reply_markup=keyboard5())

            # await message.answer("Выбери слово которое тебе было непонятно", reply_markup=)

        elif message.text == "Фишинговые электронные письма":
            normal_text = "Фишинговые электронные письма"
            await state.set_state(SurveySecurity.question1)
            await message.answer('Фишинг – это такой вид мошенничества, когда злоумышленник вынуждает вас совершить действие, позволяющее ему получить доступ к вашему устройству, учетным записям '
                                 'или персональным данным. Выдавая себя за человека или говоря от имени организации, которым вы доверяете, мошенник легко может заразить ваше устройство вредоносным ПО или '
                                 'украсть реквизиты вашей банковской карты.'
                                 , reply_markup=keyboard5())

            # await message.answer("Выбери слово которое тебе было непонятно", reply_markup=)

        elif message.text == "Поддельные сайты":
            normal_text = "Поддельные сайты"
            await state.set_state(SurveySecurity.question1)
            await message.answer(
                "Поддельные сайты – это любые сайты, которые мошенники используют незаконно для обмана пользователей или организации вредоносных атак."
                , reply_markup=keyboard5())

            # await message.answer("Выбери слово которое тебе было непонятно", reply_markup=)

        elif message.text == "Неприемлемый контент":
            normal_text = "Неприемлемый контент"
            await state.set_state(SurveySecurity.question1)
            await message.answer("Неприемлемый контент может принимать различные формы: от неточной информации до контента, который может привести вашего ребенка к противоправному поведению"
                                 , reply_markup=keyboard5())

            # await message.answer("Выбери слово которое тебе было непонятно", reply_markup=)

        elif message.text == "Кибербуллинг":
            normal_text = "Кибербуллинг"
            await state.set_state(SurveySecurity.question1)
            await message.answer("Кибербуллинг (он же интернет-травля) – это травля человека или группы людей с использованием технических средств по электронной почте, в мессенджерах, социальных сетях."
                                 , reply_markup=keyboard5())

            # await message.answer("Выбери слово которое тебе было непонятно", reply_markup=)

        elif message.text == "Неверные настройки конфиденциальности":
            normal_text = "Неверные настройки конфиденциальности"
            await state.set_state(SurveySecurity.question1)
            await  message.answer(
                "Конфиденциальность данных — это один из ключевых аспектов кибербезопасности, который направлен на защиту личной и корпоративной информации от несанкционированного доступа"
                , reply_markup=keyboard5())

            # await message.answer("Выбери слово которое тебе было непонятно", reply_markup=)

        elif message.text == "Назад":
            await state.set_state(Survey.question2)
            await message.answer("О чём бы ты хотел узнать поподробнее?", reply_markup=keyboard2())
            return

    # Вопрос после команды Start
    @dp.message(Survey.question1)
    async def send_second_question(message: types.Message, state: FSMContext):
        await state.update_data(answer1=message.text)
        await state.set_state(Survey.question2)
        await message.answer("О чём бы ты хотел узнать поподробнее?", reply_markup=keyboard2())

    # Вопрос после send_second_question
    @dp.message(Survey.question2)
    async def finish_survey(message: types.Message, state: FSMContext):
        # Проверяем нажал ли пользователь кнопку О безопасности в интернете и меняем клавиатуру
        global normal_text
        if message.text == "О безопасности в интернете":
            await state.set_state(SurveySecurity.question3)
            await message.answer("О чём бы ты хотел узнать получше?", reply_markup=keyboard3())

        # Одна из трех кнопок в начале

        elif message.text == "О безопасности со звонками":
            normal_text = "О безопасности со звонками"
            await state.set_state(SurveySecurity.question1)
            await message.answer(
                "В настоящее время телефон является основным каналом поступления сообщений, содержащих информацию о заложенных взрывных устройствах, о захвате людей в заложники, вымогательстве и шантаже."
                "\nКак правило, фактор внезапности, возникающее паническое, а порой и шоковое состояние, да и сама полученная информация приводит к тому, что человек оказывается не в состоянии правильно "
                "отреагировать на звонок, оценить реальность угрозы и получить максимум сведений из разговора."
                "\nЗвонки с угрозами могут поступать лично вам или содержать, например, требования выплатить значительную сумму денег.",
                reply_markup=keyboard5())

            # await message.answer("Выбери слово которое тебе было непонятно", reply_markup=)

        # Одна из трех кнопок в начале

        elif message.text == "О безопасности в мессенджерах":
            normal_text = "О безопасности в мессенджерах"
            await state.set_state(SurveySecurity.question1)
            await message.answer(
                "Мессенджеры — это одно из самых удобных, а потому популярных средств обмена сообщениями. "
                "\nКибер-преступники эксплуатируют уязвимости мессенджеров, чтобы получить доступ к сообщениям, рассылают фишинговые ссылки, чтобы заразить ваше "
                "устройство вирусом и заполучить ваши персональные данные, взламывают аккаунты пользователей и рассылают им просьбы о перечислении денег.", reply_markup=keyboard5())

            await message.answer("***Нажми на слово, если не знаешь его значение", reply_markup=fish_virus_and_account_keyboard())

        elif message.text == "Назад":
            await state.set_state(Survey.question1)
            await message.answer("Привет! Я бот по обучению КиберБезопасности. Начнём обучение?",
                                 reply_markup=keyboard1())
            return

    await dp.start_polling(bot, skip_updates=True)
    await bot.delete_webhook(drop_pending_updates=True)


# Запуск основного события
if __name__ == '__main__':
    asyncio.run(main())
