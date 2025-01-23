from aiogram.filters.callback_data import CallbackData

class CallBackDataObject(CallbackData, prefix='test'):
    text: str
    user_id: int