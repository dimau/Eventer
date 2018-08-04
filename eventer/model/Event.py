import sqlalchemy
from Base_class_sql_alchemy import Base
from sqlalchemy.orm import relationship
from FormattingDataRepresentation import FormattingDataRepresentation


class Event(Base, FormattingDataRepresentation):
    __tablename__ = 'events'

    _id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    _title = sqlalchemy.Column(sqlalchemy.String(150))
    _description = sqlalchemy.Column(sqlalchemy.String(1000))
    _id_kudago = sqlalchemy.Column(sqlalchemy.String(50))
    _categories_kudago = sqlalchemy.Column(sqlalchemy.String(1000))  # временно сохраняю в базу для отладки
    _tags_kudago = sqlalchemy.Column(sqlalchemy.String(50))  # временно сохраняю в базу для отладки
    _price_kudago = sqlalchemy.Column(sqlalchemy.String(50))  # временно сохраняю в базу для отладки
    _url = sqlalchemy.Column(sqlalchemy.String(500))
    _categories = sqlalchemy.Column(sqlalchemy.String(
        1000))  # список категорий через черту | в виде строки текста, к которым относится мероприятие - внутрипроектное представление
    _image = sqlalchemy.Column(sqlalchemy.String(200))
    _start_time = sqlalchemy.Column(sqlalchemy.Integer)
    _finish_time = sqlalchemy.Column(sqlalchemy.Integer)
    _duplicate_source_id = sqlalchemy.Column(sqlalchemy.String(50))
    _duplicate_id = sqlalchemy.Column(sqlalchemy.Integer)
    _price_min = sqlalchemy.Column(sqlalchemy.Integer)
    _price_max = sqlalchemy.Column(sqlalchemy.Integer)

    ratings = relationship("Rating", back_populates="event")

    def __init__(self, source_dict):
        self._title = source_dict.get('title', '')
        self._description = source_dict.get('description', '')
        self._id_kudago = source_dict.get('id_kudago', '')
        self._categories_kudago = source_dict.get('categories_kudago', '')
        self._tags_kudago = self.convert_from_iterator_to_string(source_dict.get('tags_kudago', ''))
        self._price_kudago = source_dict.get('price_kudago', '')
        self._url = source_dict.get('url', '')
        self._categories = self.convert_from_iterator_to_string(source_dict.get('categories', set()))
        self._image = source_dict.get('image', '')
        self._start_time = source_dict.get('start_time', 0)
        self._finish_time = source_dict.get('finish_time', 0)
        self._duplicate_source_id = source_dict.get('duplicate_source_id', '')
        self._duplicate_id = source_dict.get('duplicate_id', 0)
        self._price_min = source_dict.get('price_min', None)
        self._price_max = source_dict.get('price_max', None)

    def __repr__(self):
        return '<Event title: {}, ' \
               'description: {}, ' \
               'id_kudago: {}, ' \
               'categories_kudago: {}, ' \
               'tags_kudago: {}, ' \
               'price_kudago: {}, ' \
               'url: {}, ' \
               'categories: {},' \
               'image: {},' \
               'start_time: {},' \
               'finish_time: {},' \
               'duplicate_source_id: {},' \
               'duplicate_id: {},' \
               'price_min: {},' \
               'price_max: {}>'.format(self._title,
                                       self._description,
                                       self._id_kudago,
                                       self._categories_kudago,
                                       self._tags_kudago,
                                       self._price_kudago,
                                       self._url,
                                       self._categories,
                                       self._image,
                                       self._start_time,
                                       self._finish_time,
                                       self._duplicate_source_id,
                                       self._duplicate_id,
                                       self._price_min,
                                       self._price_max)

    @property
    def event_id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @property
    def id_kudago(self):
        return self._id_kudago

    @property
    def categories(self):
        # TODO: refactor automatically convert from string to set and delete function convert_from_set_to_string
        return self._categories

    @property
    def url(self):
        return self._url

    @property
    def image(self):
        return self._image

    @property
    def start_time(self):
        return self._start_time

    @property
    def duplicate_source_id(self):
        return self._duplicate_source_id

    @property
    def duplicate_id(self):
        return self._duplicate_id

    @duplicate_id.setter
    def duplicate_id(self, value):
        self._duplicate_id = int(value)

    @property
    def price_min(self):
        return self._price_min

    @property
    def price_max(self):
        return self._price_max


"""
Все категории событий
{"id":1,"slug":"concert","name":"Концерты"}
{"id":2,"slug":"theater","name":"Театр (спектакли, опера, балет итд)"}
{"id":3,"slug":"education","name":"Знания"}
{"id":4,"slug":"party","name":"Вечеринки"}
{"id":5,"slug":"sport","name":"Спорт (Раздел Отдых)"}
{"id":6,"slug":"exhibition","name":"Выставки"}
{"id":7,"slug":"tour","name":"Экскурсии"}
{"id":8,"slug":"festival","name":"Фестивали (Фестивали)"}
{"id":9,"slug":"cinema","name":"Кино (Развлечения)"}
{"id":10,"slug":"fashion","name":"Мода"}
{"id":11,"slug":"show","name":"Шоу (Развлечения)"}
{"id":12,"slug":"holiday","name":"Праздники"}
{"id":13,"slug":"social-activity","name":"Благотворительность"}
{"id":14,"slug":"yarmarki-razvlecheniya-yarmarki","name":"Ярмарки (Развлечения, Ярмарки)"}
{"id":15,"slug":"games","name":"Игры (Развлечения)"}
{"id":16,"slug":"night","name":"Ночь"}
{"id":17,"slug":"meeting","name":"Встречи"}
{"id":18,"slug":"speed-dating","name":"Быстрые свидания (Развлечения)"}
{"id":19,"slug":"flashmob","name":"Флешмобы (Развлечения)"}
{"id":20,"slug":"masquerade","name":"Маскарады (Развлечения)"}
{"id":21,"slug":"romance","name":"Романтика (Развлечения)"}
{"id":22,"slug":"dance-trainings","name":"Занятия танцами (Раздел Отдых)"}
{"id":23,"slug":"evening","name":"Творческие вечера"}
{"id":24,"slug":"discount","name":"Скидки"}
{"id":25,"slug":"stock","name":"Акции"}
{"id":26,"slug":"sale","name":"Распродажа (Магазины)"}
{"id":27,"slug":"shopping","name":"Шопинг (Магазины)"}
{"id":28,"slug":"quest","name":"Квесты"}
{"id":29,"slug":"ball","name":"Балы (Развлечения)"}
{"id":30,"slug":"yoga","name":"Йога"}
{"id":31,"slug":"presentation","name":"Презентации"}
{"id":32,"slug":"magic","name":"Фокусники, иллюзионисты (Развлечения)"}
{"id":33,"slug":"kvn","name":"КВН (Развлечения)"}
{"id":34,"slug":"comedy-club","name":"Comedy club / Камеди клаб (Развлечения)"}
{"id":35,"slug":"stand-up","name":"Стендап (Развлечения)"}
{"id":36,"slug":"kids","name":"Детские (раздел детям)"}
{"id":37,"slug":"circus","name":"Цирковые представления (Развлечения)"}
{"id":38,"slug":"open","name":"Дни открытых дверей"}
{"id":39,"slug":"other","name":"Разное"}
{"id":40,"slug":"photo","name":"Фотособытия"}
{"id":42,"slug":"global","name":"В мире"}
{"id":44,"slug":"permanent-exhibitions","name":"Постоянные выставки"}
{"id":45,"slug":"business-events","name":"События для бизнеса"}
"""

"""
Категории мест
{"id":15,"slug":"restaurants","name":"Рестораны (Рестораны)"}
{"id":16,"slug":"cafe","name":"Кафе (Рестораны)"}
{"id":17,"slug":"anticafe","name":"Антикафе"}
{"id":18,"slug":"coffee","name":"Кофейни (Рестораны)"}
{"id":19,"slug":"bar","name":"Бары"}
{"id":20,"slug":"vegetarian","name":"Вегетарианские кафе и рестораны (Рестораны)"}
{"id":22,"slug":"fastfood","name":"Фастфуды и закусочные (Рестораны)"}
{"id":23,"slug":"canteens","name":"Столовые (Рестораны)"}
{"id":24,"slug":"banquets","name":"Банкетные залы (Рестораны)"}
{"id":25,"slug":"bakeries","name":"Кондитерские (Рестораны)"}
{"id":26,"slug":"clubs","name":"Клубы"}
{"id":27,"slug":"karaoke","name":"Караоке"}
{"id":28,"slug":"concert-hall","name":"Концертные залы"}
{"id":29,"slug":"clothing","name":"Магазины одежды (Магазины)"}
{"id":30,"slug":"gifts","name":"Магазины подарков (Магазины)"}
{"id":31,"slug":"toys","name":"Магазины игрушек (Магазины)"}
{"id":32,"slug":"health-food","name":"Магазины здорового питания (Магазыины)"}
{"id":33,"slug":"flea-market","name":"Барахолки, блошиные рынки (Магазины)"}
{"id":34,"slug":"second-hand","name":"Секонд хенды (Магазины)"}
{"id":35,"slug":"tea","name":"Чайные магазины, чай (Магазины)"},{"id":36,"slug":"perfume-stores","name":"Магазины парфюмерии (Магазины)"},{"id":37,"slug":"show-room","name":"Шоу-румы (Магазины)"},{"id":38,"slug":"online-shopping","name":"Интернет-магазины (Магазины)"},{"id":39,"slug":"books","name":"Книжные магазины (Магазины)"},{"id":40,"slug":"music-stores","name":"Музыкальные магазины (Магазины)"},{"id":41,"slug":"shopping-mall","name":"Торговые центры (Магазины)"},{"id":42,"slug":"museums","name":"Музеи (раздел Музеи, Выставки)"},{"id":43,"slug":"exhibition","name":"Выставочные центры"},{"id":44,"slug":"gallery","name":"Галереи (раздел Музеи, Выставки)"},{"id":45,"slug":"culture","name":"Дома культуры"},{"id":46,"slug":"observatory","name":"Обсерватории"},{"id":47,"slug":"circus","name":"Цирки (Развлечения)"},{"id":48,"slug":"theatre","name":"Театры"},{"id":49,"slug":"cinema","name":"Кинотеатры"},{"id":50,"slug":"library","name":"Библиотеки"},{"id":51,"slug":"attractions","name":"Достопримечательности (интересные места)"},{"id":52,"slug":"monument","name":"Памятники (интересные места)"},{"id":53,"slug":"interesting-places","name":"Интересные места(Интересные места)"},{"id":54,"slug":"streets","name":"Улицы"},{"id":55,"slug":"yard","name":"Дворы (интересные места)"},{"id":56,"slug":"houses","name":"Необычные дома (интересные места)"},{"id":57,"slug":"fountain","name":"Фонтаны"},{"id":58,"slug":"bridge","name":"Мосты"},{"id":59,"slug":"park","name":"Парки (Интересные места, Отдых)"},{"id":60,"slug":"pocket-parks","name":"Скверы (Отдых)"},{"id":61,"slug":"cathedrals","name":"Соборы (интересные места)"},{"id":62,"slug":"temple","name":"Храмы"},{"id":63,"slug":"church","name":"Церкви"},{"id":64,"slug":"mosque","name":"Мечети (интересные места)"},{"id":65,"slug":"synagogue","name":"Синагоги"},{"id":66,"slug":"monastery","name":"Монастыри"},{"id":67,"slug":"palace","name":"Дворцы"},{"id":68,"slug":"castle","name":"Замки (интересные места)"},{"id":69,"slug":"homesteads","name":"Усадьбы"},{"id":70,"slug":"suburb","name":"Пригороды (Загородный отдых)"},{"id":71,"slug":"education-centers","name":"Учебные заведения (Учебн завед)"},{"id":72,"slug":"course","name":"Обучающие курсы (Учебн завед)"},{"id":73,"slug":"academy-of-music","name":"Музыкальные школы (Учебн завед)"},{"id":74,"slug":"painting","name":"Школы рисования (Учебн завед)"},{"id":75,"slug":"fitness","name":"Фитнес-центры (Отдых, Красота и здоровье)"},{"id":76,"slug":"sport","name":"Спортивные сооружения (Отдых)"},{"id":77,"slug":"ice-rink","name":"Катки"},{"id":78,"slug":"water-park","name":"Аквапарки (Отдых)"},{"id":79,"slug":"slope","name":"Горнолыжные склоны (Отдых)"},{"id":80,"slug":"diving","name":"Дайвинг-центры (Отдых)"},{"id":81,"slug":"karts","name":"Картинги (Отдых)"},{"id":82,"slug":"climbing-walls","name":"Скалодромы (Отдых)"},{"id":83,"slug":"bowling","name":"Боулинг (Развлечения)"},{"id":84,"slug":"billiards","name":"Бильярд (Развлечения)"},{"id":85,"slug":"rollerdromes","name":"Роллердромы (Отдых)"},{"id":86,"slug":"shooting-ranges","name":"Тиры и стрелковые клубы (Отдых)"},{"id":87,"slug":"wind-tunnels","name":"Аэротруба (Отдых)"},{"id":88,"slug":"paintball","name":"Пейнтбол (Отдых)"},{"id":89,"slug":"amusement","name":"Парки аттракционов (Развлечения)"},{"id":90,"slug":"salons","name":"Салоны красоты (Красота и здоровье)"},{"id":91,"slug":"photo-places","name":"Фотоместа (Фотография)"},{"id":92,"slug":"metro","name":"Метро"},{"id":93,"slug":"station","name":"Вокзалы"},{"id":94,"slug":"car-washes","name":"Автомойки"},{"id":95,"slug":"stable","name":"Конюшни, конные клубы"},{"id":96,"slug":"zoo","name":"Зоопарки (Развлечения)"},{"id":97,"slug":"cats","name":"Кошачий питомник"},{"id":98,"slug":"dogs","name":"Собачий питомник"},{"id":99,"slug":"pet-store","name":"Зоомагазины"},{"id":100,"slug":"beaches","name":"Пляжи (Отдых)"},{"id":101,"slug":"coworking","name":"Коворкинги"},{"id":102,"slug":"kids","name":"Детские места (раздел детям)"},{"id":103,"slug":"swimming-pool","name":"Бассейн (Отдых)"},{"id":104,"slug":"hostels","name":"Хостелы"},{"id":105,"slug":"inn","name":"Гостиницы (Отели)"},{"id":106,"slug":"hotels","name":"Отели (Отели)"},{"id":107,"slug":"roof","name":"Рестораны и кафе на крыше (Рестораны)"},{"id":108,"slug":"shops","name":"Магазины (Магазины)"},{"id":109,"slug":"vintage","name":"Винтажные магазины (Магазины)"},{"id":110,"slug":"handmade","name":"HandMade"},{"id":111,"slug":"other","name":"Прочее"},{"id":112,"slug":"business","name":"Бизнес-центры"},{"id":113,"slug":"art-centers","name":"Арт-центры"},{"id":114,"slug":"animal-shelters","name":"Питомники"},{"id":116,"slug":"bazy-otdyha","name":"Базы отдыха (Загородный отдых)"},{"id":117,"slug":"kottedzhi","name":"Коттеджи (Загородный отдых)"},{"id":118,"slug":"pansionaty","name":"Пансионаты (Загородный отдых)"},{"id":119,"slug":"sanatorii","name":"Санатории (Загородный отдых)"},{"id":120,"slug":"doma-otdyha","name":"Дома отдыха (Загородный отдых)"},{"id":121,"slug":"campings","name":"Кемпинги (Загородный отдых)"},{"id":122,"slug":"lakes","name":"Озёра (Загородный отдых)"},{"id":123,"slug":"airports","name":"Аэропорты"},{"id":124,"slug":"dance-studio","name":"Танцевальные студии"},{"id":125,"slug":"stomatologiya","name":"Стоматология (Красота и здоровье)"},{"id":126,"slug":"farmer-shops","name":"Фермерские магазины"},{"id":127,"slug":"workshops","name":"Мастерские"},{"id":128,"slug":"rope-park","name":"Веревочные парки (Отдых)"},{"id":129,"slug":"sport-centers","name":"спортивные комплексы (Интересн места, Красота )"},{"id":130,"slug":"art-space","name":"Арт-пространства"},{"id":131,"slug":"gay-bar","name":"Гей бар"},{"id":132,"slug":"bar-s-zhivoj-muzykoj","name":"Бар с живой музыкой"},{"id":133,"slug":"strip-club","name":"Стрип-клуб"},{"id":134,"slug":"brewery","name":"Пивоварня"},{"id":135,"slug":"comedy-club","name":"Камеди клаб"},{"id":136,"slug":"rynok","name":"Рынок"},{"id":137,"slug":"prirodnyj-zapovednik","name":"Природный заповедник"},{"id":138,"slug":"pub","name":"Паб"},{"id":139,"slug":"questroom","name":"Квест-комнаты"}]
"""
