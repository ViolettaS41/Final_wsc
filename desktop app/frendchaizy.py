from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import Screen
from kivymd.uix.screenmanager import ScreenManager
from kivymd.uix.menu import MDDropdownMenu
import requests

class AutorizationScreen(Screen):
    def check_autoriz(self):
        login = self.ids.login_input.text
        password = self.ids.password_input.text

        responce = requests.get('http://localhost:8000/autorizatoin/', params={'login': login, 'password': password})

        if responce.status_code==200:
            self.ids.error_label.text=''
            login = ''
            password= ''
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
            },
            {'viewclass': 'OneLineListItem',
            'text': 'Мои сессии',},
            {
                'viewclass': 'OneLineListItem',
                'text': 'Выход',
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
             'text':'Модемы'},
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
        

class CompanyScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.menu_item=[
            {'viewclass': 'OneLineListItem',
            'text': 'Мой профиль',
            },
            {'viewclass': 'OneLineListItem',
            'text': 'Мои сессии',},
            {
                'viewclass': 'OneLineListItem',
                'text': 'Выход',
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
             'text':'Модемы'},
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

class AutomatScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.menu_item=[
            {'viewclass': 'OneLineListItem',
            'text': 'Мой профиль',
            },
            {'viewclass': 'OneLineListItem',
            'text': 'Мои сессии',},
            {
                'viewclass': 'OneLineListItem',
                'text': 'Выход',
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
             'text':'Модемы'},
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

class WindowManager(ScreenManager):
    pass

class FrendchaizyApp(MDApp):
    
    def build(self):
        return Builder.load_file('frn.kv')
    

FrendchaizyApp().run()