import pandas as pd
from customers.models import Customer
from accounts.models import User
from accounts.utils import phone_number_validator
from importer.services.base_import_service import BaseImportService
from convertdate import persian
from django.core.exceptions import ObjectDoesNotExist
import datetime


class UpdateLeadService(BaseImportService):

    def import_data(self):
        for entry in self.data_list:

            #Empty row checkup
            if not entry["لطفا شماره موبایل خود را با فونت انگلیسی وارد کنید."]:
                    print("Empty Row!")
                    continue
            
            #Convert Jalali date to Gregorian
            if not pd.isna(entry['لطفا تاریخ تولد خود را وارد کنید']):
                date_list = entry['لطفا تاریخ تولد خود را وارد کنید'].split("/")
                date_list = persian.to_gregorian(year=int(date_list[0]), month=int(date_list[1]), day=int(date_list[2]))
                entry['لطفا تاریخ تولد خود را وارد کنید'] = datetime.date(date_list[0], date_list[1], date_list[2])
            else:
                entry['لطفا تاریخ تولد خود را وارد کنید'] = None

            #Translate Gender to English
            if not pd.isna(entry['لطفا جنسیت خود را مشخص کنید']):
                if entry['لطفا جنسیت خود را مشخص کنید'] == "زن":
                    entry['لطفا جنسیت خود را مشخص کنید'] = "female"
                elif entry['لطفا جنسیت خود را مشخص کنید'] == "مرد":
                    entry['لطفا جنسیت خود را مشخص کنید'] = "male"
            else:
                entry['لطفا جنسیت خود را مشخص کنید'] = None

            #Customer Update
            try:
                customer = Customer.objects.get(
                phone_number=phone_number_validator(str(int(entry['لطفا شماره موبایل خود را با فونت انگلیسی وارد کنید.'])))
                )
                customers = Customer.objects.filter(
                phone_number=phone_number_validator(str(int(entry['لطفا شماره موبایل خود را با فونت انگلیسی وارد کنید.'])))
                ).update(
                    first_name=entry['لطفا نام \xa0شناسنامه ای خود را به فارسی وارد کنید'] if not pd.isna(entry['لطفا نام \xa0شناسنامه ای خود را به فارسی وارد کنید']) else None,

                    last_name=entry['لطفا نام خانوادگی شناسنامه ای خود را (به همراه پسوند) وارد کنید'] if not pd.isna(entry['لطفا نام خانوادگی شناسنامه ای خود را (به همراه پسوند) وارد کنید']) else None,

                    national_code=str(int(entry['لطفا کد ملی خود را\xa0 با فونت انگلیسی وارد کنید'])) if not pd.isna(entry['لطفا کد ملی خود را\xa0 با فونت انگلیسی وارد کنید']) else None,

                    gender=entry['لطفا جنسیت خود را مشخص کنید'],

                    birth_date=entry['لطفا تاریخ تولد خود را وارد کنید'],

                    email=entry['لطفا جیمیل خود را وارد کنید'] if not pd.isna(entry['لطفا جیمیل خود را وارد کنید']) else None,

                    eng_first_name=entry['نام خود را به زبان انگلیسی به شکل صحیح وارد کنید'] if not pd.isna(entry['نام خود را به زبان انگلیسی به شکل صحیح وارد کنید']) else None,

                    eng_last_name=entry['نام خانوادگی خود را به همراه پسوند به زبان انگلیسی به شکل صحیح وارد کنید'] if not pd.isna(entry['نام خانوادگی خود را به همراه پسوند به زبان انگلیسی به شکل صحیح وارد کنید']) else None,
                )
                print("Customer Updated!")
                
            except ObjectDoesNotExist as e:
                print("Customer Doesn't Exist!")
                continue
            
            #User Update
            try:
                user = User.objects.get(phone_number=phone_number_validator(str(int(entry['لطفا شماره موبایل خود را با فونت انگلیسی وارد کنید.']))))
                users = User.objects.filter(
                phone_number=phone_number_validator(str(int(entry['لطفا شماره موبایل خود را با فونت انگلیسی وارد کنید.'])))
                ).update(
                    first_name=entry['لطفا نام \xa0شناسنامه ای خود را به فارسی وارد کنید'] if not pd.isna(entry['لطفا نام \xa0شناسنامه ای خود را به فارسی وارد کنید']) else None,

                    last_name=entry['لطفا نام خانوادگی شناسنامه ای خود را (به همراه پسوند) وارد کنید'] if not pd.isna(entry['لطفا نام خانوادگی شناسنامه ای خود را (به همراه پسوند) وارد کنید']) else None,

                    gender=entry['لطفا جنسیت خود را مشخص کنید'],

                    birth_date=entry['لطفا تاریخ تولد خود را وارد کنید'],

                    email=entry['لطفا جیمیل خود را وارد کنید'] if not pd.isna(entry['لطفا جیمیل خود را وارد کنید']) else None,

                )
                print("User Updated!")
                
            except ObjectDoesNotExist as e:
                print("User Doesn't Exist!")
                continue
