from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup

shopping_list = []

class ShoppingListApp(App):
    def build(self):
        self.title = "Shopping List"

        main_layout = BoxLayout(orientation='vertical')

        self.list_layout = BoxLayout(orientation='vertical', size_hint_y=None)
        self.list_layout.bind(minimum_height=self.list_layout.setter('height'))

        self.scroll_view = ScrollView(size_hint=(1, 0.8))
        self.scroll_view.add_widget(self.list_layout)

        main_layout.add_widget(self.scroll_view)

        input_layout = BoxLayout(size_hint=(1,0.1))

        self.input_text = TextInput(hint_text="Enter new item")
        input_layout.add_widget(self.input_text)

        add_button = Button(text="Add Item", on_press=self.add_item)
        input_layout.add_widget(add_button)

        main_layout.add_widget(input_layout)

        button_layout = BoxLayout(size_hint=(1,0.1))

        delete_button = Button(text="Delete Item", on_press=self.delete_item)
        button_layout.add_widget(delete_button)

        clear_button = Button(text="Clear List", on_press=self.clear_list)
        button_layout.add_widget(clear_button)

        save_button = Button(text="Save List", on_press=self.save_list)
        button_layout.add_widget(save_button)

        load_button = Button(text="Load List", on_press=self.load_list)
        button_layout.add_widget(load_button)

        main_layout.add_widget(button_layout)

        return main_layout


    def add_item(self, instance):
        item = self.input_text.text
        if item:
            shopping_list.append(item)
            self.update_list()
            self.input_text.text = ""

    def delete_item(self, instance):
        if shopping_list:
            item_to_delete = shopping_list.pop()
            self.update_list()
            popup = Popup(title='Item Deleted',
                          content=Label(text=f"'{item_to_delete}' has been removed from the shopping list."),
                          size_hint=(0.6, 0.4))
            popup.open()
        else:
            popup = Popup(title='Error',
                          content=Label(text='Shopping list is empty.'),
                          size_hint=(0.6, 0.4))
            popup.open()

    def clear_list(self, instance):
        shopping_list.clear()
        self.update_list()

    def save_list(self, instance):
        with open("shopping_list.txt", 'w') as file:
            for item in shopping_list:
                file.write(f"{item}\n")
        popup = Popup(title='Save List',
                      content=Label(text='Shopping list saved to shopping_list.txt'),
                      size_hint=(0.6, 0.4))
        popup.open()

    def load_list(self, instance):
        try:
            with open("shopping_list.txt", 'r') as file:
                global shopping_list
                shopping_list = [line.strip() for line in file]
            self.update_list()
            popup = Popup(title='Load List',
                          content=Label(text='Shopping list loaded from shopping_list'),
                          size_hint=(0.6, 0.4))
            popup.open()
        except FileNotFoundError:
            popup = Popup(title='Load List',
                          content=Label(text='No saved shopping list found.'),
                          size_hint=(0.6, 0.4))
            popup.open()
        except Exception as e:
            popup = Popup(title='Error',
                          content=Label(text=f'An error occurred: {e}'),
                          size_hint=(0.6, 0.4))
            popup.open()

    def update_list(self):
        self.list_layout.clear_widgets()
        for item in shopping_list:
            self.list_layout.add_widget(Label(text=item, size_hint_y=None, height=40))

if __name__ == '__main__':
    ShoppingListApp().run()