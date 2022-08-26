from service import models as service_doctors

from web import models as web_site_infos

def get_site_infos(request)-> dict:
    Site_infos = web_site_infos.SiteInfos.objects.first()
    return {'Site_infos': Site_infos}

def get_doctors(request)-> dict:
    doctors = service_doctors.Doctor.objects.all()
    return {'doctors': doctors}