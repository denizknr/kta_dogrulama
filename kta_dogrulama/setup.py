import frappe


def after_install():
    frappe.db.commit()
    print("KTA Doğrulama uygulaması başarıyla yüklendi.")
    print("Test Masası Doğrulama Kaydı DocType'ı kullanıma hazır.")
