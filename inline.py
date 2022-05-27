from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

#Кнопки
yes1 = InlineKeyboardMarkup(row_width=2).add(InlineKeyboardButton(text='Да',callback_data='yes1'),
                                            InlineKeyboardButton(text='Нет',callback_data='no1'))

begin_filling = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Начать заполнять Анкету',callback_data='now'),
                                            InlineKeyboardButton(text='Заполню позже',callback_data='later'))

yes6 = InlineKeyboardMarkup(row_width=2).add(InlineKeyboardButton(text='Да',callback_data='yes6'),
                                            InlineKeyboardButton(text='Нет',callback_data='no6'))

yes7 = InlineKeyboardMarkup(row_width=2).add(InlineKeyboardButton(text='Да',callback_data='yes7'),
                                            InlineKeyboardButton(text='Нет',callback_data='no7'))

yes8 = InlineKeyboardMarkup(row_width=2).add(InlineKeyboardButton(text='Да',callback_data='yes8'),
                                            InlineKeyboardButton(text='Нет',callback_data='no8'))

yes9 = InlineKeyboardMarkup(row_width=2).add(InlineKeyboardButton(text='Да',callback_data='yes9'),
                                            InlineKeyboardButton(text='Нет',callback_data='no9'))

yes10 = InlineKeyboardMarkup(row_width=2).add(InlineKeyboardButton(text='Да',callback_data='yes10'),
                                            InlineKeyboardButton(text='Нет',callback_data='no10'))

yes11 = InlineKeyboardMarkup(row_width=2).add(InlineKeyboardButton(text='Да',callback_data='yes11'),
                                            InlineKeyboardButton(text='Нет',callback_data='no11'))

yes12 = InlineKeyboardMarkup(row_width=2).add(InlineKeyboardButton(text='Да',callback_data='yes12'),
                                            InlineKeyboardButton(text='Нет',callback_data='no12'))

yes13 = InlineKeyboardMarkup(row_width=2).add(InlineKeyboardButton(text='Да',callback_data='yes13'),
                                            InlineKeyboardButton(text='Нет',callback_data='no13'))

yes14 = InlineKeyboardMarkup(row_width=2).add(InlineKeyboardButton(text='Да',callback_data='yes14'),
                                            InlineKeyboardButton(text='Нет',callback_data='no14'))

yes15 = InlineKeyboardMarkup(row_width=2).add(InlineKeyboardButton(text='Да',callback_data='yes15'),
                                            InlineKeyboardButton(text='Нет',callback_data='no15'))

yes16 = InlineKeyboardMarkup(row_width=2).add(InlineKeyboardButton(text='Да',callback_data='yes16'),
                                            InlineKeyboardButton(text='Нет',callback_data='no16'))

yes17 = InlineKeyboardMarkup(row_width=2).add(InlineKeyboardButton(text='Да',callback_data='yes17'),
                                            InlineKeyboardButton(text='Нет',callback_data='no17'))

yes18 = InlineKeyboardMarkup(row_width=2).add(InlineKeyboardButton(text='Да',callback_data='yes18'),
                                            InlineKeyboardButton(text='Нет',callback_data='no18'))

yes19 = InlineKeyboardMarkup(row_width=2).add(InlineKeyboardButton(text='Да',callback_data='yes19'),
                                            InlineKeyboardButton(text='Нет',callback_data='no19'))

yes20 = InlineKeyboardMarkup(row_width=2).add(InlineKeyboardButton(text='Да',callback_data='yes20'),
                                            InlineKeyboardButton(text='Нет',callback_data='no20'))

redact = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Завершить и отправить анкету',callback_data='ready'),
                                            InlineKeyboardButton(text='Дополнить',callback_data='redaction'))

all_questions = InlineKeyboardMarkup(row_width=2)
nothing = InlineKeyboardButton(text='--> Завершить анкету <--',callback_data='fio')
fio = InlineKeyboardButton(text='Ваше ФИО',callback_data='fio')
day = InlineKeyboardButton(text='Дата рождения',callback_data='day')
place = InlineKeyboardButton(text='Место рождения',callback_data='place')
time = InlineKeyboardButton(text='Время рождения',callback_data='time')
source = InlineKeyboardButton(text='Источник о времени рождения',callback_data='source')
surc = InlineKeyboardButton(text='Обстоятельства рождения',callback_data='surc')
marriage = InlineKeyboardButton(text='Брак',callback_data='marriage')
divorce = InlineKeyboardButton(text='Развод',callback_data='divorce')
children = InlineKeyboardButton(text='Ваши дети',callback_data='children')
reloc = InlineKeyboardButton(text='Переезды',callback_data='reloc')
job = InlineKeyboardButton(text='Работа',callback_data='job')
events = InlineKeyboardButton(text='Важные события',callback_data='events')
death = InlineKeyboardButton(text='Смерти',callback_data='death')
operations = InlineKeyboardButton(text='Операции',callback_data='operations')
property = InlineKeyboardButton(text='Имущество',callback_data='property')
other = InlineKeyboardButton(text='Прочее',callback_data='other')
wishes = InlineKeyboardButton(text='Пожелания к консультации',callback_data='wishes')
contacts = InlineKeyboardButton(text='Ваши контакты',callback_data='contacts')


all_questions.add(nothing).row(fio,day).row(place,time).add(source).add(surc).row(marriage,divorce).row(children,reloc).row(job,events).\
    row(death,operations).row(property,other).row(wishes,contacts)

# thirty = InlineKeyboardMarkup(row_width=1)

# thirty.row(q,w,e,r).row(t,i,o,p).row(a,s,d,f).row(g,h,j,k).row(l,z,x,c).row(v,b,n,m)

# urlbutton = InlineKeyboardButton(text='Нет',url='https://mosgorzdrav.ru/pkb1')
# urlkb.row(yes,no)