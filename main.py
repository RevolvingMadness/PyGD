from pygd import PyGD

pygd_instance = PyGD("CCLocalLevels.dat")

pygd_instance.write_to_file("CCLocalLevelsGenerated.xml")

levels = pygd_instance.get_levels()
