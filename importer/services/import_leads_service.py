import pandas as pd
from courses.models import BaseCourse, Course, Register
from customers.models import Customer, ReferralType
from accounts.utils import phone_number_validator
from importer.services.base_import_service import BaseImportService


# todo should refactor for a safe way instead upload public
class ImportLeadService(BaseImportService):

    def create_base_course(self, title, description):
        base_course, _ = BaseCourse.objects.get_or_create(
            title=title,
            defaults={
                "description": description,
            },
        )
        return base_course

    def get_or_create_customer(self, entry,ref):
        try:
            customer = Customer.objects.create(
                phone_number=phone_number_validator(str(entry["شماره موبایل"])) if not pd.isna(
                    entry["شماره موبایل"]) else None,
                seller=None,
                email=entry["Gmail"] if not pd.isna(entry["Gmail"]) else None,
                first_name=entry["نام"],
                last_name=entry["نام خانوادگی"],
                referral=ref,
            )
        except Exception as e:
            customer = Customer.objects.get(
                phone_number=phone_number_validator(str(entry["شماره موبایل"])))

        return customer

    def get_or_create_course(self, base_course, code):
        c, _ = Course.objects.get_or_create(
            base_course=base_course,
            code=int(code),
        )
        return c

    def register_customer(self, customer, base_course, code):
        if pd.isna(code):
            return
        c = self.get_or_create_course(base_course, code)
        Register.objects.get_or_create(
            customer=customer,
            course=c
        )


    def import_data(self):

        one = self.create_base_course("One", "One")
        trade = self.create_base_course("Trade", "Trade")
        mentoring = self.create_base_course("Mentoring", "Mentoring")


        for entry in self.data_list:
            ref, _ = ReferralType.objects.get_or_create(
                title=entry["معرف"]
            )
            customer = self.get_or_create_customer(entry,ref)

            self.register_customer(customer, one, entry["One"])
            self.register_customer(customer, trade, entry["Trade"])
            self.register_customer(customer, mentoring, entry["Mentoring"])
