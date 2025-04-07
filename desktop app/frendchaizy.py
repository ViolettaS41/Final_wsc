from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import Screen
from kivymd.uix.screenmanager import ScreenManager
from kivymd.uix.menu import MDDropdownMenu
import requests
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivymd.uix.anchorlayout import MDAnchorLayout

class AutorizationScreen(Screen):
    def check_autoriz(self):
        login = self.ids.login_input.text
        password = self.ids.password_input.text

        responce = requests.get('http://localhost:8000/autorizatoin/', params={'login': login, 'password': password})

        if responce.status_code==200:
            self.ids.error_label.text=''
            self.manager.current='main'
        elif responce.status_code==404:
            self.ids.error_label.text='Ошибка: неверный email/телефон или пароль'
        else:
            self.ids.error_label.text='Ошибка: не удалось подключиться'

class MainScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.menu_item=[
            {'viewclass': 'OneLineListItem',
            'text': 'Мой профиль',
            'icon_left': 'account'
            },
            {'viewclass': 'OneLineListItem',
            'text': 'Мои сессии',
            'icon_left': 'lock', },
            {
                'viewclass': 'OneLineListItem',
                'text': 'Выход',
                'icon_left': 'logout',
                'on_release': lambda x='logout': self.menu_callback(x),
            }
        ]
        self.dropdownmenu = None

        self.admin_menu_item=[
            {'viewclass':'OneLineListItem',
             'text':'Торговые автоматы',
             'on_release': lambda x='automat': self.menu_callback(x)},
            {'viewclass':'OneLineListItem',
             'text':'Компании',
             'on_release': lambda x="company": self.menu_callback(x)},
            {'viewclass':'OneLineListItem',
             'text':'Пользователи'},
            {'viewclass':'OneLineListItem',
             'text':'Модемы',
             'on_release': lambda x='modem': self.menu_callback(x)},
            {'viewclass':'OneLineListItem',
             'text':'Дополнительные'},
        ]
        self.admin_dropdownmenu = None
    def open_user_menu(self):
        if not self.dropdownmenu:
            self.dropdownmenu = MDDropdownMenu(
                caller= self.ids.user_profile,
                items = self.menu_item,
                width_mult=4,
            )
        self.dropdownmenu.open()

    def open_admin_menu(self):
        if not self.admin_dropdownmenu:
            self.admin_dropdownmenu=MDDropdownMenu(
                caller=self.ids.admin_btn,
                items=self.admin_menu_item,
                width_mult=6
            )
        self.admin_dropdownmenu.open()
    def menu_callback(self, text):
        if text == "company":
            self.manager.current = "company"
        elif text=='automat':
            self.manager.current='automat'
        elif text=='logout':
            self.manager.current='auto'
        elif text=='modem':
            self.manager.current='modem'
        

class CompanyScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

        self.menu_item=[
            {'viewclass': 'OneLineListItem',
            'text': 'Мой профиль',
            'icon_left': 'account'
            },
            {'viewclass': 'OneLineListItem',
            'text': 'Мои сессии',
            'icon_left': 'lock', },
            {
                'viewclass': 'OneLineListItem',
                'text': 'Выход',
                'icon_left': 'logout',
                'on_release': lambda x='logout': self.menu_callback(x),
            }
        ]
        self.dropdownmenu = None

        self.admin_menu_item=[
            {'viewclass':'OneLineListItem',
             'text':'Торговые автоматы',
             'on_release': lambda x='automat': self.menu_callback(x)},
            {'viewclass':'OneLineListItem',
             'text':'Компании',
             'on_release': lambda x="company": self.menu_callback(x)},
            {'viewclass':'OneLineListItem',
             'text':'Пользователи'},
            {'viewclass':'OneLineListItem',
             'text':'Модемы',
             'on_release': lambda x='modem': self.menu_callback(x)},
            {'viewclass':'OneLineListItem',
             'text':'Дополнительные'},
        ]
        self.admin_dropdownmenu = None

        self.data_table=None
    def open_user_menu(self):
        if not self.dropdownmenu:
            self.dropdownmenu = MDDropdownMenu(
                caller= self.ids.user_profile,
                items = self.menu_item,
                width_mult=4,
            )
        self.dropdownmenu.open()

    def open_admin_menu(self):
        if not self.admin_dropdownmenu:
            self.admin_dropdownmenu=MDDropdownMenu(
                caller=self.ids.admin_btn,
                items=self.admin_menu_item,
                width_mult=6
            )
        self.admin_dropdownmenu.open()
    def menu_callback(self, text):
        if text == "company":
            self.manager.current = "company"
        elif text=='automat':
            self.manager.current='automat'
        elif text=='logout':
            self.manager.current='auto'
        elif text=='modem':
            self.manager.current='modem'


    def on_enter(self, *args):
        if not self.data_table:
            self.create_datatable()

    def create_datatable(self):
        layout = MDAnchorLayout()
        self.data_table = MDDataTable(
            size_hint=(0.9,0.9),
            use_pagination=True,
            sorted_on='Название',
            column_data=[
                ('Название', dp(30)),
                ('Вышестоящая', dp(40)),
                ('Адрес', dp(30)),
                ('Контакты', dp(30)),
                ('В работе с', dp(40)),
                ('Действия', dp(30)),
            ],
            row_data=[
                ("ТА1", "Компания А", "ул. Ленина, 1", "+79991234567", "01.01.2023", "Редактировать"),
                ("ТА2", "Компания Б", "ул. Пушкина, 2", "+79999876543", "15.03.2023", "Удалить"),
            ],
        )
        layout.add_widget(self.data_table)
        self.ids.table_layout.add_widget(layout)
    

class AutomatScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.menu_item=[
            {'viewclass': 'OneLineListItem',
            'text': 'Мой профиль',
            'icon_left': 'account'
            },
            {'viewclass': 'OneLineListItem',
            'text': 'Мои сессии',
            'icon_left': 'lock', },
            {
                'viewclass': 'OneLineListItem',
                'text': 'Выход',
                'icon_left': 'logout',
                'on_release': lambda x='logout': self.menu_callback(x),
            }
        ]
        self.dropdownmenu = None

        self.admin_menu_item=[
            {'viewclass':'OneLineListItem',
             'text':'Торговые автоматы',
             'on_release': lambda x='automat': self.menu_callback(x)},
            {'viewclass':'OneLineListItem',
             'text':'Компании',
             'on_release': lambda x="company": self.menu_callback(x)},
            {'viewclass':'OneLineListItem',
             'text':'Пользователи'},
            {'viewclass':'OneLineListItem',
             'text':'Модемы',
             'on_release': lambda x='modem': self.menu_callback(x)},
            {'viewclass':'OneLineListItem',
             'text':'Дополнительные'},
        ]
        self.admin_dropdownmenu = None
        self.data_table = None

    def on_enter(self, *args):
        if not self.data_table:
            self.create_datatable()

    def create_datatable(self):
        layout = MDAnchorLayout()
        self.data_table = MDDataTable(
            size_hint=(0.9,0.9),
            use_pagination=True,
            sorted_on='Название автомата',
            column_data=[
                ('id', dp(20)),
                ('Название автомата', dp(30)),
                ('Модель', dp(30)),
                ('Компания', dp(30)),
                ('Модем', dp(30)),
                ('Адрес/место', dp(40)),
                ('В работе с', dp(30)),
                ('Действия', dp(30)),
            ],
            row_data=[
                ("12432", "ГП Магнит", "400", "ООО", "121434546", "ул.Ленина 34 у входа", "12.03.2025", "Редактировать"),
                ("435252", "БЦ Московский", "546", "OAO", "1232453566","ул.Барина 3", "01.01.2025", "Редактровать"),
            ],
        )
        layout.add_widget(self.data_table)
        self.ids.automat_layout.add_widget(layout)


    def open_user_menu(self):
        if not self.dropdownmenu:
            self.dropdownmenu = MDDropdownMenu(
                caller= self.ids.user_profile,
                items = self.menu_item,
                width_mult=4,
            )
        self.dropdownmenu.open()

    def open_admin_menu(self):
        if not self.admin_dropdownmenu:
            self.admin_dropdownmenu=MDDropdownMenu(
                caller=self.ids.admin_btn,
                items=self.admin_menu_item,
                width_mult=6
            )
        self.admin_dropdownmenu.open()
    def menu_callback(self, text):
        if text == "company":
            self.manager.current = "company"
        elif text=='automat':
            self.manager.current='automat'
        elif text=='logout':
            self.manager.current='auto'
        elif text=='modem':
            self.manager.current='modem'

class ModemScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.menu_item=[
            {'viewclass': 'OneLineListItem',
            'text': 'Мой профиль',
            'icon_left': 'account'
            },
            {'viewclass': 'OneLineListItem',
            'text': 'Мои сессии',
            'icon_left': 'lock', },
            {
                'viewclass': 'OneLineListItem',
                'text': 'Выход',
                'icon_left': 'logout',
                'on_release': lambda x='logout': self.menu_callback(x),
            }
        ]
        self.dropdownmenu = None

        self.admin_menu_item=[
            {'viewclass':'OneLineListItem',
             'text':'Торговые автоматы',
             'on_release': lambda x='automat': self.menu_callback(x)},
            {'viewclass':'OneLineListItem',
             'text':'Компании',
             'on_release': lambda x="company": self.menu_callback(x)},
            {'viewclass':'OneLineListItem',
             'text':'Пользователи'},
            {'viewclass':'OneLineListItem',
             'text':'Модемы',
             'on_release': lambda x='modem': self.menu_callback(x)},
            {'viewclass':'OneLineListItem',
             'text':'Дополнительные'},
        ]
        self.admin_dropdownmenu = None
    def open_user_menu(self):
        if not self.dropdownmenu:
            self.dropdownmenu = MDDropdownMenu(
                caller= self.ids.user_profile,
                items = self.menu_item,
                width_mult=4,
            )
        self.dropdownmenu.open()

    def open_admin_menu(self):
        if not self.admin_dropdownmenu:
            self.admin_dropdownmenu=MDDropdownMenu(
                caller=self.ids.admin_btn,
                items=self.admin_menu_item,
                width_mult=6
            )
        self.admin_dropdownmenu.open()
    def menu_callback(self, text):
        if text == "company":
            self.manager.current = "company"
        elif text=='automat':
            self.manager.current='automat'
        elif text=='logout':
            self.manager.current='auto'
        elif text=='modem':
            self.manager.current='modem'

class AddingCompanyScreen(Screen):
    pass

class AddingAutomatcreen(Screen):
    pass

class MonitorTAScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.menu_item=[
            {'viewclass': 'OneLineListItem',
            'text': 'Мой профиль',
            'icon_left': 'account'
            },
            {'viewclass': 'OneLineListItem',
            'text': 'Мои сессии',
            'icon_left': 'lock', },
            {
                'viewclass': 'OneLineListItem',
                'text': 'Выход',
                'icon_left': 'logout',
                'on_release': lambda x='logout': self.menu_callback(x),
            }
        ]
        self.dropdownmenu = None

        self.admin_menu_item=[
            {'viewclass':'OneLineListItem',
             'text':'Торговые автоматы',
             'on_release': lambda x='automat': self.menu_callback(x)},
            {'viewclass':'OneLineListItem',
             'text':'Компании',
             'on_release': lambda x="company": self.menu_callback(x)},
            {'viewclass':'OneLineListItem',
             'text':'Пользователи'},
            {'viewclass':'OneLineListItem',
             'text':'Модемы',
             'on_release': lambda x='modem': self.menu_callback(x)},
            {'viewclass':'OneLineListItem',
             'text':'Дополнительные'},
        ]
        self.admin_dropdownmenu = None
    def open_user_menu(self):
        if not self.dropdownmenu:
            self.dropdownmenu = MDDropdownMenu(
                caller= self.ids.user_profile,
                items = self.menu_item,
                width_mult=4,
            )
        self.dropdownmenu.open()

    def open_admin_menu(self):
        if not self.admin_dropdownmenu:
            self.admin_dropdownmenu=MDDropdownMenu(
                caller=self.ids.admin_btn,
                items=self.admin_menu_item,
                width_mult=6
            )
        self.admin_dropdownmenu.open()
    def menu_callback(self, text):
        if text == "company":
            self.manager.current = "company"
        elif text=='automat':
            self.manager.current='automat'
        elif text=='logout':
            self.manager.current='auto'
        elif text=='modem':
            self.manager.current='modem'

class WindowManager(ScreenManager):
    pass

class FrendchaizyApp(MDApp):
    
    def build(self):
        self.theme_cls.theme_style = "Light" 
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.accent_palette = "Amber"
        self.theme_cls.material_style = "M3" 
        return Builder.load_file('frn.kv')
    

FrendchaizyApp().run()