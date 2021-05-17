import urllib,json
from urllib.request import urlopen
from kivy.app import App
from kivy.lang import Builder


READ_API_KEY='Y9VK48WE8V3W3G1D'
CHANNEL_ID=858583


kv = '''
GridLayout:
    rows: 1
    Button:
        on_release:
            app.set_text()
    Label:
        text: "Nothing yet"
        id: my_label

'''


class Myapp(App):
    def build(self):
        return Builder.load_string(kv)

    def set_text(self):
        my_label = self.root.ids.my_label
        conn = urlopen("http://api.thingspeak.com/channels/%s/feeds/last.json?api_key=%s" \
                           % (CHANNEL_ID,READ_API_KEY))
        response = conn.read()
        data=json.loads(response)
        my_label.text = (data['field1'])
        

if __name__ == "__main__":
    Myapp().run()

  