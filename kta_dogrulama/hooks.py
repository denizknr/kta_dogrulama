app_name = "kta_dogrulama"
app_title = "KTA Dogrulama"
app_publisher = "KTA Endüstri"
app_description = "Test ve Form Masası Aparat Doğrulama Kayıt Formu (PTR 07/222-02)"
app_email = "info@kta.com.tr"
app_license = "MIT"
app_version = "1.0.0"

fixtures = [
    {
        "doctype": "Module Def",
        "filters": [["module_name", "in", ["KTA Dogrulama"]]]
    }
]

after_install = "kta_dogrulama.setup.after_install"
