from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

class VIPWalletApp(App):
    def build(self):
        # Background color set to dark
        Window.clearcolor = (0.1, 0.1, 0.1, 1)
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        title = Label(
            text='Welcome to VIP Wallet',
            font_size='32sp',
            bold=True,
            color=(1, 0.84, 0, 1) # Gold color
        )
        
        status = Label(
            text='Security: Active\nStatus: Encrypted',
            font_size='18sp',
            color=(1, 1, 1, 1)
        )
        
        layout.add_widget(title)
        layout.add_widget(status)
        
        return layout

if __name__ == '__main__':
    VIPWalletApp().run()
