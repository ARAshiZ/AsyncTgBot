__all__ = ['register_user_commands']

from aiogram.fsm.state import default_state

from aiogram import Router
from aiogram.filters import CommandStart, Command, StateFilter
from aiogram import F

from bot.commands.common import cmd_cancel_no_state, cmd_order, cmd_cancel
from bot.commands.download import download_command
from bot.commands.help import help_command, call_help
from bot.commands.insertAbout import insert_about, AboutForm, process_info, process_info_title
from bot.commands.insertEmployee import EmployeeForm, process_user_id, insert_employee, process_offer
from bot.commands.insertJobs import insert_jobs, JobsForm, process_title, process_payment, process_high_education, \
    process_result
from bot.commands.insertSubscribe import insert_subscribe, process_sub_title, process_sub_date, process_sub_price, \
    SubscribeForm
from bot.commands.ordering import available_food_names, OrderFood, food_choosen_incorrectly, cmd_food, food_chosen, \
    food_size_chosen, available_food_sizes, food_size_chosen_incorrectly
from bot.commands.start import create_menu, bring_to_main, create_reaply_keyboard1, create_reaply_keyboard2
from bot.commands.sticker import sticker_command, call_sticker
from bot.commands.upload import upload_command
from bot.middlewares.register_check import RegisterCheck


def register_user_commands(router: Router) -> None:

    router.message.register(create_menu, CommandStart())
    router.message.register(help_command, Command(commands=['help']))
    router.message.register(download_command, Command(commands=['download']),
                            F.content_type.in_({'photo', 'video', 'audio', 'text'}))
    router.message.register(upload_command, Command(commands=['upload']),
                            F.content_type.in_({'photo', 'video', 'audio', 'text'}))
    router.message.register(sticker_command, Command(commands=['sticker']))
    router.message.register(RegisterCheck)
    register_insert_emloyee(router)
    register_insert_job(router)
    register_insert_about(router)
    register_insert_subscribe(router)

    router.callback_query.register(RegisterCheck)
    router.callback_query.register(bring_to_main, F.data == 'back')
    router.callback_query.register(call_help, F.data == 'help')
    router.callback_query.register(call_sticker, F.data == 'sticker')
    router.callback_query.register(create_reaply_keyboard1, F.data == 'create_reaply1')
    router.callback_query.register(create_reaply_keyboard2, F.data == 'create_reaply2')

def register_insert_emloyee(router: Router):
    router.message.register(insert_employee, Command(commands=['employee']))
    router.message.register(process_user_id, EmployeeForm.waiting_for_user_id)
    router.message.register(process_offer, EmployeeForm.waiting_for_offer)

def register_insert_job(router: Router):
    router.message.register(insert_jobs, Command(commands=['job']))
    router.message.register(process_title, JobsForm.waiting_for_title)
    router.message.register(process_payment, JobsForm.waiting_for_payment)
    router.message.register(process_high_education, JobsForm.waiting_for_high_education)
    router.message.register(process_result, JobsForm.result_state)

def register_insert_about(router: Router):
    router.message.register(insert_about, Command(commands=['about']))
    router.message.register(process_info_title, AboutForm.waiting_for_model_title)
    router.message.register(process_info, AboutForm.waiting_for_model_info)
    router.message.register(process_result, AboutForm.result_state)

def register_insert_subscribe(router: Router):
    router.message.register(insert_subscribe, Command(commands=['subscribe']))
    router.message.register(process_sub_title, SubscribeForm.waiting_for_sub_title)
    router.message.register(process_sub_date, SubscribeForm.waiting_for_sub_term)
    router.message.register(process_sub_price, SubscribeForm.waiting_for_sub_price)
    router.message.register(process_result, SubscribeForm.result_state)

def register_orders_command(router: Router):
    router.message.register(cmd_order, Command(commands=['oreder']), StateFilter(None))
    router.message.register(cmd_cancel_no_state, F.text.lower() == 'отмена', default_state)
    router.message.register(cmd_cancel, Command(commands=['order']), F.text.lower() == 'отмена')

    router.message.register(cmd_food, Command(commands=['food']))
    router.message.register(food_chosen, F.text.in_(available_food_names), OrderFood.choosing_food_name)
    router.message.register(food_choosen_incorrectly, StateFilter('OrderFood:choosing_food_name'))
    router.message.register(food_size_chosen, F.text.in_(available_food_sizes), OrderFood.choosing_food_size)
    router.message.register(food_size_chosen_incorrectly, OrderFood.choosing_food_size)

