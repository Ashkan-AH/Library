from celery import shared_task
from importer.services.import_leads_service import ImportLeadService
from importer.services.update_leads_service import UpdateLeadService


@shared_task(bind=True)
def import_excel_task(self, file_importer_id):
    from importer.models import FileImporterModel

    obj = FileImporterModel.objects.get(id=file_importer_id)
    if obj.import_type == FileImporterModel.ExcelFileType.NEW_LEADS:
        ImportLeadService(obj.data_file.url)
    if obj.import_type == FileImporterModel.ExcelFileType.UPDATE_LEADS_DATA:
        UpdateLeadService(obj.data_file.url)

    # CustomerExcelImporter(ifu.data_file.open('r'))
    obj.is_imported = True
    obj.save()
