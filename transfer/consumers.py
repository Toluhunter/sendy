from asgiref.sync import async_to_sync

from channels.generic.websocket import JsonWebsocketConsumer

class Chat(JsonWebsocketConsumer):

    def connect(self):
        
        self.group_name = self.scope["url_route"]["kwargs"]["chat_name"]
        async_to_sync(self.channel_layer.group_add)(self.group_name, self.channel_name)
        self.accept()
    
    def receive_json(self, content, **kwargs):
        
        async_to_sync(self.channel_layer.group_send)(self.group_name, {"type": "chat", "content":content})
    
    def chat(self, event):

        self.send_json(event["content"])
    
    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(self.group_name, self.channel_name)
        return super().disconnect(code)
    

