from aiogram.types import User, Chat

TEST_USER = User(id=123, is_bot=False, first_name='test', last_name='bot',
                 username='testbot', language_code='ru-RU', is_premium=False, added_to_attachment_menu=None,
                 can_read_all_group_messages=None, supports_inline_queries=None
                 )

TEST_USER_CHAT = Chat(id=12, type='private', title=None, username=TEST_USER.username, first_name=TEST_USER.first_name,
                      last_name=TEST_USER.last_name, photo=None, bio=None, has_private_forwards=None,
                      join_to_send_message=None, join_by_request=None, description=None, invite_link=None,
                      pinned_message=None, permissions=None, slow_mode_delay=None, message_auto_delete_time=None,
                      has_protected_content=None, sticker_set_name=None, cat_set_sticker_set=None, linked_chat_id=None,
                      location=None
                      )