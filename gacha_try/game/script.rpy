﻿# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define a = Character('Таинственный голос в вашей голове', color="#cb1a55")
define you = Character('ты', color="#e9cdd6")

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:

    scene black

    a "*торжественно* Сегодня… сегодня началась эпоха перемен. День, когда был сделан выбор, изменивший судьбу человече—"
    you "Что? Кто это сказал?"
    "вы стоите в растянутой футболке с логотипом \"Пельмени Фьюри\" медленно поворачивая голову влево, потом вправо. Никого."
    "и в течение следующей пары секунд стоит тишина и вы успокаиваиваетесь"
    "никаких белых комнат и смирительных рубашек в ближайшее время не ожидается"
    a "*в замешательстве* Э, ты меня слышишь? Но как..... Чёрт. Ладно. Неважно. Просто... ДЕЙСТВУЙ ПО СЦЕНАРИЮ!"
    "ох, все же мягкие белые стены ждут вас"
    you "Сценарию? Что за бред вообще?"
    a "КХМ. *пытается вернуть пафос* Ты — Избранный. Тот, кому выпало великое испытание. Повелитель судьбы. Обладатель Билета Героя!"
    you "Это… вот этот желтый стикер из пачки чипсов?"
    you "Вы вытянули из пачки чипсов помятую бумажку с надписью \"Поздравляем! Вы выиграли путешествие мечты!\".\nНо чем больше вы на нее смотрите, тем больше убеждаетесь в том, что вам нужно обратиться к психиатру"
    a "*вздыхает, шепчет себе* Почему всегда попадаются такие…\nЛадно. Импровизируем."
    a "Никуда тебя не заберут, все по-настоящему."
    a "И ЭТО не просто кусок бумаги! Это артефакт, что позволяет вызвать Героя из иного мира, в битву против Древнего Зла!"
    you "Вам явно не нравится, что ваши мысли так нагло читают и вы уже думаете что бы такого отвратительного представить..."
    a "на нас люди смотрят"
    "вы передумали"
    you "Ну, а если я не хочу следовать на поводу своей шизы?"
    a "НЕ ВАЖНО, ХОЧЕШЬ ЛИ ТЫ! Все уже оплачено. Бюджет ограничен. Декорации арендованы. Мы начали."
    you "Ты еще скажи что ты режиссер"
    a "*гордо* Да! Режиссёр… судьбы! *в сторону* Блин, где дымовая машина?.."
    "что-то подсказывает вам, что вы совсем с ума сходить начали, переиграв в китайские гачи... Но может если просто плыть по течению, то сон быстро закончится?"
    you "Ну ладно… Ща."
    a "*взволнованно, даже слишком взволнованно* ДА! Прочти слова призыва: \"Изыди из времени, герой отчаянья, ведомый судьбой!\""
    you "Ээ… Изыди из времени… герой чаяния…"
    a "ОТЧАЯНЬЯ! НЕ ЧАЯНЬЯ!"
    a "…Господи, дайте мне нормального актёра… хоть раз."

    jump gacha_screen

label gacha_screen:
    call screen gacha_screen
    "Ты вернулся из гачи."    

    return